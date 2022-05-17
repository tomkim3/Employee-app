# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_employee import NewEmployee  # noqa: E501
from openapi_server.test import BaseTestCase


class TestEmployeesController(BaseTestCase):
    """EmployeesController integration test stubs"""

    def test_create_employee(self):
        """Test case for create_employee

        Create a employee
        """
        new_employee = {
  "name" : "name",
  "attr" : "attr"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/employees',
            method='POST',
            headers=headers,
            data=json.dumps(new_employee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_employee(self):
        """Test case for delete_employee

        Delete a employee
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/employees/{employee_id}'.format(employee_id='employee_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_employees(self):
        """Test case for list_employees

        List employees
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/employees',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_employee(self):
        """Test case for update_employee

        Update a employee
        """
        new_employee = {
  "name" : "name",
  "attr" : "attr"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/employees/{employee_id}'.format(employee_id='employee_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(new_employee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
