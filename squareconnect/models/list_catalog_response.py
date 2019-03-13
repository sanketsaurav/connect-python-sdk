# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class ListCatalogResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, cursor=None, objects=None):
        """
        ListCatalogResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[Error]',
            'cursor': 'str',
            'objects': 'list[CatalogObject]'
        }

        self.attribute_map = {
            'errors': 'errors',
            'cursor': 'cursor',
            'objects': 'objects'
        }

        self._errors = errors
        self._cursor = cursor
        self._objects = objects

    @property
    def errors(self):
        """
        Gets the errors of this ListCatalogResponse.
        The set of [Error](#type-error)s encountered.

        :return: The errors of this ListCatalogResponse.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ListCatalogResponse.
        The set of [Error](#type-error)s encountered.

        :param errors: The errors of this ListCatalogResponse.
        :type: list[Error]
        """

        self._errors = errors

    @property
    def cursor(self):
        """
        Gets the cursor of this ListCatalogResponse.
        The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Pagination](/basics/api101/pagination) for more information.

        :return: The cursor of this ListCatalogResponse.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this ListCatalogResponse.
        The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Pagination](/basics/api101/pagination) for more information.

        :param cursor: The cursor of this ListCatalogResponse.
        :type: str
        """

        self._cursor = cursor

    @property
    def objects(self):
        """
        Gets the objects of this ListCatalogResponse.
        The [CatalogObject](#type-catalogobject)s returned.

        :return: The objects of this ListCatalogResponse.
        :rtype: list[CatalogObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this ListCatalogResponse.
        The [CatalogObject](#type-catalogobject)s returned.

        :param objects: The objects of this ListCatalogResponse.
        :type: list[CatalogObject]
        """

        self._objects = objects

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
