import connexion
import six

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_employee import NewEmployee  # noqa: E501
from openapi_server import util


def create_employee(new_employee=None):  # noqa: E501
    """Create a employee

     # noqa: E501

    :param new_employee: 
    :type new_employee: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        new_employee = NewEmployee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_employee(employee_id):  # noqa: E501
    """Delete a employee

     # noqa: E501

    :param employee_id: The id of the employee to retrieve
    :type employee_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_employee_by_id(employee_id):  # noqa: E501
    """Get employee by id

     # noqa: E501

    :param employee_id: The id of the employee to get
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def list_employees():  # noqa: E501
    """List employees

     # noqa: E501


    :rtype: List[Employee]
    """
    return 'do some magic!'


def update_employee(employee_id, new_employee=None):  # noqa: E501
    """Update a employee

     # noqa: E501

    :param employee_id: The id of the employee to retrieve
    :type employee_id: str
    :param new_employee: 
    :type new_employee: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        new_employee = NewEmployee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
