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

class CosResourceConfigurationApiV1(WatsonService):
    """The COS Resource Configuration API V1 service."""

    default_url = 'https://config.cloud-object-storage.cloud.ibm.com/v1'

    def __init__(self,
                 url=default_url,
                 iam_apikey=None,
                 iam_access_token=None,
                 iam_url=None,
                ):
        """
        Construct a new client for the COS Resource Configuration API service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://config.cloud-object-storage.cloud.ibm.com/v1").
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
                                     use_vcap_services=True)

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

        url = '/b/{0}'.format(*self._encode_path_vars(bucket))
        response = self.request(method='GET',
                                url=url,
                                headers=headers,
                                accept_json=True)
        return response


    def update_bucket_config(self, bucket, firewall=None, **kwargs):
        """
        Updates a bucket's metadata. Only updates specified mutable fields.

        Updates a bucket using [JSON Merge Patch](https://tools.ietf.org/html/rfc7396).
        Only updates specified mutable fields.

        :param str bucket: Name of a bucket.
        :param FirewallFirewall firewall: Container for firewall information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if bucket is None:
            raise ValueError('bucket must be provided')
        if firewall is not None:
            firewall = self._convert_model(firewall, FirewallFirewall)

        headers = {
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

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

    :attr str name: (optional) The name of the bucket.
    :attr str crn: (optional) The service instance that holds the bucket.
    :attr str service_instance_id: (optional) The service instance that holds the bucket.
    :attr str service_instance_crn: (optional) The service instance that holds the bucket.
    :attr datetime time_created: (optional) The creation time of the bucket in RFC 3339
    format.
    :attr datetime last_updated: (optional) The modification time of the bucket in RFC
    3339 format.
    :attr str object_count: (optional) Total number of objects in the bucket.
    :attr str bytes_used: (optional) Total size of all objects in the bucket.
    :attr BucketFirewall firewall: (optional) List of allowed IP addresses for a bucket.
    """

    def __init__(self, name=None, crn=None, service_instance_id=None, service_instance_crn=None, time_created=None, last_updated=None, object_count=None, bytes_used=None, firewall=None):
        """
        Initialize a Bucket object.

        :param str name: (optional) The name of the bucket.
        :param str crn: (optional) The service instance that holds the bucket.
        :param str service_instance_id: (optional) The service instance that holds the
        bucket.
        :param str service_instance_crn: (optional) The service instance that holds the
        bucket.
        :param datetime time_created: (optional) The creation time of the bucket in RFC
        3339 format.
        :param datetime last_updated: (optional) The modification time of the bucket in
        RFC 3339 format.
        :param str object_count: (optional) Total number of objects in the bucket.
        :param str bytes_used: (optional) Total size of all objects in the bucket.
        :param BucketFirewall firewall: (optional) List of allowed IP addresses for a
        bucket.
        """
        self.name = name
        self.crn = crn
        self.service_instance_id = service_instance_id
        self.service_instance_crn = service_instance_crn
        self.time_created = time_created
        self.last_updated = last_updated
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
        if 'last_updated' in _dict:
            args['last_updated'] = string_to_datetime(_dict.get('last_updated'))
        if 'object_count' in _dict:
            args['object_count'] = _dict.get('object_count')
        if 'bytes_used' in _dict:
            args['bytes_used'] = _dict.get('bytes_used')
        if 'firewall' in _dict:
            args['firewall'] = BucketFirewall._from_dict(_dict.get('firewall'))
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
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = datetime_to_string(self.last_updated)
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


class BucketFirewall(object):
    """
    List of allowed IP addresses for a bucket.

    :attr list[str] allowed_ip: (optional) List of IP addresses to be affected by firewall
    in CIDR format.
    """

    def __init__(self, allowed_ip=None):
        """
        Initialize a BucketFirewall object.

        :param list[str] allowed_ip: (optional) List of IP addresses to be affected by
        firewall in CIDR format.
        """
        self.allowed_ip = allowed_ip

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BucketFirewall object from a json dictionary."""
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
        """Return a `str` version of this BucketFirewall object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FirewallFirewall(object):
    """
    Container for firewall information.

    :attr list[str] allowed_ip: (optional) List of IP addresses to be affected by firewall
    in CIDR format.
    """

    def __init__(self, allowed_ip=None):
        """
        Initialize a FirewallFirewall object.

        :param list[str] allowed_ip: (optional) List of IP addresses to be affected by
        firewall in CIDR format.
        """
        self.allowed_ip = allowed_ip

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallFirewall object from a json dictionary."""
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
        """Return a `str` version of this FirewallFirewall object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


