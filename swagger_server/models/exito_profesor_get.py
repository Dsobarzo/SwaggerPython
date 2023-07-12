# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ExitoProfesorGet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id_profesor: int=None, nombre: str=None, apellido: str=None, email: str=None, id_carrera: int=None):  # noqa: E501
        """ExitoProfesorGet - a model defined in Swagger

        :param id_profesor: The id_profesor of this ExitoProfesorGet.  # noqa: E501
        :type id_profesor: int
        :param nombre: The nombre of this ExitoProfesorGet.  # noqa: E501
        :type nombre: str
        :param apellido: The apellido of this ExitoProfesorGet.  # noqa: E501
        :type apellido: str
        :param email: The email of this ExitoProfesorGet.  # noqa: E501
        :type email: str
        :param id_carrera: The id_carrera of this ExitoProfesorGet.  # noqa: E501
        :type id_carrera: int
        """
        self.swagger_types = {
            'id_profesor': int,
            'nombre': str,
            'apellido': str,
            'email': str,
            'id_carrera': int
        }

        self.attribute_map = {
            'id_profesor': 'id_profesor',
            'nombre': 'nombre',
            'apellido': 'apellido',
            'email': 'email',
            'id_carrera': 'id_carrera'
        }
        self._id_profesor = id_profesor
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._id_carrera = id_carrera

    @classmethod
    def from_dict(cls, dikt) -> 'ExitoProfesorGet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExitoProfesorGet of this ExitoProfesorGet.  # noqa: E501
        :rtype: ExitoProfesorGet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_profesor(self) -> int:
        """Gets the id_profesor of this ExitoProfesorGet.

        ID  que le corresponde al profesor, auto-icrementado  # noqa: E501

        :return: The id_profesor of this ExitoProfesorGet.
        :rtype: int
        """
        return self._id_profesor

    @id_profesor.setter
    def id_profesor(self, id_profesor: int):
        """Sets the id_profesor of this ExitoProfesorGet.

        ID  que le corresponde al profesor, auto-icrementado  # noqa: E501

        :param id_profesor: The id_profesor of this ExitoProfesorGet.
        :type id_profesor: int
        """
        allowed_values = ["1"]  # noqa: E501
        if id_profesor not in allowed_values:
            raise ValueError(
                "Invalid value for `id_profesor` ({0}), must be one of {1}"
                .format(id_profesor, allowed_values)
            )

        self._id_profesor = id_profesor

    @property
    def nombre(self) -> str:
        """Gets the nombre of this ExitoProfesorGet.

        Primer nombre del profesor  # noqa: E501

        :return: The nombre of this ExitoProfesorGet.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this ExitoProfesorGet.

        Primer nombre del profesor  # noqa: E501

        :param nombre: The nombre of this ExitoProfesorGet.
        :type nombre: str
        """
        allowed_values = ["nombre"]  # noqa: E501
        if nombre not in allowed_values:
            raise ValueError(
                "Invalid value for `nombre` ({0}), must be one of {1}"
                .format(nombre, allowed_values)
            )

        self._nombre = nombre

    @property
    def apellido(self) -> str:
        """Gets the apellido of this ExitoProfesorGet.

        Primer apellido del profesor  # noqa: E501

        :return: The apellido of this ExitoProfesorGet.
        :rtype: str
        """
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        """Sets the apellido of this ExitoProfesorGet.

        Primer apellido del profesor  # noqa: E501

        :param apellido: The apellido of this ExitoProfesorGet.
        :type apellido: str
        """
        allowed_values = ["apellido"]  # noqa: E501
        if apellido not in allowed_values:
            raise ValueError(
                "Invalid value for `apellido` ({0}), must be one of {1}"
                .format(apellido, allowed_values)
            )

        self._apellido = apellido

    @property
    def email(self) -> str:
        """Gets the email of this ExitoProfesorGet.

        E-Mail del Profesor  # noqa: E501

        :return: The email of this ExitoProfesorGet.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ExitoProfesorGet.

        E-Mail del Profesor  # noqa: E501

        :param email: The email of this ExitoProfesorGet.
        :type email: str
        """
        allowed_values = ["email"]  # noqa: E501
        if email not in allowed_values:
            raise ValueError(
                "Invalid value for `email` ({0}), must be one of {1}"
                .format(email, allowed_values)
            )

        self._email = email

    @property
    def id_carrera(self) -> int:
        """Gets the id_carrera of this ExitoProfesorGet.

        Id de la tabla carreras, relacion con carrera en donde realiza funciones el profesor.  # noqa: E501

        :return: The id_carrera of this ExitoProfesorGet.
        :rtype: int
        """
        return self._id_carrera

    @id_carrera.setter
    def id_carrera(self, id_carrera: int):
        """Sets the id_carrera of this ExitoProfesorGet.

        Id de la tabla carreras, relacion con carrera en donde realiza funciones el profesor.  # noqa: E501

        :param id_carrera: The id_carrera of this ExitoProfesorGet.
        :type id_carrera: int
        """
        allowed_values = ["1"]  # noqa: E501
        if id_carrera not in allowed_values:
            raise ValueError(
                "Invalid value for `id_carrera` ({0}), must be one of {1}"
                .format(id_carrera, allowed_values)
            )

        self._id_carrera = id_carrera
