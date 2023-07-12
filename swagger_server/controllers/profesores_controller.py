import connexion
import six

from swagger_server.models.body_profesor_post import BodyProfesorPost  # noqa: E501
from swagger_server.models.exito_profesor_get import ExitoProfesorGet  # noqa: E501
from swagger_server.models.exito_profesor_modificar import ExitoProfesorModificar  # noqa: E501
from swagger_server import util


def borrarprofesor_id_delete(id):  # noqa: E501
    """Elimina un profesor existente

     # noqa: E501

    :param id: ID del profesor a eliminar
    :type id: float

    :rtype: ExitoProfesorModificar
    """
    return 'do some magic!'


def guardar_profesor(body):  # noqa: E501
    """Agrega un Profesor a la base de datos.

    Peticion de tipo POST al EndPoint, para agregar un profesor a la base de Datos. # noqa: E501

    :param body: Agregar Profesor.
    :type body: dict | bytes

    :rtype: BodyProfesorPost
    """
    if connexion.request.is_json:
        body = BodyProfesorPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def listas_profesores():  # noqa: E501
    """Consulta a la base de datos todos los profesores existentes en ella.

    Peticion del cliente a la api para obtener todos los clientes en la base de datos. # noqa: E501


    :rtype: ExitoProfesorGet
    """
    return 'do some magic!'


def modificarprofesor_id_put(body, id):  # noqa: E501
    """Modificar un profesor existente

     # noqa: E501

    :param body: Agregar Profesor.
    :type body: dict | bytes
    :param id: ID del profesor a modificar
    :type id: float

    :rtype: ExitoProfesorModificar
    """
    if connexion.request.is_json:
        body = BodyProfesorPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
