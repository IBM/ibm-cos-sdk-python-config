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
supports reading bucket metadata, setting IP access controls, and configuring logging and
monitoring services.
"""

from __future__ import absolute_import

import json
from .common import get_sdk_headers
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime

##############################################################################
# Service
##############################################################################

class ResourceConfigurationV1(BaseService):
    """The ResourceConfiguration V1 service."""

    default_url = 'https://config.cloud-object-storage.cloud.ibm.com/v1'

    def __init__(self,
                 url=default_url,
                 iam_apikey=None,
                 iam_access_token=None,
                 iam_url=None,
                 iam_client_id=None,
                 iam_client_secret=None,
                ):
        """
        Construct a new client for the ResourceConfiguration service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://config.cloud-object-storage.cloud.ibm.com/v1/v1").
               The base url may differ between IBM Cloud regions.

        :param str iam_apikey: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.cloud.ibm.com/identity/token'.

        :param str iam_client_id: An optional client_id value to use when interacting with the IAM service.

        :param str iam_client_secret: An optional client_secret value to use when interacting with the IAM service.
        """

        BaseService.__init__(self,
            vcap_services_name='resource_configuration',
            url=url,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            iam_client_id=iam_client_id,
            iam_client_secret=iam_client_secret,
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
        sdk_headers = get_sdk_headers('resource_configuration', 'V1', 'get_bucket_config')
        headers.update(sdk_headers)

        url = '/b/{0}'.format(*self._encode_path_vars(bucket))
        response = self.request(method='GET',
                                url=url,
                                headers=headers,
                                accept_json=True)
        return response


    def update_bucket_config(self, bucket, firewall=None, activity_tracking=None, metrics_monitoring=None, hard_quota=None, if_match=None, **kwargs):
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
        :param Firewall firewall: An access control mechanism based on the network (IP
        address) where request originated. Requests not originating from IP addresses
        listed in the `allowed_ip` field will be denied regardless of any access policies
        (including public access) that might otherwise permit the request.  Viewing or
        updating the `Firewall` element requires the requester to have the `manager` role.
        :param ActivityTracking activity_tracking: Enables sending log data to Activity
        Tracker and LogDNA to provide visibility into object read and write events. All
        object events are sent to the activity tracker instance defined in the
        `activity_tracker_crn` field.
        :param MetricsMonitoring metrics_monitoring: Enables sending metrics to IBM Cloud
        Monitoring. All metrics are sent to the IBM Cloud Monitoring instance defined in
        the `monitoring_crn` field.
        :param int hard_quota: Maximum bytes for this bucket.
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
        if activity_tracking is not None:
            activity_tracking = self._convert_model(activity_tracking, ActivityTracking)
        if metrics_monitoring is not None:
            metrics_monitoring = self._convert_model(metrics_monitoring, MetricsMonitoring)

        headers = {
            'if-match': if_match
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('resource_configuration', 'V1', 'update_bucket_config')
        headers.update(sdk_headers)

        data = {
            'firewall': firewall,
            'activity_tracking': activity_tracking,
            'metrics_monitoring': metrics_monitoring,
            'hard_quota': hard_quota
        }

        url = '/b/{0}'.format(*self._encode_path_vars(bucket))
        response = self.request(method='PATCH',
                                url=url,
                                headers=headers,
                                json=data,
                                accept_json=False)
        return response



##############################################################################
# Models
##############################################################################


class ActivityTracking(object):
    """
    Enables sending log data to Activity Tracker and LogDNA to provide visibility into
    object read and write events. All object events are sent to the activity tracker
    instance defined in the `activity_tracker_crn` field.

    :attr bool read_data_events: (optional) If set to `true`, all object read events (i.e.
    downloads) will be sent to Activity Tracker.
    :attr bool write_data_events: (optional) If set to `true`, all object write events
    (i.e. uploads) will be sent to Activity Tracker.
    :attr str activity_tracker_crn: (optional) Required the first time `activity_tracking`
    is configured. The instance of Activity Tracker that will receive object event data.
    The format is "crn:v1:bluemix:public:logdnaat:{bucket location}:a/{storage
    account}:{activity tracker service instance}::".
    """

    def __init__(self, read_data_events=None, write_data_events=None, activity_tracker_crn=None):
        """
        Initialize a ActivityTracking object.

        :param bool read_data_events: (optional) If set to `true`, all object read events
        (i.e. downloads) will be sent to Activity Tracker.
        :param bool write_data_events: (optional) If set to `true`, all object write
        events (i.e. uploads) will be sent to Activity Tracker.
        :param str activity_tracker_crn: (optional) Required the first time
        `activity_tracking` is configured. The instance of Activity Tracker that will
        receive object event data. The format is "crn:v1:bluemix:public:logdnaat:{bucket
        location}:a/{storage account}:{activity tracker service instance}::".
        """
        self.read_data_events = read_data_events
        self.write_data_events = write_data_events
        self.activity_tracker_crn = activity_tracker_crn

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActivityTracking object from a json dictionary."""
        args = {}
        validKeys = ['read_data_events', 'write_data_events', 'activity_tracker_crn']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError('Unrecognized keys detected in dictionary for class ActivityTracking: ' + ', '.join(badKeys))
        if 'read_data_events' in _dict:
            args['read_data_events'] = _dict.get('read_data_events')
        if 'write_data_events' in _dict:
            args['write_data_events'] = _dict.get('write_data_events')
        if 'activity_tracker_crn' in _dict:
            args['activity_tracker_crn'] = _dict.get('activity_tracker_crn')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'read_data_events') and self.read_data_events is not None:
            _dict['read_data_events'] = self.read_data_events
        if hasattr(self, 'write_data_events') and self.write_data_events is not None:
            _dict['write_data_events'] = self.write_data_events
        if hasattr(self, 'activity_tracker_crn') and self.activity_tracker_crn is not None:
            _dict['activity_tracker_crn'] = self.activity_tracker_crn
        return _dict

    def __str__(self):
        """Return a `str` version of this ActivityTracking object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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
    :attr int noncurrent_object_count: (optional) Number of non-current object versions in
    the bucket. Non-mutable.
    :attr int noncurrent_bytes_used: (optional) Total size of all non-current object
    versions in the bucket. Non-mutable.
    :attr int delete_marker_count: (optional) Total number of delete markers in the
    bucket. Non-mutable.
    :attr int hard_quota: (optional) Maximum bytes for this bucket.
    :attr Firewall firewall: (optional) An access control mechanism based on the network
    (IP address) where request originated. Requests not originating from IP addresses
    listed in the `allowed_ip` field will be denied regardless of any access policies
    (including public access) that might otherwise permit the request.  Viewing or
    updating the `Firewall` element requires the requester to have the `manager` role.
    :attr ActivityTracking activity_tracking: (optional) Enables sending log data to
    Activity Tracker and LogDNA to provide visibility into object read and write events.
    All object events are sent to the activity tracker instance defined in the
    `activity_tracker_crn` field.
    :attr MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics to IBM
    Cloud Monitoring. All metrics are sent to the IBM Cloud Monitoring instance defined in
    the `monitoring_crn` field.
    """

    def __init__(self, name=None, crn=None, service_instance_id=None, service_instance_crn=None, time_created=None, time_updated=None, object_count=None, bytes_used=None, noncurrent_object_count=None, noncurrent_bytes_used=None, delete_marker_count=None, hard_quota=None, firewall=None, activity_tracking=None, metrics_monitoring=None):
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
        :param int noncurrent_object_count: (optional) Number of non-current object
        versions in the bucket. Non-mutable.
        :param int noncurrent_bytes_used: (optional) Total size of all non-current object
        versions in the bucket. Non-mutable.
        :param int delete_marker_count: (optional) Total number of delete markers in the
        bucket. Non-mutable.
        :param int hard_quota: (optional) Maximum bytes for this bucket.
        :param Firewall firewall: (optional) An access control mechanism based on the
        network (IP address) where request originated. Requests not originating from IP
        addresses listed in the `allowed_ip` field will be denied regardless of any access
        policies (including public access) that might otherwise permit the request.
        Viewing or updating the `Firewall` element requires the requester to have the
        `manager` role.
        :param ActivityTracking activity_tracking: (optional) Enables sending log data to
        Activity Tracker and LogDNA to provide visibility into object read and write
        events. All object events are sent to the activity tracker instance defined in the
        `activity_tracker_crn` field.
        :param MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics to
        IBM Cloud Monitoring. All metrics are sent to the IBM Cloud Monitoring instance
        defined in the `monitoring_crn` field.
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
        self.hard_quota = hard_quota
        self.firewall = firewall
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Bucket object from a json dictionary."""
        args = {}
        validKeys = ['name', 'crn', 'service_instance_id', 'service_instance_crn', 'time_created', 'time_updated', 'object_count', 'bytes_used', 'noncurrent_object_count', 'noncurrent_bytes_used', 'delete_marker_count', 'hard_quota', 'firewall', 'activity_tracking', 'metrics_monitoring']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError('Unrecognized keys detected in dictionary for class Bucket: ' + ', '.join(badKeys))
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
        if 'hard_quota' in _dict:
            args['hard_quota'] = _dict.get('hard_quota')
        if 'firewall' in _dict:
            args['firewall'] = Firewall._from_dict(_dict.get('firewall'))
        if 'activity_tracking' in _dict:
            args['activity_tracking'] = ActivityTracking._from_dict(_dict.get('activity_tracking'))
        if 'metrics_monitoring' in _dict:
            args['metrics_monitoring'] = MetricsMonitoring._from_dict(_dict.get('metrics_monitoring'))
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
        if hasattr(self, 'noncurrent_object_count') and self.noncurrent_object_count is not None:
            _dict['noncurrent_object_count'] = self.noncurrent_object_count
        if hasattr(self, 'noncurrent_bytes_used') and self.noncurrent_bytes_used is not None:
            _dict['noncurrent_bytes_used'] = self.noncurrent_bytes_used
        if hasattr(self, 'delete_marker_count') and self.delete_marker_count is not None:
            _dict['delete_marker_count'] = self.delete_marker_count
        if hasattr(self, 'hard_quota') and self.hard_quota is not None:
            _dict['hard_quota'] = self.hard_quota
        if hasattr(self, 'firewall') and self.firewall is not None:
            _dict['firewall'] = self.firewall._to_dict()
        if hasattr(self, 'activity_tracking') and self.activity_tracking is not None:
            _dict['activity_tracking'] = self.activity_tracking._to_dict()
        if hasattr(self, 'metrics_monitoring') and self.metrics_monitoring is not None:
            _dict['metrics_monitoring'] = self.metrics_monitoring._to_dict()
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
    An access control mechanism based on the network (IP address) where request
    originated. Requests not originating from IP addresses listed in the `allowed_ip`
    field will be denied regardless of any access policies (including public access) that
    might otherwise permit the request.  Viewing or updating the `Firewall` element
    requires the requester to have the `manager` role.

    :attr list[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR notation
    to be affected by firewall in CIDR notation is supported. Passing an empty array will
    lift the IP address filter.  The `allowed_ip` array can contain a maximum of 1000
    items.
    :attr list[str] denied_ip: (optional) List of IPv4 or IPv6 addresses in CIDR notation
    to be affected by firewall in CIDR notation is supported. Passing an empty array will
    lift the IP address filter.  The `denied_ip` array can contain a maximum of 1000
    items.
    :attr list[str] allowed_network_type: (optional) Indicates which network types are
    allowed for bucket access. May contain `public`, `private`, and/or `direct` elements.
    Setting `allowed_network_type` to only `private` will prevent access to object storage
    from outside of the IBM Cloud.  The entire array will be overwritten in a `PATCH`
    operation. For more information on network types, [see the
    documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
    """

    def __init__(self, allowed_ip=None, denied_ip=None, allowed_network_type=None):
        """
        Initialize a Firewall object.

        :param list[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
        notation to be affected by firewall in CIDR notation is supported. Passing an
        empty array will lift the IP address filter.  The `allowed_ip` array can contain a
        maximum of 1000 items.
        :param list[str] denied_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
        notation to be affected by firewall in CIDR notation is supported. Passing an
        empty array will lift the IP address filter.  The `denied_ip` array can contain a
        maximum of 1000 items.
        :param list[str] allowed_network_type: (optional) Indicates which network types
        are allowed for bucket access. May contain `public`, `private`, and/or `direct`
        elements. Setting `allowed_network_type` to only `private` will prevent access to
        object storage from outside of the IBM Cloud.  The entire array will be
        overwritten in a `PATCH` operation. For more information on network types, [see
        the
        documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
        """
        self.allowed_ip = allowed_ip
        self.denied_ip = denied_ip
        self.allowed_network_type = allowed_network_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Firewall object from a json dictionary."""
        args = {}
        validKeys = ['allowed_ip', 'denied_ip', 'allowed_network_type']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError('Unrecognized keys detected in dictionary for class Firewall: ' + ', '.join(badKeys))
        if 'allowed_ip' in _dict:
            args['allowed_ip'] = _dict.get('allowed_ip')
        if 'denied_ip' in _dict:
            args['denied_ip'] = _dict.get('denied_ip')
        if 'allowed_network_type' in _dict:
            args['allowed_network_type'] = _dict.get('allowed_network_type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allowed_ip') and self.allowed_ip is not None:
            _dict['allowed_ip'] = self.allowed_ip
        if hasattr(self, 'denied_ip') and self.denied_ip is not None:
            _dict['denied_ip'] = self.denied_ip
        if hasattr(self, 'allowed_network_type') and self.allowed_network_type is not None:
            _dict['allowed_network_type'] = self.allowed_network_type
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


class MetricsMonitoring(object):
    """
    Enables sending metrics to IBM Cloud Monitoring. All metrics are sent to the IBM Cloud
    Monitoring instance defined in the `monitoring_crn` field.

    :attr bool usage_metrics_enabled: (optional) If set to `true`, all usage metrics (i.e.
    `bytes_used`) will be sent to the monitoring service.
    :attr bool request_metrics_enabled: (optional) If set to `true`, all request metrics
    (i.e. `rest.object.head`) will be sent to the monitoring service.
    :attr str metrics_monitoring_crn: (optional) Required the first time
    `metrics_monitoring` is configured. The instance of IBM Cloud Monitoring that will
    receive the bucket metrics. The format is "crn:v1:bluemix:public:logdnaat:{bucket
    location}:a/{storage account}:{monitoring service instance}::".
    """

    def __init__(self, usage_metrics_enabled=None, request_metrics_enabled=None, metrics_monitoring_crn=None):
        """
        Initialize a MetricsMonitoring object.

        :param bool usage_metrics_enabled: (optional) If set to `true`, all usage metrics
        (i.e. `bytes_used`) will be sent to the monitoring service.
        :param bool request_metrics_enabled: (optional) If set to `true`, all request
        metrics (i.e. `rest.object.head`) will be sent to the monitoring service.
        :param str metrics_monitoring_crn: (optional) Required the first time
        `metrics_monitoring` is configured. The instance of IBM Cloud Monitoring that will
        receive the bucket metrics. The format is "crn:v1:bluemix:public:logdnaat:{bucket
        location}:a/{storage account}:{monitoring service instance}::".
        """
        self.usage_metrics_enabled = usage_metrics_enabled
        self.request_metrics_enabled = request_metrics_enabled
        self.metrics_monitoring_crn = metrics_monitoring_crn

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricsMonitoring object from a json dictionary."""
        args = {}
        validKeys = ['usage_metrics_enabled', 'request_metrics_enabled', 'metrics_monitoring_crn']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError('Unrecognized keys detected in dictionary for class MetricsMonitoring: ' + ', '.join(badKeys))
        if 'usage_metrics_enabled' in _dict:
            args['usage_metrics_enabled'] = _dict.get('usage_metrics_enabled')
        if 'request_metrics_enabled' in _dict:
            args['request_metrics_enabled'] = _dict.get('request_metrics_enabled')
        if 'metrics_monitoring_crn' in _dict:
            args['metrics_monitoring_crn'] = _dict.get('metrics_monitoring_crn')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'usage_metrics_enabled') and self.usage_metrics_enabled is not None:
            _dict['usage_metrics_enabled'] = self.usage_metrics_enabled
        if hasattr(self, 'request_metrics_enabled') and self.request_metrics_enabled is not None:
            _dict['request_metrics_enabled'] = self.request_metrics_enabled
        if hasattr(self, 'metrics_monitoring_crn') and self.metrics_monitoring_crn is not None:
            _dict['metrics_monitoring_crn'] = self.metrics_monitoring_crn
        return _dict

    def __str__(self):
        """Return a `str` version of this MetricsMonitoring object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


