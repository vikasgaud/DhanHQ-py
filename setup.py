import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.3'
PACKAGE_NAME = 'dhanhq'
AUTHOR = 'Dhan'
AUTHOR_EMAIL = 'dhan-oss@dhan.co'
URL = ''

LICENSE = 'MIT LICENSE'
DESCRIPTION = 'The official Python client for communicating with the Dhan API'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["pandas>=1.4.3",
                    "requests>=2.28.1",
                    "websockets>=9.1"]
                    
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
