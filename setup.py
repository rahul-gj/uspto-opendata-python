import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'requests>=2.18.4',
    'beautifulsoup4==4.7.1',
]

setup(name='uspto-peds-python',
      version='0.8.4',
      description='uspto-peds-python is a client library for searching the USPTO PEDS Data APIs',
      long_description=README,
      license="MIT",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: WIN :: WIN 7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Archiving",
        "Topic :: Text Processing",
        "Topic :: Utilities",
      ],
      author='Andreas Motl',
      author_email='andreas.motl@ip-tools.org',
      url='https://github.com/rahul-gj/uspto-opendata-python',
      keywords='uspto pair pbd peds opendata bulk data download patent information research search',
      packages=find_packages(),
      include_package_data=True,
      package_data={
      },
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=[],
      dependency_links=[
        'https://github.com/kennethreitz/clint/tarball/9d3693d6#egg=clint-0.5.1',
      ],
    )
