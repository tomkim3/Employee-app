# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Employee(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, attr=None):  # noqa: E501
        """Employee - a model defined in OpenAPI

        :param id: The id of this Employee.  # noqa: E501
        :type id: str
        :param name: The name of this Employee.  # noqa: E501
        :type name: str
        :param attr: The attr of this Employee.  # noqa: E501
        :type attr: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'attr': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'attr': 'attr'
        }

        self._id = id
        self._name = name
        self._attr = attr

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Employee.


        :return: The id of this Employee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Employee.


        :param id: The id of this Employee.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Employee.


        :return: The name of this Employee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Employee.


        :param name: The name of this Employee.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def attr(self):
        """Gets the attr of this Employee.


        :return: The attr of this Employee.
        :rtype: str
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this Employee.


        :param attr: The attr of this Employee.
        :type attr: str
        """

        self._attr = attr
