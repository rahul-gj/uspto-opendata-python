.. image:: https://img.shields.io/badge/PYthon3.6-green.svg

|

##########################
USPTO Peds API client
##########################


*****
About
*****
``uspto-peds-python`` is a client library for accessing the USPTO peds Data APIs.  It is written in Python.

Currently, it implements API wrappers for the

- `Patent Examination Data System (PEDS) search by numbers only`_

The PEDS systems contain bibliographic, published document and patent term extension data in Public PAIR from 1981 to present.
There is also some data dating back to 1935.

The PEDS system also provides information concerning the transaction activity that has occurred for each patent.
The transaction history includes the transaction date, transaction code and transaction description for each transaction activity.

.. _Patent Examination Data System (PEDS): https://ped.uspto.gov/peds/

.. attention::

    This is trimmed fork for limited use:
    Please see original full library at https://github.com/rahul-gj/uspto-peds-python

***************
Getting started
***************

Install
=======
If you know your way around Python, installing this software is really easy::

    pip install https://github.com/rahul-gj/uspto-peds-python/archive/master.zip

Please refer to the `virtualenv`_ page about further guidelines how to install and use this software.

.. _virtualenv: https://github.com/rahul-gj/uspto-peds-python/blob/master/docs/virtualenv.rst


Usage
=====
Please refer to the respective documentation about which API you want to access:

    from uspto_peds import PEDSClient

    client = PEDSClient()

    client.search('patentNumber:(6583088 6875727 8697602)')


*******************
Project information
*******************
``uspto-peds-python`` is released under the MIT license.
The code lives on `GitHub <https://github.com/rahul-gj/uspto-peds-python>`_ and
the Python package is to be published to `PyPI <https://pypi.org/project/uspto-peds-python/>`_.


The software has been tested on Python 3.6.

If you'd like to contribute you're most welcome!
Spend some time taking a look around, locate a bug, design issue or
spelling mistake and then send us a pull request or create an issue.

Thanks in advance for your efforts, we really appreciate any help or feedback.

Disclaimer
==========
The project and its authors are not affiliated with the USPTO in any way.
It is a sole project from the community for making data more accessible in the spirit of open data.


*******
Credits
*******
Thanks to the USPTO data team and all people working behind the scenes
for providing these excellent services to the community. You know who you are.


**********
Background
**********
The Patent Application Information Retrieval (PAIR) APIs let customers retrieve and download
multiple records of USPTO patent application or patent filing status at no cost.

They are part of the US Patent and Trademark Office's (USPTO) commitment to fostering a culture of open government as
described by the 2013 Executive Order 13642 to make open and machine-readable data the new default for government information
(`HTML <https://obamawhitehouse.archives.gov/the-press-office/2013/05/09/executive-order-making-open-and-machine-readable-new-default-government->`_,
`PDF <https://www.gpo.gov/fdsys/pkg/FR-2013-05-14/pdf/2013-11533.pdf>`_).

The API was conceived as part of the `USPTO Open Data Initiative`_, please also visit the `USPTO Open Data Portal`_
and its `API catalog`_ for other new APIs provided by the US Patent and Trademark Office.

The US Patent and Trademark office encourages innovators and entrepreneurs worldwide to publish their inventions
for worldwide use and adoption. They have opened their APIs to third party developers inside and outside of
government so that they can directly benefit from this data, by making and using their own apps.

For terms of use regarding their APIs and data, please visit the respective pages at `USPTO general terms`_ and
`PatentsView API terms`_. In general, the published material is in the public domain and may be freely distributed and
copied, but it is requested that in any subsequent use the United States Patent and Trademark Office (USPTO) be given
appropriate acknowledgement (e.g., "Source: United States Patent and Trademark Office, www.uspto.gov").

.. _USPTO Open Data Initiative: https://www.uspto.gov/learning-and-resources/open-data-and-mobility
.. _USPTO Open Data Portal: https://developer.uspto.gov/
.. _API catalog: https://developer.uspto.gov/api-catalog

.. _Bulk Data Products: https://www.uspto.gov/learning-and-resources/bulk-data-products
.. _Bulk search and download: https://developer.uspto.gov/api-catalog/bulk-search-and-download
.. _PAIR Bulk Data: https://developer.uspto.gov/api-catalog/pair-bulk-data

.. _USPTO general terms: https://www.uspto.gov/terms-use-uspto-websites#copyright
.. _PatentsView API terms: http://www.patentsview.org/api/faqs.html#what-api
