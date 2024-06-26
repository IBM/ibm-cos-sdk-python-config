# coding: utf-8

# (C) Copyright IBM Corp. 2024.
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

# IBM OpenAPI SDK Code Generator Version: 3.91.0-d9755c53-20240605-153412

"""
REST API used to configure Cloud Object Storage buckets.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
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
    def new_instance(
        cls,
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

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the ResourceConfiguration service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # buckets
    #########################

    def get_bucket_config(
        self,
        bucket: str,
        **kwargs,
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_bucket_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket']
        path_param_values = self.encode_path_vars(bucket)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/b/{bucket}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_bucket_config(
        self,
        bucket: str,
        *,
        bucket_patch: Optional['BucketPatch'] = None,
        if_match: Optional[str] = None,
        **kwargs,
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
        if bucket_patch is not None and isinstance(bucket_patch, BucketPatch):
            bucket_patch = convert_model(bucket_patch)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_bucket_config',
        )
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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ActivityTracking:
    """
    Enables sending log data to IBM Cloud Activity Tracker Event Routing to provide
    visibility into bucket management, object read and write events. (Recommended) When
    the `activity_tracker_crn` is not populated, then enabled events are sent to the
    Activity Tracker Event Routing instance at the container's location unless otherwise
    specified in the Activity Tracker Event Routing Event Routing service configuration.
    (Legacy) When the `activity_tracker_crn` is populated, then enabled events are sent to
    the Activity Tracker Event Routing instance specified.

    :param bool read_data_events: (optional) If set to `true`, all object read
          events (i.e. downloads) will be sent to Activity Tracker Event Routing.
    :param bool write_data_events: (optional) If set to `true`, all object write
          events (i.e. uploads) will be sent to Activity Tracker Event Routing.
    :param str activity_tracker_crn: (optional) When the `activity_tracker_crn` is
          not populated, then enabled events are sent to the Activity Tracker Event
          Routing instance associated to the container's location unless otherwise
          specified in the Activity Tracker Event Routing Event Routing service
          configuration. If `activity_tracker_crn` is populated, then enabled events are
          sent to the Activity Tracker Event Routing instance specified and bucket
          management events are always enabled.
    :param bool management_events: (optional) This field only applies if
          `activity_tracker_crn` is not populated. If set to `true`, all bucket management
          events will be sent to Activity Tracker Event Routing.
    """

    def __init__(
        self,
        *,
        read_data_events: Optional[bool] = None,
        write_data_events: Optional[bool] = None,
        activity_tracker_crn: Optional[str] = None,
        management_events: Optional[bool] = None,
    ) -> None:
        """
        Initialize a ActivityTracking object.

        :param bool read_data_events: (optional) If set to `true`, all object read
               events (i.e. downloads) will be sent to Activity Tracker Event Routing.
        :param bool write_data_events: (optional) If set to `true`, all object
               write events (i.e. uploads) will be sent to Activity Tracker Event Routing.
        :param str activity_tracker_crn: (optional) When the `activity_tracker_crn`
               is not populated, then enabled events are sent to the Activity Tracker
               Event Routing instance associated to the container's location unless
               otherwise specified in the Activity Tracker Event Routing Event Routing
               service configuration. If `activity_tracker_crn` is populated, then enabled
               events are sent to the Activity Tracker Event Routing instance specified
               and bucket management events are always enabled.
        :param bool management_events: (optional) This field only applies if
               `activity_tracker_crn` is not populated. If set to `true`, all bucket
               management events will be sent to Activity Tracker Event Routing.
        """
        self.read_data_events = read_data_events
        self.write_data_events = write_data_events
        self.activity_tracker_crn = activity_tracker_crn
        self.management_events = management_events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActivityTracking':
        """Initialize a ActivityTracking object from a json dictionary."""
        args = {}
        if (read_data_events := _dict.get('read_data_events')) is not None:
            args['read_data_events'] = read_data_events
        if (write_data_events := _dict.get('write_data_events')) is not None:
            args['write_data_events'] = write_data_events
        if (activity_tracker_crn := _dict.get('activity_tracker_crn')) is not None:
            args['activity_tracker_crn'] = activity_tracker_crn
        if (management_events := _dict.get('management_events')) is not None:
            args['management_events'] = management_events
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
        if hasattr(self, 'management_events') and self.management_events is not None:
            _dict['management_events'] = self.management_events
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


class Bucket:
    """
    A bucket.

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
    :param int noncurrent_bytes_used: (optional) Total size of all non-current
          object versions in the bucket. Non-mutable.
    :param int delete_marker_count: (optional) Total number of delete markers in the
          bucket. Non-mutable.
    :param Firewall firewall: (optional) An access control mechanism based on the
          network (IP address) where request originated. Requests not originating from IP
          addresses listed in the `allowed_ip` field will be denied regardless of any
          access policies (including public access) that might otherwise permit the
          request.  Viewing or updating the `Firewall` element requires the requester to
          have the `manager` role.
    :param ActivityTracking activity_tracking: (optional) Enables sending log data
          to IBM Cloud Activity Tracker Event Routing to provide visibility into bucket
          management, object read and write events. (Recommended) When the
          `activity_tracker_crn` is not populated, then enabled events are sent to the
          Activity Tracker Event Routing instance at the container's location unless
          otherwise specified in the Activity Tracker Event Routing Event Routing service
          configuration. (Legacy) When the `activity_tracker_crn` is populated, then
          enabled events are sent to the Activity Tracker Event Routing instance
          specified.
    :param MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics
          to IBM Cloud Monitoring.  All metrics are opt-in. (Recommended) When the
          `metrics_monitoring_crn` is not populated, then enabled metrics are sent to the
          Monitoring instance at the container's location unless otherwise specified in
          the Metrics Router service configuration. (Legacy) When the
          `metrics_monitoring_crn` is populated, then enabled metrics are sent to the
          Monitoring instance defined in the `metrics_monitoring_crn` field.
    :param int hard_quota: (optional) Maximum bytes for this bucket.
    :param ProtectionManagementResponse protection_management: (optional) Data
          structure holding protection management response.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        crn: Optional[str] = None,
        service_instance_id: Optional[str] = None,
        service_instance_crn: Optional[str] = None,
        time_created: Optional[datetime] = None,
        time_updated: Optional[datetime] = None,
        object_count: Optional[int] = None,
        bytes_used: Optional[int] = None,
        noncurrent_object_count: Optional[int] = None,
        noncurrent_bytes_used: Optional[int] = None,
        delete_marker_count: Optional[int] = None,
        firewall: Optional['Firewall'] = None,
        activity_tracking: Optional['ActivityTracking'] = None,
        metrics_monitoring: Optional['MetricsMonitoring'] = None,
        hard_quota: Optional[int] = None,
        protection_management: Optional['ProtectionManagementResponse'] = None,
    ) -> None:
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
               data to IBM Cloud Activity Tracker Event Routing to provide visibility into
               bucket management, object read and write events. (Recommended) When the
               `activity_tracker_crn` is not populated, then enabled events are sent to
               the Activity Tracker Event Routing instance at the container's location
               unless otherwise specified in the Activity Tracker Event Routing Event
               Routing service configuration. (Legacy) When the `activity_tracker_crn` is
               populated, then enabled events are sent to the Activity Tracker Event
               Routing instance specified.
        :param MetricsMonitoring metrics_monitoring: (optional) Enables sending
               metrics to IBM Cloud Monitoring.  All metrics are opt-in. (Recommended)
               When the `metrics_monitoring_crn` is not populated, then enabled metrics
               are sent to the Monitoring instance at the container's location unless
               otherwise specified in the Metrics Router service configuration. (Legacy)
               When the `metrics_monitoring_crn` is populated, then enabled metrics are
               sent to the Monitoring instance defined in the `metrics_monitoring_crn`
               field.
        :param int hard_quota: (optional) Maximum bytes for this bucket.
        :param ProtectionManagementResponse protection_management: (optional) Data
               structure holding protection management response.
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
        self.protection_management = protection_management

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Bucket':
        """Initialize a Bucket object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        if (service_instance_id := _dict.get('service_instance_id')) is not None:
            args['service_instance_id'] = service_instance_id
        if (service_instance_crn := _dict.get('service_instance_crn')) is not None:
            args['service_instance_crn'] = service_instance_crn
        if (time_created := _dict.get('time_created')) is not None:
            args['time_created'] = string_to_datetime(time_created)
        if (time_updated := _dict.get('time_updated')) is not None:
            args['time_updated'] = string_to_datetime(time_updated)
        if (object_count := _dict.get('object_count')) is not None:
            args['object_count'] = object_count
        if (bytes_used := _dict.get('bytes_used')) is not None:
            args['bytes_used'] = bytes_used
        if (noncurrent_object_count := _dict.get('noncurrent_object_count')) is not None:
            args['noncurrent_object_count'] = noncurrent_object_count
        if (noncurrent_bytes_used := _dict.get('noncurrent_bytes_used')) is not None:
            args['noncurrent_bytes_used'] = noncurrent_bytes_used
        if (delete_marker_count := _dict.get('delete_marker_count')) is not None:
            args['delete_marker_count'] = delete_marker_count
        if (firewall := _dict.get('firewall')) is not None:
            args['firewall'] = Firewall.from_dict(firewall)
        if (activity_tracking := _dict.get('activity_tracking')) is not None:
            args['activity_tracking'] = ActivityTracking.from_dict(activity_tracking)
        if (metrics_monitoring := _dict.get('metrics_monitoring')) is not None:
            args['metrics_monitoring'] = MetricsMonitoring.from_dict(metrics_monitoring)
        if (hard_quota := _dict.get('hard_quota')) is not None:
            args['hard_quota'] = hard_quota
        if (protection_management := _dict.get('protection_management')) is not None:
            args['protection_management'] = ProtectionManagementResponse.from_dict(protection_management)
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
        if hasattr(self, 'protection_management') and self.protection_management is not None:
            if isinstance(self.protection_management, dict):
                _dict['protection_management'] = self.protection_management
            else:
                _dict['protection_management'] = self.protection_management.to_dict()
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


class BucketPatch:
    """
    An object containing new bucket metadata.

    :param Firewall firewall: (optional) An access control mechanism based on the
          network (IP address) where request originated. Requests not originating from IP
          addresses listed in the `allowed_ip` field will be denied regardless of any
          access policies (including public access) that might otherwise permit the
          request.  Viewing or updating the `Firewall` element requires the requester to
          have the `manager` role.
    :param ActivityTracking activity_tracking: (optional) Enables sending log data
          to IBM Cloud Activity Tracker Event Routing to provide visibility into bucket
          management, object read and write events. (Recommended) When the
          `activity_tracker_crn` is not populated, then enabled events are sent to the
          Activity Tracker Event Routing instance at the container's location unless
          otherwise specified in the Activity Tracker Event Routing Event Routing service
          configuration. (Legacy) When the `activity_tracker_crn` is populated, then
          enabled events are sent to the Activity Tracker Event Routing instance
          specified.
    :param MetricsMonitoring metrics_monitoring: (optional) Enables sending metrics
          to IBM Cloud Monitoring.  All metrics are opt-in. (Recommended) When the
          `metrics_monitoring_crn` is not populated, then enabled metrics are sent to the
          Monitoring instance at the container's location unless otherwise specified in
          the Metrics Router service configuration. (Legacy) When the
          `metrics_monitoring_crn` is populated, then enabled metrics are sent to the
          Monitoring instance defined in the `metrics_monitoring_crn` field.
    :param int hard_quota: (optional) Maximum bytes for this bucket.
    :param ProtectionManagement protection_management: (optional) Data structure
          holding protection management operations.
    """

    def __init__(
        self,
        *,
        firewall: Optional['Firewall'] = None,
        activity_tracking: Optional['ActivityTracking'] = None,
        metrics_monitoring: Optional['MetricsMonitoring'] = None,
        hard_quota: Optional[int] = None,
        protection_management: Optional['ProtectionManagement'] = None,
    ) -> None:
        """
        Initialize a BucketPatch object.

        :param Firewall firewall: (optional) An access control mechanism based on
               the network (IP address) where request originated. Requests not originating
               from IP addresses listed in the `allowed_ip` field will be denied
               regardless of any access policies (including public access) that might
               otherwise permit the request.  Viewing or updating the `Firewall` element
               requires the requester to have the `manager` role.
        :param ActivityTracking activity_tracking: (optional) Enables sending log
               data to IBM Cloud Activity Tracker Event Routing to provide visibility into
               bucket management, object read and write events. (Recommended) When the
               `activity_tracker_crn` is not populated, then enabled events are sent to
               the Activity Tracker Event Routing instance at the container's location
               unless otherwise specified in the Activity Tracker Event Routing Event
               Routing service configuration. (Legacy) When the `activity_tracker_crn` is
               populated, then enabled events are sent to the Activity Tracker Event
               Routing instance specified.
        :param MetricsMonitoring metrics_monitoring: (optional) Enables sending
               metrics to IBM Cloud Monitoring.  All metrics are opt-in. (Recommended)
               When the `metrics_monitoring_crn` is not populated, then enabled metrics
               are sent to the Monitoring instance at the container's location unless
               otherwise specified in the Metrics Router service configuration. (Legacy)
               When the `metrics_monitoring_crn` is populated, then enabled metrics are
               sent to the Monitoring instance defined in the `metrics_monitoring_crn`
               field.
        :param int hard_quota: (optional) Maximum bytes for this bucket.
        :param ProtectionManagement protection_management: (optional) Data
               structure holding protection management operations.
        """
        self.firewall = firewall
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring
        self.hard_quota = hard_quota
        self.protection_management = protection_management

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BucketPatch':
        """Initialize a BucketPatch object from a json dictionary."""
        args = {}
        if (firewall := _dict.get('firewall')) is not None:
            args['firewall'] = Firewall.from_dict(firewall)
        if (activity_tracking := _dict.get('activity_tracking')) is not None:
            args['activity_tracking'] = ActivityTracking.from_dict(activity_tracking)
        if (metrics_monitoring := _dict.get('metrics_monitoring')) is not None:
            args['metrics_monitoring'] = MetricsMonitoring.from_dict(metrics_monitoring)
        if (hard_quota := _dict.get('hard_quota')) is not None:
            args['hard_quota'] = hard_quota
        if (protection_management := _dict.get('protection_management')) is not None:
            args['protection_management'] = ProtectionManagement.from_dict(protection_management)
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
        if hasattr(self, 'protection_management') and self.protection_management is not None:
            if isinstance(self.protection_management, dict):
                _dict['protection_management'] = self.protection_management
            else:
                _dict['protection_management'] = self.protection_management.to_dict()
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


class Firewall:
    """
    An access control mechanism based on the network (IP address) where request
    originated. Requests not originating from IP addresses listed in the `allowed_ip`
    field will be denied regardless of any access policies (including public access) that
    might otherwise permit the request.  Viewing or updating the `Firewall` element
    requires the requester to have the `manager` role.

    :param List[str] allowed_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
          notation to be affected by firewall in CIDR notation is supported. Passing an
          empty array will lift the IP address filter.  The `allowed_ip` array can contain
          a maximum of 1000 items.
    :param List[str] denied_ip: (optional) List of IPv4 or IPv6 addresses in CIDR
          notation to be affected by firewall in CIDR notation is supported. Passing an
          empty array will lift the IP address filter.  The `denied_ip` array can contain
          a maximum of 1000 items.
    :param List[str] allowed_network_type: (optional) Indicates which network types
          are allowed for bucket access. May contain `public`, `private`, and/or `direct`
          elements. Setting `allowed_network_type` to only `private` will prevent access
          to object storage from outside of the IBM Cloud.  The entire array will be
          overwritten in a `PATCH` operation. For more information on network types, [see
          the
          documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#advanced-endpoint-types).
    """

    def __init__(
        self,
        *,
        allowed_ip: Optional[List[str]] = None,
        denied_ip: Optional[List[str]] = None,
        allowed_network_type: Optional[List[str]] = None,
    ) -> None:
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
        if (allowed_ip := _dict.get('allowed_ip')) is not None:
            args['allowed_ip'] = allowed_ip
        if (denied_ip := _dict.get('denied_ip')) is not None:
            args['denied_ip'] = denied_ip
        if (allowed_network_type := _dict.get('allowed_network_type')) is not None:
            args['allowed_network_type'] = allowed_network_type
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



class MetricsMonitoring:
    """
    Enables sending metrics to IBM Cloud Monitoring.  All metrics are opt-in.
    (Recommended) When the `metrics_monitoring_crn` is not populated, then enabled metrics
    are sent to the Monitoring instance at the container's location unless otherwise
    specified in the Metrics Router service configuration. (Legacy) When the
    `metrics_monitoring_crn` is populated, then enabled metrics are sent to the Monitoring
    instance defined in the `metrics_monitoring_crn` field.

    :param bool usage_metrics_enabled: (optional) If set to `true`, all usage
          metrics (i.e. `bytes_used`) will be sent to the monitoring service.
    :param bool request_metrics_enabled: (optional) If set to `true`, all request
          metrics (i.e. `rest.object.head`) will be sent to the monitoring service.
    :param str metrics_monitoring_crn: (optional) When the `metrics_monitoring_crn`
          is not populated, then enabled metrics are sent to the monitoring instance
          associated to the container's location unless otherwise specified in the Metrics
          Router service configuration. If `metrics_monitoring_crn` is populated, then
          enabled events are sent to the Metrics Monitoring instance specified.
    """

    def __init__(
        self,
        *,
        usage_metrics_enabled: Optional[bool] = None,
        request_metrics_enabled: Optional[bool] = None,
        metrics_monitoring_crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a MetricsMonitoring object.

        :param bool usage_metrics_enabled: (optional) If set to `true`, all usage
               metrics (i.e. `bytes_used`) will be sent to the monitoring service.
        :param bool request_metrics_enabled: (optional) If set to `true`, all
               request metrics (i.e. `rest.object.head`) will be sent to the monitoring
               service.
        :param str metrics_monitoring_crn: (optional) When the
               `metrics_monitoring_crn` is not populated, then enabled metrics are sent to
               the monitoring instance associated to the container's location unless
               otherwise specified in the Metrics Router service configuration. If
               `metrics_monitoring_crn` is populated, then enabled events are sent to the
               Metrics Monitoring instance specified.
        """
        self.usage_metrics_enabled = usage_metrics_enabled
        self.request_metrics_enabled = request_metrics_enabled
        self.metrics_monitoring_crn = metrics_monitoring_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricsMonitoring':
        """Initialize a MetricsMonitoring object from a json dictionary."""
        args = {}
        if (usage_metrics_enabled := _dict.get('usage_metrics_enabled')) is not None:
            args['usage_metrics_enabled'] = usage_metrics_enabled
        if (request_metrics_enabled := _dict.get('request_metrics_enabled')) is not None:
            args['request_metrics_enabled'] = request_metrics_enabled
        if (metrics_monitoring_crn := _dict.get('metrics_monitoring_crn')) is not None:
            args['metrics_monitoring_crn'] = metrics_monitoring_crn
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


class ProtectionManagement:
    """
    Data structure holding protection management operations.

    :param str requested_state: (optional) If set to `activate`, protection
          management action on the bucket is being activated.
    :param str protection_management_token: (optional) This field is required when
          using requested_state\:`activate` and holds a JWT that is provided by the Cloud
          Operator. This should be the encoded JWT.
    """

    def __init__(
        self,
        *,
        requested_state: Optional[str] = None,
        protection_management_token: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProtectionManagement object.

        :param str requested_state: (optional) If set to `activate`, protection
               management action on the bucket is being activated.
        :param str protection_management_token: (optional) This field is required
               when using requested_state\:`activate` and holds a JWT that is provided by
               the Cloud Operator. This should be the encoded JWT.
        """
        self.requested_state = requested_state
        self.protection_management_token = protection_management_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProtectionManagement':
        """Initialize a ProtectionManagement object from a json dictionary."""
        args = {}
        if (requested_state := _dict.get('requested_state')) is not None:
            args['requested_state'] = requested_state
        if (protection_management_token := _dict.get('protection_management_token')) is not None:
            args['protection_management_token'] = protection_management_token
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProtectionManagement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'requested_state') and self.requested_state is not None:
            _dict['requested_state'] = self.requested_state
        if hasattr(self, 'protection_management_token') and self.protection_management_token is not None:
            _dict['protection_management_token'] = self.protection_management_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProtectionManagement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProtectionManagement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProtectionManagement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RequestedStateEnum(str, Enum):
        """
        If set to `activate`, protection management action on the bucket is being
        activated.
        """

        ACTIVATE = 'activate'
        DEACTIVATE = 'deactivate'



class ProtectionManagementResponse:
    """
    Data structure holding protection management response.

    :param str token_applied_counter: (optional) Indicates the X number of
          protection management tokens that have been applied to the bucket in its
          lifetime.
    :param List[ProtectionManagementResponseTokenEntry] token_entries: (optional)
          The 'protection management token list' holding a recent list of applied tokens.
          This list may contain a subset of all tokens applied to the bucket, as indicated
          by the counter.
    """

    def __init__(
        self,
        *,
        token_applied_counter: Optional[str] = None,
        token_entries: Optional[List['ProtectionManagementResponseTokenEntry']] = None,
    ) -> None:
        """
        Initialize a ProtectionManagementResponse object.

        :param str token_applied_counter: (optional) Indicates the X number of
               protection management tokens that have been applied to the bucket in its
               lifetime.
        :param List[ProtectionManagementResponseTokenEntry] token_entries:
               (optional) The 'protection management token list' holding a recent list of
               applied tokens. This list may contain a subset of all tokens applied to the
               bucket, as indicated by the counter.
        """
        self.token_applied_counter = token_applied_counter
        self.token_entries = token_entries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProtectionManagementResponse':
        """Initialize a ProtectionManagementResponse object from a json dictionary."""
        args = {}
        if (token_applied_counter := _dict.get('token_applied_counter')) is not None:
            args['token_applied_counter'] = token_applied_counter
        if (token_entries := _dict.get('token_entries')) is not None:
            args['token_entries'] = [ProtectionManagementResponseTokenEntry.from_dict(v) for v in token_entries]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProtectionManagementResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token_applied_counter') and self.token_applied_counter is not None:
            _dict['token_applied_counter'] = self.token_applied_counter
        if hasattr(self, 'token_entries') and self.token_entries is not None:
            token_entries_list = []
            for v in self.token_entries:
                if isinstance(v, dict):
                    token_entries_list.append(v)
                else:
                    token_entries_list.append(v.to_dict())
            _dict['token_entries'] = token_entries_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProtectionManagementResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProtectionManagementResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProtectionManagementResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProtectionManagementResponseTokenEntry:
    """
    Data structure holding protection management token.

    :param str token_id: (optional)
    :param str token_expiration_time: (optional)
    :param str token_reference_id: (optional)
    :param str applied_time: (optional)
    :param str invalidated_time: (optional)
    :param str expiration_time: (optional)
    :param bool shorten_retention_flag: (optional)
    """

    def __init__(
        self,
        *,
        token_id: Optional[str] = None,
        token_expiration_time: Optional[str] = None,
        token_reference_id: Optional[str] = None,
        applied_time: Optional[str] = None,
        invalidated_time: Optional[str] = None,
        expiration_time: Optional[str] = None,
        shorten_retention_flag: Optional[bool] = None,
    ) -> None:
        """
        Initialize a ProtectionManagementResponseTokenEntry object.

        :param str token_id: (optional)
        :param str token_expiration_time: (optional)
        :param str token_reference_id: (optional)
        :param str applied_time: (optional)
        :param str invalidated_time: (optional)
        :param str expiration_time: (optional)
        :param bool shorten_retention_flag: (optional)
        """
        self.token_id = token_id
        self.token_expiration_time = token_expiration_time
        self.token_reference_id = token_reference_id
        self.applied_time = applied_time
        self.invalidated_time = invalidated_time
        self.expiration_time = expiration_time
        self.shorten_retention_flag = shorten_retention_flag

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProtectionManagementResponseTokenEntry':
        """Initialize a ProtectionManagementResponseTokenEntry object from a json dictionary."""
        args = {}
        if (token_id := _dict.get('token_id')) is not None:
            args['token_id'] = token_id
        if (token_expiration_time := _dict.get('token_expiration_time')) is not None:
            args['token_expiration_time'] = token_expiration_time
        if (token_reference_id := _dict.get('token_reference_id')) is not None:
            args['token_reference_id'] = token_reference_id
        if (applied_time := _dict.get('applied_time')) is not None:
            args['applied_time'] = applied_time
        if (invalidated_time := _dict.get('invalidated_time')) is not None:
            args['invalidated_time'] = invalidated_time
        if (expiration_time := _dict.get('expiration_time')) is not None:
            args['expiration_time'] = expiration_time
        if (shorten_retention_flag := _dict.get('shorten_retention_flag')) is not None:
            args['shorten_retention_flag'] = shorten_retention_flag
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProtectionManagementResponseTokenEntry object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token_id') and self.token_id is not None:
            _dict['token_id'] = self.token_id
        if hasattr(self, 'token_expiration_time') and self.token_expiration_time is not None:
            _dict['token_expiration_time'] = self.token_expiration_time
        if hasattr(self, 'token_reference_id') and self.token_reference_id is not None:
            _dict['token_reference_id'] = self.token_reference_id
        if hasattr(self, 'applied_time') and self.applied_time is not None:
            _dict['applied_time'] = self.applied_time
        if hasattr(self, 'invalidated_time') and self.invalidated_time is not None:
            _dict['invalidated_time'] = self.invalidated_time
        if hasattr(self, 'expiration_time') and self.expiration_time is not None:
            _dict['expiration_time'] = self.expiration_time
        if hasattr(self, 'shorten_retention_flag') and self.shorten_retention_flag is not None:
            _dict['shorten_retention_flag'] = self.shorten_retention_flag
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProtectionManagementResponseTokenEntry object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProtectionManagementResponseTokenEntry') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProtectionManagementResponseTokenEntry') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
