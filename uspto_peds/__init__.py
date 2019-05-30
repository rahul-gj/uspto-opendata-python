"""Module for simple peds search"""
import logging
import json

import requests
from bs4 import BeautifulSoup


__version__ = '0.8.4'
logger = logging.getLogger(__name__)


class PEDSClient:
    """
    Simple Python client for simple searching the USPTO Patent Examination Data System API (https://ped.uspto.gov/peds/).
    stolen from (Via fork) from https://github.com/ip-tools/uspto-opendata-python
    See also: https://ped.uspto.gov/peds/#/apiDocumentation
    Module is self explanatory. for detailed explanation see original package.
    """
    QUERY_URL = 'https://ped.uspto.gov/api/queries'

    def __init__(self):
        self.session = requests.Session()

    def query(self, expression):
        logger.info('Querying for expression=%s', expression)
        solr_query = {
            'searchText': expression,
            'df': 'patentNumber',
            'facet': True,
            'fl': '*',
            'fq': [],
            'qf': 'appEarlyPubNumber applId patentNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber',
            'sort': 'applId asc',
        }

        response = self.session.post(self.QUERY_URL, json=solr_query)

        if response.status_code != 200:

            message = u'Error while querying for {}'.format(expression)
            if response.text:
                message += u'\n{}'.format(response.text)
            logger.error(message)

            if 'Content-Type' in response.headers and response.headers['Content-Type'].startswith('text/html'):
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('title')
                message = title.string.strip()
                hr = soup.body.find('hr')
                reason = hr.next_sibling.string.strip()
                if reason:
                    message += u'. ' + reason
                message += ' (status={})'.format(response.status_code)
                logger.error(message)
                raise ValueError(message)
            else:
                message = u'API error. Status: {}, Reason: {}, Content-Type: {}'.format(
                    response.status_code, response.reason, response.headers.get('Content-Type'))
                logger.error(message)
                raise ValueError(message)

        return response.json()

    def search(self, *args):
        total_response = self.query(*args)
        search_response = total_response['queryResults']['searchResponse']

        result = search_response['response']

        metadata = {
            'indexLastUpdatedDate': total_response['queryResults']['indexLastUpdatedDate'],
            'queryId': total_response['queryResults']['queryId'],
            'responseHeader': search_response['responseHeader']
        }
        result.update(metadata=metadata)
        return result
