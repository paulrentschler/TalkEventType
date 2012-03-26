from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 
    'Products', 'TalkEventType', 'version.txt')).read().strip()

setup(name='Products.TalkEventType',
    version=version,
    description="A event specific to speakers giving talks.",
    long_description=open("README.txt").read() + "\n" +
                     open("HISTORY.txt").read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='Paul Rentschler, Huck Institutes of the Life Sciences',
    author_email='par117@psu.edu',
    url='http://www.huck.psu.edu/people/par117',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      # -*- Extra requirements: -*-
      'Products.Relations>=0.8.1',
      'Products.CMFPlone>=4.1',
      ],
    entry_points="""
      # -*- Entry points: -*-
      """,
    )
