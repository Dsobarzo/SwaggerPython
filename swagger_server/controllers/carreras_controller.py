import connexion
import six

from swagger_server.models.exito_carrera_get import ExitoCarreraGet  # noqa: E501
from swagger_server import util


def listas_carreras():  # noqa: E501
    """Consulta a la base de datos todas las Carreras existentes en ella.

    Peticion del cliente a la api para obtener todas las Carreras en la base de datos. # noqa: E501


    :rtype: ExitoCarreraGet
    """
    return 'do some magic!'
