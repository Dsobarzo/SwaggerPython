# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BodyProfesorPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nombre: str=None, apellido: str=None, email: str=None, id_carrera: int=None):  # noqa: E501
        """BodyProfesorPost - a model defined in Swagger

        :param nombre: The nombre of this BodyProfesorPost.  # noqa: E501
        :type nombre: str
        :param apellido: The apellido of this BodyProfesorPost.  # noqa: E501
        :type apellido: str
        :param email: The email of this BodyProfesorPost.  # noqa: E501
        :type email: str
        :param id_carrera: The id_carrera of this BodyProfesorPost.  # noqa: E501
        :type id_carrera: int
        """
        self.swagger_types = {
            'nombre': str,
            'apellido': str,
            'email': str,
            'id_carrera': int
        }

        self.attribute_map = {
            'nombre': 'nombre',
            'apellido': 'apellido',
            'email': 'email',
            'id_carrera': 'id_carrera'
        }
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._id_carrera = id_carrera

    @classmethod
    def from_dict(cls, dikt) -> 'BodyProfesorPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BodyProfesorPost of this BodyProfesorPost.  # noqa: E501
        :rtype: BodyProfesorPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nombre(self) -> str:
        """Gets the nombre of this BodyProfesorPost.

        Primer nombre del profesor.  # noqa: E501

        :return: The nombre of this BodyProfesorPost.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this BodyProfesorPost.

        Primer nombre del profesor.  # noqa: E501

        :param nombre: The nombre of this BodyProfesorPost.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def apellido(self) -> str:
        """Gets the apellido of this BodyProfesorPost.

        Primer apellido del profesor.  # noqa: E501

        :return: The apellido of this BodyProfesorPost.
        :rtype: str
        """
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        """Sets the apellido of this BodyProfesorPost.

        Primer apellido del profesor.  # noqa: E501

        :param apellido: The apellido of this BodyProfesorPost.
        :type apellido: str
        """

        self._apellido = apellido

    @property
    def email(self) -> str:
        """Gets the email of this BodyProfesorPost.

        E-Mail del Profesor.  # noqa: E501

        :return: The email of this BodyProfesorPost.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this BodyProfesorPost.

        E-Mail del Profesor.  # noqa: E501

        :param email: The email of this BodyProfesorPost.
        :type email: str
        """

        self._email = email

    @property
    def id_carrera(self) -> int:
        """Gets the id_carrera of this BodyProfesorPost.

        Id de la tabla carreras, relacion con carrera en donde realiza funciones el profesor.  # noqa: E501

        :return: The id_carrera of this BodyProfesorPost.
        :rtype: int
        """
        return self._id_carrera

    @id_carrera.setter
    def id_carrera(self, id_carrera: int):
        """Sets the id_carrera of this BodyProfesorPost.

        Id de la tabla carreras, relacion con carrera en donde realiza funciones el profesor.  # noqa: E501

        :param id_carrera: The id_carrera of this BodyProfesorPost.
        :type id_carrera: int
        """

        self._id_carrera = id_carrera
