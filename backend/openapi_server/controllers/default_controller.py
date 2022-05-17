import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.get_health_response import GetHealthResponse  # noqa: E501
from openapi_server import util


def health_check():  # noqa: E501
    """Return server status

     # noqa: E501


    :rtype: GetHealthResponse
    """
    return 'do some magic!'
