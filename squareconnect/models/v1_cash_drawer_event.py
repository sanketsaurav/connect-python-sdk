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


class V1CashDrawerEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, employee_id=None, event_type=None, event_money=None, created_at=None, description=None):
        """
        V1CashDrawerEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'employee_id': 'str',
            'event_type': 'str',
            'event_money': 'V1Money',
            'created_at': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'employee_id': 'employee_id',
            'event_type': 'event_type',
            'event_money': 'event_money',
            'created_at': 'created_at',
            'description': 'description'
        }

        self._id = id
        self._employee_id = employee_id
        self._event_type = event_type
        self._event_money = event_money
        self._created_at = created_at
        self._description = description

    @property
    def id(self):
        """
        Gets the id of this V1CashDrawerEvent.
        The event's unique ID.

        :return: The id of this V1CashDrawerEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1CashDrawerEvent.
        The event's unique ID.

        :param id: The id of this V1CashDrawerEvent.
        :type: str
        """

        self._id = id

    @property
    def employee_id(self):
        """
        Gets the employee_id of this V1CashDrawerEvent.
        The ID of the employee that created the event.

        :return: The employee_id of this V1CashDrawerEvent.
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """
        Sets the employee_id of this V1CashDrawerEvent.
        The ID of the employee that created the event.

        :param employee_id: The employee_id of this V1CashDrawerEvent.
        :type: str
        """

        self._employee_id = employee_id

    @property
    def event_type(self):
        """
        Gets the event_type of this V1CashDrawerEvent.
        The type of event that occurred. See [V1CashDrawerEventEventType](#type-v1cashdrawereventeventtype) for possible values

        :return: The event_type of this V1CashDrawerEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this V1CashDrawerEvent.
        The type of event that occurred. See [V1CashDrawerEventEventType](#type-v1cashdrawereventeventtype) for possible values

        :param event_type: The event_type of this V1CashDrawerEvent.
        :type: str
        """

        self._event_type = event_type

    @property
    def event_money(self):
        """
        Gets the event_money of this V1CashDrawerEvent.
        The amount of money that was added to or removed from the cash drawer because of the event. This value can be positive (for added money) or negative (for removed money).

        :return: The event_money of this V1CashDrawerEvent.
        :rtype: V1Money
        """
        return self._event_money

    @event_money.setter
    def event_money(self, event_money):
        """
        Sets the event_money of this V1CashDrawerEvent.
        The amount of money that was added to or removed from the cash drawer because of the event. This value can be positive (for added money) or negative (for removed money).

        :param event_money: The event_money of this V1CashDrawerEvent.
        :type: V1Money
        """

        self._event_money = event_money

    @property
    def created_at(self):
        """
        Gets the created_at of this V1CashDrawerEvent.
        The time when the event occurred, in ISO 8601 format.

        :return: The created_at of this V1CashDrawerEvent.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this V1CashDrawerEvent.
        The time when the event occurred, in ISO 8601 format.

        :param created_at: The created_at of this V1CashDrawerEvent.
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this V1CashDrawerEvent.
        An optional description of the event, entered by the employee that created it.

        :return: The description of this V1CashDrawerEvent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1CashDrawerEvent.
        An optional description of the event, entered by the employee that created it.

        :param description: The description of this V1CashDrawerEvent.
        :type: str
        """

        self._description = description

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
