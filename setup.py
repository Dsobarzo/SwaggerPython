# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Api Laboratorios de Simulacion (UMAG).",
    author_email="",
    url="",
    keywords=["Swagger", "Api Laboratorios de Simulacion (UMAG)."],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API programada en java spring boot V3.1.1 para manejar la informacion de los laboratorios de simulacion en la facultad de Ciencias de la salud (Universidad de Magallanes), con una base de datos postgresSQL en una instancia RDS-AWS y un backend SandBox railway (hambiente de desarrollo).
    """
)
