# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exito_carrera_get import ExitoCarreraGet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCarrerasController(BaseTestCase):
    """CarrerasController integration test stubs"""

    def test_listas_carreras(self):
        """Test case for listas_carreras

        Consulta a la base de datos todas las Carreras existentes en ella.
        """
        response = self.client.open(
            '//obtenercarreras',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
