# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
REST API used to configure Cloud Object Storage buckets.  This version of the API only
supports reading bucket metadata and setting IP access controls.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################

class ResourceConfigurationV1(WatsonService):
    """The ResourceConfiguration V1 service."""

    default_url = 'https://config.cloud-object-storage.cloud.ibm.com/v1'

    def __init__(self,
                 url=default_url,
                 iam_apikey=None,
                 iam_access_token=None,
                 iam_url=None,
                ):
        """
        Construct a new client for the ResourceConfiguration service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://config.cloud-object-storage.cloud.ibm.com/v1/v1").
               The base url may differ between Bluemix regions.

        :param str iam_apikey: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.bluemix.net/identity/token'.
        """

        WatsonService.__init__(self,
                                     vcap_services_name='',
                                     url=url,
                                     iam_apikey=iam_apikey,
                                     iam_access_token=iam_access_token,
                                     iam_url=iam_url,
                                     use_vcap_services=True,
                                     display_name='ResourceConfiguration')

    #########################
    # buckets
    #########################

    def get_bucket_config(self, bucket, **kwargs):
        """
        Returns metadata for the specified bucket.

        Returns metadata for the specified bucket.

        :param str bucket: Name of a bucket.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if bucket is None:
            raise ValueError('bucket must be provided')

        headers = {
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['X-IBMCloud-SDK-Analytics'] = 'service_name=;service_version=V1;operation_id=get_bucket_config'

        url = '/b/{0}'.format(*self._encode_path_vars(bucket))
        response = self.request(method='GET',
                                url=url,
                                headers=headers,
                                accept_json=True)
        return response


    def update_bucket_config(self, bucket, firewall=None, if_match=None, **kwargs):
        """
        Make changes to a bucket's configuration.

        Updates a bucket using [JSON Merge Patch](https://tools.ietf.org/html/rfc7396).
        This request is used to add functionality (like an IP access filter) or to update
        existing parameters.  **Primitives are overwritten and replaced in their entirety.
        It is not possible to append a new (or to delete a specific) value to an array.**
        Arrays can be cleared by updating the parameter with an empty array `[]`. Only
        updates specified mutable fields. Please don't use `PATCH` trying to update the
        number of objects in a bucket, any timestamps, or other non-mutable fields.

        :param str bucket: Name of a bucket.
        :param Firewall firewall: A filter that controls access based on the network where
        request originated. Requests not originating from IP addresses listed in the
        `allowed_ip` field will be denied.  Viewing or updating the `Firewall` element
        requires the requester to have the `manager` role.
        :param str if_match: An Etag previously returned in a header when fetching or
        updating a bucket's metadata. If this value does not match the active Etag, the
        request will fail.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if bucket is None:
            raise ValueError('bucket must be provided')
        if firewall is not None:
            firewall = self._convert_model(firewall, Firewall)

        headers = {
            'if-match': if_match
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['X-IBMCloud-SDK-Analytics'] = 'service_name=;service_version=V1;operation_id=update_bucket_config'

        data = {
            'firewall': firewall
        }

        url = '/b/{0}'.format(*self._encode_path_vars(bucket))
        response = self.request(method='PATCH',
                                url=url,
                                headers=headers,
                                json=data,
                                accept_json=True)
        return response



##############################################################################
# Models
##############################################################################


class Bucket(object):
    """
    A bucket.

    :attr str name: (optional) The name of the bucket. Non-mutable.
    :attr str crn: (optional) The service instance that holds the bucket. Non-mutable.
    :attr str service_instance_id: (optional) The service instance that holds the bucket.
    Non-mutable.
    :attr str service_instance_crn: (optional) The service instance that holds the bucket.
    Non-mutable.
    :attr datetime time_created: (optional) The creation time of the bucket in RFC 3339
    format. Non-mutable.
    :attr datetime time_updated: (optional) The modification time of the bucket in RFC
    3339 format. Non-mutable.
    :attr int object_count: (optional) Total number of objects in the bucket. Non-mutable.
    :attr int bytes_used: (optional) Total size of all objects in the bucket. Non-mutable.
    :attr Firewall firewall: (optional) A filter that controls access based on the network
    where request originated. Requests not originating from IP addresses listed in the
    `allowed_ip` field will be denied.  Viewing or updating the `Firewall` element
    requires the requester to have the `manager` role.
    """

    def __init__(self, name=None, crn=None, service_instance_id=None, service_instance_crn=None, time_created=None, time_updated=None, object_count=None, bytes_used=None, firewall=None):
        """
        Initialize a Bucket object.

        :param str name: (optional) The name of the bucket. Non-mutable.
        :param str crn: (optional) The service instance that holds the bucket.
        Non-mutable.
        :param str service_instance_id: (optional) The service instance that holds the
        bucket. Non-mutable.
        :param str service_instance_crn: (optional) The service instance that holds the
        bucket. Non-mutable.
        :param datetime time_created: (optional) The creation time of the bucket in RFC
        3339 format. Non-mutable.
        :param datetime time_updated: (optional) The modification time of the bucket in
        RFC 3339 format. Non-mutable.
        :param int object_count: (optional) Total number of objects in the bucket.
        Non-mutable.
        :param int bytes_used: (optional) Total size of all objects in the bucket.
        Non-mutable.
        :param Firewall firewall: (optional) A filter that controls access based on the
        network where request originated. Requests not originating from IP addresses
        listed in the `allowed_ip` field will be denied.  Viewing or updating the
        `Firewall` element requires the requester to have the `manager` role.
        """
        self.name = name
        self.crn = crn
        self.service_instance_id = service_instance_id
        self.service_instance_crn = service_instance_crn
        self.time_created = time_created
        self.time_updated = time_updated
        self.object_count = object_count
        self.bytes_used = bytes_used
        self.firewall = firewall

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Bucket object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        if 'service_instance_crn' in _dict:
            args['service_instance_crn'] = _dict.get('service_instance_crn')
        if 'time_created' in _dict:
            args['time_created'] = string_to_datetime(_dict.get('time_created'))
        if 'time_updated' in _dict:
            args['time_updated'] = string_to_datetime(_dict.get('time_updated'))
        if 'object_count' in _dict:
            args['object_count'] = _dict.get('object_count')
        if 'bytes_used' in _dict:
            args['bytes_used'] = _dict.get('bytes_used')
        if 'firewall' in _dict:
            args['firewall'] = Firewall._from_dict(_dict.get('firewall'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
        if hasattr(self, 'service_instance_crn') and self.service_instance_crn is not None:
            _dict['service_instance_crn'] = self.service_instance_crn
        if hasattr(self, 'time_created') and self.time_created is not None:
            _dict['time_created'] = datetime_to_string(self.time_created)
        if hasattr(self, 'time_updated') and self.time_updated is not None:
            _dict['time_updated'] = datetime_to_string(self.time_updated)
        if hasattr(self, 'object_count') and self.object_count is not None:
            _dict['object_count'] = self.object_count
        if hasattr(self, 'bytes_used') and self.bytes_used is not None:
            _dict['bytes_used'] = self.bytes_used
        if hasattr(self, 'firewall') and self.firewall is not None:
            _dict['firewall'] = self.firewall._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Bucket object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Firewall(object):
    """
    A filter that controls access based on the network where request originated. Requests
    not originating from IP addresses listed in the `allowed_ip` field will be denied.
    Viewing or updating the `Firewall` element requires the requester to have the
    `manager` role.

    :attr list[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR notation
    to be affected by firewall in CIDR notation is supported. Passing an empty array will
    lift the IP address filter.  The `allowed_ip` array can contain a maximum of 1000
    items.
    """

    def __init__(self, allowed_ip=None):
        """
        Initialize a Firewall object.

        :param list[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
        notation to be affected by firewall in CIDR notation is supported. Passing an
        empty array will lift the IP address filter.  The `allowed_ip` array can contain a
        maximum of 1000 items.
        """
        self.allowed_ip = allowed_ip

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Firewall object from a json dictionary."""
        args = {}
        if 'allowed_ip' in _dict:
            args['allowed_ip'] = _dict.get('allowed_ip')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allowed_ip') and self.allowed_ip is not None:
            _dict['allowed_ip'] = self.allowed_ip
        return _dict

    def __str__(self):
        """Return a `str` version of this Firewall object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


