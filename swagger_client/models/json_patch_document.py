# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JsonPatchDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, op=None, path=None, value=None, _from=None):
        """
        JsonPatchDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op': 'str',
            'path': 'str',
            'value': 'object',
            '_from': 'str'
        }

        self.attribute_map = {
            'op': 'op',
            'path': 'path',
            'value': 'value',
            '_from': 'from'
        }

        self._op = op
        self._path = path
        self._value = value
        self.__from = _from

    @property
    def op(self):
        """
        Gets the op of this JsonPatchDocument.
        The operation to be performed

        :return: The op of this JsonPatchDocument.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this JsonPatchDocument.
        The operation to be performed

        :param op: The op of this JsonPatchDocument.
        :type: str
        """
        allowed_values = ["add", "remove", "replace", "move", "copy", "test"]
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def path(self):
        """
        Gets the path of this JsonPatchDocument.
        Path of the value to operate on

        :return: The path of this JsonPatchDocument.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this JsonPatchDocument.
        Path of the value to operate on

        :param path: The path of this JsonPatchDocument.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def value(self):
        """
        Gets the value of this JsonPatchDocument.
        The value for the operation.

        :return: The value of this JsonPatchDocument.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this JsonPatchDocument.
        The value for the operation.

        :param value: The value of this JsonPatchDocument.
        :type: object
        """

        self._value = value

    @property
    def _from(self):
        """
        Gets the _from of this JsonPatchDocument.

        :return: The _from of this JsonPatchDocument.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this JsonPatchDocument.

        :param _from: The _from of this JsonPatchDocument.
        :type: str
        """

        self.__from = _from

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, JsonPatchDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other