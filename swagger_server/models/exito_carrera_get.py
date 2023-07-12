# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ExitoCarreraGet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id_carrera: int=None, carrera: str=None):  # noqa: E501
        """ExitoCarreraGet - a model defined in Swagger

        :param id_carrera: The id_carrera of this ExitoCarreraGet.  # noqa: E501
        :type id_carrera: int
        :param carrera: The carrera of this ExitoCarreraGet.  # noqa: E501
        :type carrera: str
        """
        self.swagger_types = {
            'id_carrera': int,
            'carrera': str
        }

        self.attribute_map = {
            'id_carrera': 'id_carrera',
            'carrera': 'carrera'
        }
        self._id_carrera = id_carrera
        self._carrera = carrera

    @classmethod
    def from_dict(cls, dikt) -> 'ExitoCarreraGet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExitoCarreraGet of this ExitoCarreraGet.  # noqa: E501
        :rtype: ExitoCarreraGet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_carrera(self) -> int:
        """Gets the id_carrera of this ExitoCarreraGet.

        ID  que le corresponde a la Carrera, auto-icrementado  # noqa: E501

        :return: The id_carrera of this ExitoCarreraGet.
        :rtype: int
        """
        return self._id_carrera

    @id_carrera.setter
    def id_carrera(self, id_carrera: int):
        """Sets the id_carrera of this ExitoCarreraGet.

        ID  que le corresponde a la Carrera, auto-icrementado  # noqa: E501

        :param id_carrera: The id_carrera of this ExitoCarreraGet.
        :type id_carrera: int
        """
        allowed_values = ["1"]  # noqa: E501
        if id_carrera not in allowed_values:
            raise ValueError(
                "Invalid value for `id_carrera` ({0}), must be one of {1}"
                .format(id_carrera, allowed_values)
            )

        self._id_carrera = id_carrera

    @property
    def carrera(self) -> str:
        """Gets the carrera of this ExitoCarreraGet.

        Nombre de la carrera  # noqa: E501

        :return: The carrera of this ExitoCarreraGet.
        :rtype: str
        """
        return self._carrera

    @carrera.setter
    def carrera(self, carrera: str):
        """Sets the carrera of this ExitoCarreraGet.

        Nombre de la carrera  # noqa: E501

        :param carrera: The carrera of this ExitoCarreraGet.
        :type carrera: str
        """
        allowed_values = ["nombre"]  # noqa: E501
        if carrera not in allowed_values:
            raise ValueError(
                "Invalid value for `carrera` ({0}), must be one of {1}"
                .format(carrera, allowed_values)
            )

        self._carrera = carrera
