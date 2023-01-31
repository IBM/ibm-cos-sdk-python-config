# coding: utf-8

# (C) Copyright IBM Corp. 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.64.1-cee95189-20230124-211647

"""
REST API used to configure Cloud Object Storage buckets.  This version of the API only
supports reading bucket metadata, setting IP access controls, and configuring logging and
monitoring services.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ResourceConfigurationV1(BaseService):
    """The ResourceConfiguration V1 service."""

    DEFAULT_SERVICE_URL = 'https://config.cloud-object-storage.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'resource_configuration'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ResourceConfigurationV1':
        """
        Return a new client for the ResourceConfiguration service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the ResourceConfiguration service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # buckets
    #########################


    def get_bucket_config(self,
        bucket: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Returns metadata for the specified bucket.

        Returns metadata for the specified bucket.

        :param str bucket: Name of a bucket.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Bucket` object
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_bucket_config')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket']
        path_param_values = self.encode_path_vars(bucket)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/b/{bucket}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_bucket_config(self,
        bucket: str,
        *,
        bucket_patch: 'BucketPatch' = None,
        if_match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Make changes to a bucket's configuration.

        Updates a bucket using [JSON Merge Patch](https://tools.ietf.org/html/rfc7396).
        This request is used to add functionality (like an IP access filter) or to update
        existing parameters.  **Primitives are overwritten and replaced in their entirety.
        It is not possible to append a new (or to delete a specific) value to an array.**
        Arrays can be cleared by updating the parameter with an empty array `[]`. A
        `PATCH` operation only updates specified mutable fields. Please don't use `PATCH`
        trying to update the number of objects in a bucket, any timestamps, or other
        non-mutable fields.

        :param str bucket: Name of a bucket.
        :param BucketPatch bucket_patch: (optional) An object containing new
               configuration metadata.
        :param str if_match: (optional) An Etag previously returned in a header
               when fetching or updating a bucket's metadata. If this value does not match
               the active Etag, the request will fail.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        if  bucket_patch is not None and isinstance(bucket_patch, BucketPatch):
            bucket_patch = convert_model(bucket_patch)
        headers = {
            'if-match': if_match,
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_bucket_config')
        headers.update(sdk_headers)

        data = json.dumps(bucket_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['bucket']
        path_param_values = self.encode_path_vars(bucket)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/b/{bucket}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ActivityTracking():
    """
    Enables sending log data to IBM Cloud Activity Tracker to provide visibility into
    object read and write events. All object events are sent to the activity tracker
    instance defined in the `activity_tracker_crn` field.

    :attr bool read_data_events: (optional) If set to `true`, all object read events
          (i.e. downloads) will be sent to Activity Tracker.
    :attr bool write_data_events: (optional) If set to `true`, all object write
          events (i.e. uploads) will be sent to Activity Tracker.
    :attr str activity_tracker_crn: (optional) Required the first time
          `activity_tracking` is configured. The instance of Activity Tracker that will
          receive object event data. The format is "crn:v1:bluemix:public:logdnaat:{bucket
          location}:a/{storage account}:{activity tracker service instance}::".
    """

    def __init__(self,
                 *,
                 read_data_events: bool = None,
                 write_data_events: bool = None,
                 activity_tracker_crn: str = None) -> None:
        """
        Initialize a ActivityTracking object.

        :param bool read_data_events: (optional) If set to `true`, all object read
               events (i.e. downloads) will be sent to Activity Tracker.
        :param bool write_data_events: (optional) If set to `true`, all object
               write events (i.e. uploads) will be sent to Activity Tracker.
        :param str activity_tracker_crn: (optional) Required the first time
               `activity_tracking` is configured. The instance of Activity Tracker that
               will receive object event data. The format is
               "crn:v1:bluemix:public:logdnaat:{bucket location}:a/{storage
               account}:{activity tracker service instance}::".
        """
        self.read_data_events = read_data_events
        self.write_data_events = write_data_events
        self.activity_tracker_crn = activity_tracker_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActivityTracking':
        """Initialize a ActivityTracking object from a json dictionary."""
        args = {}
        if 'read_data_events' in _dict:
            args['read_data_events'] = _dict.get('read_data_events')
        if 'write_data_events' in _dict:
            args['write_data_events'] = _dict.get('write_data_events')
        if 'activity_tracker_crn' in _dict:
            args['activity_tracker_crn'] = _dict.get('activity_tracker_crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActivityTracking object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'read_data_events') and self.read_data_events is not None:
            _dict['read_data_events'] = self.read_data_events
        if hasattr(self, 'write_data_events') and self.write_data_events is not None:
            _dict['write_data_events'] = self.write_data_events
        if hasattr(self, 'activity_tracker_crn') and self.activity_tracker_crn is not None:
            _dict['activity_tracker_crn'] = self.activity_tracker_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActivityTracking object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActivityTracking') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActivityTracking') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Bucket():
    """
    A bucket.

    :attr str name: (optional) The name of the bucket. Non-mutable.
    :attr str crn: (optional) The service instance that holds the bucket.
          Non-mutable.
    :attr str service_instance_id: (optional) The service instance that holds the
          bucket. Non-mutable.
    :attr str service_instance_crn: (optional) The service instance that holds the
          bucket. Non-mutable.
    :attr datetime time_created: (optional) The creation time of the bucket in RFC
          3339 format. Non-mutable.
    :attr datetime time_updated: (optional) The modification time of the bucket in
          RFC 3339 format. Non-mutable.
    :attr int object_count: (optional) Total number of objects in the bucket.
          Non-mutable.
    :attr int bytes_used: (optional) Total size of all objects in the bucket.
          Non-mutable.
    :attr int noncurrent_object_count: (optional) Number of non-current object
          versions in the bucket. Non-mutable.
    :attr int noncurrent_bytes_used: (optional) Total size of all non-current object
          versions in the bucket. Non-mutable.
    :attr int delete_marker_count: (optional) Total number of delete markers in the
          bucket. Non-mutable.
    :attr Firewall firewall: (optional) An access control mechanism based on the
          network (IP address) where request originated. Requests not originating from IP
          addresses listed in the `allowed_ip` field will be denied regardless of any
          access policies (including public access) that might otherwise permit the
          request.  Viewing or updating the `Firewall` element requires the requester to
          have the `manager` role.
    :attr ActivityTracking activity_tracking: (optional) Enables sending log data to
          IBM Cloud Activity Tracker to provide visibility into object read and write
          events. All object events are sent to the activity tracker instance defined in
          the `activity_tracker_crn` field.
    :attr MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics
          to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud Monitoring
          instance defined in the `monitoring_crn` field.
    :attr int hard_quota: (optional) Maximum bytes for this bucket.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 crn: str = None,
                 service_instance_id: str = None,
                 service_instance_crn: str = None,
                 time_created: datetime = None,
                 time_updated: datetime = None,
                 object_count: int = None,
                 bytes_used: int = None,
                 noncurrent_object_count: int = None,
                 noncurrent_bytes_used: int = None,
                 delete_marker_count: int = None,
                 firewall: 'Firewall' = None,
                 activity_tracking: 'ActivityTracking' = None,
                 metrics_monitoring: 'MetricsMonitoring' = None,
                 hard_quota: int = None) -> None:
        """
        Initialize a Bucket object.

        :param str name: (optional) The name of the bucket. Non-mutable.
        :param str crn: (optional) The service instance that holds the bucket.
               Non-mutable.
        :param str service_instance_id: (optional) The service instance that holds
               the bucket. Non-mutable.
        :param str service_instance_crn: (optional) The service instance that holds
               the bucket. Non-mutable.
        :param datetime time_created: (optional) The creation time of the bucket in
               RFC 3339 format. Non-mutable.
        :param datetime time_updated: (optional) The modification time of the
               bucket in RFC 3339 format. Non-mutable.
        :param int object_count: (optional) Total number of objects in the bucket.
               Non-mutable.
        :param int bytes_used: (optional) Total size of all objects in the bucket.
               Non-mutable.
        :param int noncurrent_object_count: (optional) Number of non-current object
               versions in the bucket. Non-mutable.
        :param int noncurrent_bytes_used: (optional) Total size of all non-current
               object versions in the bucket. Non-mutable.
        :param int delete_marker_count: (optional) Total number of delete markers
               in the bucket. Non-mutable.
        :param Firewall firewall: (optional) An access control mechanism based on
               the network (IP address) where request originated. Requests not originating
               from IP addresses listed in the `allowed_ip` field will be denied
               regardless of any access policies (including public access) that might
               otherwise permit the request.  Viewing or updating the `Firewall` element
               requires the requester to have the `manager` role.
        :param ActivityTracking activity_tracking: (optional) Enables sending log
               data to IBM Cloud Activity Tracker to provide visibility into object read
               and write events. All object events are sent to the activity tracker
               instance defined in the `activity_tracker_crn` field.
        :param MetricsMonitoring metrics_monitoring: (optional) Enables sending
               metrics to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud
               Monitoring instance defined in the `monitoring_crn` field.
        :param int hard_quota: (optional) Maximum bytes for this bucket.
        """
        self.name = name
        self.crn = crn
        self.service_instance_id = service_instance_id
        self.service_instance_crn = service_instance_crn
        self.time_created = time_created
        self.time_updated = time_updated
        self.object_count = object_count
        self.bytes_used = bytes_used
        self.noncurrent_object_count = noncurrent_object_count
        self.noncurrent_bytes_used = noncurrent_bytes_used
        self.delete_marker_count = delete_marker_count
        self.firewall = firewall
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring
        self.hard_quota = hard_quota

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Bucket':
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
        if 'noncurrent_object_count' in _dict:
            args['noncurrent_object_count'] = _dict.get('noncurrent_object_count')
        if 'noncurrent_bytes_used' in _dict:
            args['noncurrent_bytes_used'] = _dict.get('noncurrent_bytes_used')
        if 'delete_marker_count' in _dict:
            args['delete_marker_count'] = _dict.get('delete_marker_count')
        if 'firewall' in _dict:
            args['firewall'] = Firewall.from_dict(_dict.get('firewall'))
        if 'activity_tracking' in _dict:
            args['activity_tracking'] = ActivityTracking.from_dict(_dict.get('activity_tracking'))
        if 'metrics_monitoring' in _dict:
            args['metrics_monitoring'] = MetricsMonitoring.from_dict(_dict.get('metrics_monitoring'))
        if 'hard_quota' in _dict:
            args['hard_quota'] = _dict.get('hard_quota')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Bucket object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
        if hasattr(self, 'noncurrent_object_count') and self.noncurrent_object_count is not None:
            _dict['noncurrent_object_count'] = self.noncurrent_object_count
        if hasattr(self, 'noncurrent_bytes_used') and self.noncurrent_bytes_used is not None:
            _dict['noncurrent_bytes_used'] = self.noncurrent_bytes_used
        if hasattr(self, 'delete_marker_count') and self.delete_marker_count is not None:
            _dict['delete_marker_count'] = self.delete_marker_count
        if hasattr(self, 'firewall') and self.firewall is not None:
            if isinstance(self.firewall, dict):
                _dict['firewall'] = self.firewall
            else:
                _dict['firewall'] = self.firewall.to_dict()
        if hasattr(self, 'activity_tracking') and self.activity_tracking is not None:
            if isinstance(self.activity_tracking, dict):
                _dict['activity_tracking'] = self.activity_tracking
            else:
                _dict['activity_tracking'] = self.activity_tracking.to_dict()
        if hasattr(self, 'metrics_monitoring') and self.metrics_monitoring is not None:
            if isinstance(self.metrics_monitoring, dict):
                _dict['metrics_monitoring'] = self.metrics_monitoring
            else:
                _dict['metrics_monitoring'] = self.metrics_monitoring.to_dict()
        if hasattr(self, 'hard_quota') and self.hard_quota is not None:
            _dict['hard_quota'] = self.hard_quota
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Bucket object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Bucket') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Bucket') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BucketPatch():
    """
    An object containing new bucket metadata.

    :attr Firewall firewall: (optional) An access control mechanism based on the
          network (IP address) where request originated. Requests not originating from IP
          addresses listed in the `allowed_ip` field will be denied regardless of any
          access policies (including public access) that might otherwise permit the
          request.  Viewing or updating the `Firewall` element requires the requester to
          have the `manager` role.
    :attr ActivityTracking activity_tracking: (optional) Enables sending log data to
          IBM Cloud Activity Tracker to provide visibility into object read and write
          events. All object events are sent to the activity tracker instance defined in
          the `activity_tracker_crn` field.
    :attr MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics
          to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud Monitoring
          instance defined in the `monitoring_crn` field.
    :attr int hard_quota: (optional) Maximum bytes for this bucket.
    """

    def __init__(self,
                 *,
                 firewall: 'Firewall' = None,
                 activity_tracking: 'ActivityTracking' = None,
                 metrics_monitoring: 'MetricsMonitoring' = None,
                 hard_quota: int = None) -> None:
        """
        Initialize a BucketPatch object.

        :param Firewall firewall: (optional) An access control mechanism based on
               the network (IP address) where request originated. Requests not originating
               from IP addresses listed in the `allowed_ip` field will be denied
               regardless of any access policies (including public access) that might
               otherwise permit the request.  Viewing or updating the `Firewall` element
               requires the requester to have the `manager` role.
        :param ActivityTracking activity_tracking: (optional) Enables sending log
               data to IBM Cloud Activity Tracker to provide visibility into object read
               and write events. All object events are sent to the activity tracker
               instance defined in the `activity_tracker_crn` field.
        :param MetricsMonitoring metrics_monitoring: (optional) Enables sending
               metrics to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud
               Monitoring instance defined in the `monitoring_crn` field.
        :param int hard_quota: (optional) Maximum bytes for this bucket.
        """
        self.firewall = firewall
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring
        self.hard_quota = hard_quota

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BucketPatch':
        """Initialize a BucketPatch object from a json dictionary."""
        args = {}
        if 'firewall' in _dict:
            args['firewall'] = Firewall.from_dict(_dict.get('firewall'))
        if 'activity_tracking' in _dict:
            args['activity_tracking'] = ActivityTracking.from_dict(_dict.get('activity_tracking'))
        if 'metrics_monitoring' in _dict:
            args['metrics_monitoring'] = MetricsMonitoring.from_dict(_dict.get('metrics_monitoring'))
        if 'hard_quota' in _dict:
            args['hard_quota'] = _dict.get('hard_quota')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BucketPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'firewall') and self.firewall is not None:
            if isinstance(self.firewall, dict):
                _dict['firewall'] = self.firewall
            else:
                _dict['firewall'] = self.firewall.to_dict()
        if hasattr(self, 'activity_tracking') and self.activity_tracking is not None:
            if isinstance(self.activity_tracking, dict):
                _dict['activity_tracking'] = self.activity_tracking
            else:
                _dict['activity_tracking'] = self.activity_tracking.to_dict()
        if hasattr(self, 'metrics_monitoring') and self.metrics_monitoring is not None:
            if isinstance(self.metrics_monitoring, dict):
                _dict['metrics_monitoring'] = self.metrics_monitoring
            else:
                _dict['metrics_monitoring'] = self.metrics_monitoring.to_dict()
        if hasattr(self, 'hard_quota') and self.hard_quota is not None:
            _dict['hard_quota'] = self.hard_quota
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BucketPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BucketPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BucketPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Firewall():
    """
    An access control mechanism based on the network (IP address) where request
    originated. Requests not originating from IP addresses listed in the `allowed_ip`
    field will be denied regardless of any access policies (including public access) that
    might otherwise permit the request.  Viewing or updating the `Firewall` element
    requires the requester to have the `manager` role.

    :attr List[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
          notation to be affected by firewall in CIDR notation is supported. Passing an
          empty array will lift the IP address filter.  The `allowed_ip` array can contain
          a maximum of 1000 items.
    :attr List[str] denied_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
          notation to be affected by firewall in CIDR notation is supported. Passing an
          empty array will lift the IP address filter.  The `denied_ip` array can contain
          a maximum of 1000 items.
    :attr List[str] allowed_network_type: (optional) Indicates which network types
          are allowed for bucket access. May contain `public`, `private`, and/or `direct`
          elements. Setting `allowed_network_type` to only `private` will prevent access
          to object storage from outside of the IBM Cloud.  The entire array will be
          overwritten in a `PATCH` operation. For more information on network types, [see
          the
          documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
    """

    def __init__(self,
                 *,
                 allowed_ip: List[str] = None,
                 denied_ip: List[str] = None,
                 allowed_network_type: List[str] = None) -> None:
        """
        Initialize a Firewall object.

        :param List[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in
               CIDR notation to be affected by firewall in CIDR notation is supported.
               Passing an empty array will lift the IP address filter.  The `allowed_ip`
               array can contain a maximum of 1000 items.
        :param List[str] denied_ip: (optional) List of IPv4 or IPv6 addresses in
               CIDR notation to be affected by firewall in CIDR notation is supported.
               Passing an empty array will lift the IP address filter.  The `denied_ip`
               array can contain a maximum of 1000 items.
        :param List[str] allowed_network_type: (optional) Indicates which network
               types are allowed for bucket access. May contain `public`, `private`,
               and/or `direct` elements. Setting `allowed_network_type` to only `private`
               will prevent access to object storage from outside of the IBM Cloud.  The
               entire array will be overwritten in a `PATCH` operation. For more
               information on network types, [see the
               documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
        """
        self.allowed_ip = allowed_ip
        self.denied_ip = denied_ip
        self.allowed_network_type = allowed_network_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Firewall':
        """Initialize a Firewall object from a json dictionary."""
        args = {}
        if 'allowed_ip' in _dict:
            args['allowed_ip'] = _dict.get('allowed_ip')
        if 'denied_ip' in _dict:
            args['denied_ip'] = _dict.get('denied_ip')
        if 'allowed_network_type' in _dict:
            args['allowed_network_type'] = _dict.get('allowed_network_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Firewall object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allowed_ip') and self.allowed_ip is not None:
            _dict['allowed_ip'] = self.allowed_ip
        if hasattr(self, 'denied_ip') and self.denied_ip is not None:
            _dict['denied_ip'] = self.denied_ip
        if hasattr(self, 'allowed_network_type') and self.allowed_network_type is not None:
            _dict['allowed_network_type'] = self.allowed_network_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Firewall object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Firewall') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Firewall') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AllowedNetworkTypeEnum(str, Enum):
        """
        May contain `public`, `private`, and/or `direct` elements. Setting
        `allowed_network_type` to only `private` will prevent access to object storage
        from outside of the IBM Cloud.  The entire array will be overwritten in a `PATCH`
        operation. For more information on network types, [see the
        documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
        """
        PUBLIC = 'public'
        PRIVATE = 'private'
        DIRECT = 'direct'


class MetricsMonitoring():
    """
    Enables sending metrics to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud
    Monitoring instance defined in the `monitoring_crn` field.

    :attr bool usage_metrics_enabled: (optional) If set to `true`, all usage metrics
          (i.e. `bytes_used`) will be sent to the monitoring service.
    :attr bool request_metrics_enabled: (optional) If set to `true`, all request
          metrics (i.e. `rest.object.head`) will be sent to the monitoring service.
    :attr str metrics_monitoring_crn: (optional) Required the first time
          `metrics_monitoring` is configured. The instance of IBM Cloud Monitoring that
          will receive the bucket metrics. The format is
          "crn:v1:bluemix:public:logdnaat:{bucket location}:a/{storage
          account}:{monitoring service instance}::".
    """

    def __init__(self,
                 *,
                 usage_metrics_enabled: bool = None,
                 request_metrics_enabled: bool = None,
                 metrics_monitoring_crn: str = None) -> None:
        """
        Initialize a MetricsMonitoring object.

        :param bool usage_metrics_enabled: (optional) If set to `true`, all usage
               metrics (i.e. `bytes_used`) will be sent to the monitoring service.
        :param bool request_metrics_enabled: (optional) If set to `true`, all
               request metrics (i.e. `rest.object.head`) will be sent to the monitoring
               service.
        :param str metrics_monitoring_crn: (optional) Required the first time
               `metrics_monitoring` is configured. The instance of IBM Cloud Monitoring
               that will receive the bucket metrics. The format is
               "crn:v1:bluemix:public:logdnaat:{bucket location}:a/{storage
               account}:{monitoring service instance}::".
        """
        self.usage_metrics_enabled = usage_metrics_enabled
        self.request_metrics_enabled = request_metrics_enabled
        self.metrics_monitoring_crn = metrics_monitoring_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricsMonitoring':
        """Initialize a MetricsMonitoring object from a json dictionary."""
        args = {}
        if 'usage_metrics_enabled' in _dict:
            args['usage_metrics_enabled'] = _dict.get('usage_metrics_enabled')
        if 'request_metrics_enabled' in _dict:
            args['request_metrics_enabled'] = _dict.get('request_metrics_enabled')
        if 'metrics_monitoring_crn' in _dict:
            args['metrics_monitoring_crn'] = _dict.get('metrics_monitoring_crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricsMonitoring object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'usage_metrics_enabled') and self.usage_metrics_enabled is not None:
            _dict['usage_metrics_enabled'] = self.usage_metrics_enabled
        if hasattr(self, 'request_metrics_enabled') and self.request_metrics_enabled is not None:
            _dict['request_metrics_enabled'] = self.request_metrics_enabled
        if hasattr(self, 'metrics_monitoring_crn') and self.metrics_monitoring_crn is not None:
            _dict['metrics_monitoring_crn'] = self.metrics_monitoring_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricsMonitoring object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MetricsMonitoring') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricsMonitoring') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
