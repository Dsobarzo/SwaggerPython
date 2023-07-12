# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body_profesor_post import BodyProfesorPost  # noqa: E501
from swagger_server.models.exito_profesor_get import ExitoProfesorGet  # noqa: E501
from swagger_server.models.exito_profesor_modificar import ExitoProfesorModificar  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProfesoresController(BaseTestCase):
    """ProfesoresController integration test stubs"""

    def test_borrarprofesor_id_delete(self):
        """Test case for borrarprofesor_id_delete

        Elimina un profesor existente
        """
        response = self.client.open(
            '//borrarprofesor/{id}'.format(id=1.2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_guardar_profesor(self):
        """Test case for guardar_profesor

        Agrega un Profesor a la base de datos.
        """
        body = BodyProfesorPost()
        response = self.client.open(
            '//guardarprofesor',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_listas_profesores(self):
        """Test case for listas_profesores

        Consulta a la base de datos todos los profesores existentes en ella.
        """
        response = self.client.open(
            '//obtenerprofesores',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modificarprofesor_id_put(self):
        """Test case for modificarprofesor_id_put

        Modificar un profesor existente
        """
        body = BodyProfesorPost()
        response = self.client.open(
            '//modificarprofesor/{id}'.format(id=1.2),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
