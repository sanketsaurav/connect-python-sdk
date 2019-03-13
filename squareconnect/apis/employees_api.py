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


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class EmployeesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_employees(self, **kwargs):
        """
        ListEmployees
        Gets a list of `Employee` objects for a business.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_employees(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str location_id: Filter employees returned to only those that are associated with the specified location.
        :param str status: Specifies the EmployeeStatus to filter the employee by.
        :param int limit: The number of employees to be returned on each page.
        :param str cursor: The token required to retrieve the specified page of results.
        :return: ListEmployeesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'status', 'limit', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_employees" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/v2/employees'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'location_id' in params and params['location_id'] is not None:
            query_params['location_id'] = params['location_id']
        if 'status' in params and params['status'] is not None:
            query_params['status'] = params['status']
        if 'limit' in params and params['limit'] is not None:
            query_params['limit'] = params['limit']
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}
        header_params['Square-Version'] = "2019-03-13"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListEmployeesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_employee(self, id, **kwargs):
        """
        RetrieveEmployee
        Gets an `Employee` by Square-assigned employee `ID` (UUID)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_employee(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: UUID for the employee that was requested. (required)
        :return: RetrieveEmployeeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_employee" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve_employee`")


        resource_path = '/v2/employees/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-03-13"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveEmployeeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        
