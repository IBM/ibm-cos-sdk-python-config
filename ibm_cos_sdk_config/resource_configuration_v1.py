# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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

# IBM OpenAPI SDK Code Generator Version: 3.98.0-8be2046a-20241205-162752

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
    # backupPolicy
    #########################

    def create_backup_policy(
        self,
        bucket: str,
        initial_retention: 'DeleteAfterDays',
        policy_name: str,
        target_backup_vault_crn: str,
        backup_type: str,
        *,
        m_d5: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a new backup policy to the COS Bucket.

        Attach a new Backup Policy on a bucket.
        This request results in the creation of a single, new RecoveryRange on the
        destination BackupVault.
        Deletion and re-creation of a BackupPolicy to the same BackupVault destination
        will generate a new RecoveryRange.
        The following shall be validated. Any failure to validate shall cause a HTTP 400
        to be returned.
          * the user has `cloud-object-storage.bucket.post_backup_policy` permissions on
        the source-bucket
          * the source-bucket must have `cloud-object-storage.backup_vault.sync`
        permissions on the Backup Vault
          * the source-bucket must have versioning-on
          * the Backup Vault must exist and be able to be contacted by the source-bucket
          * the source-bucket must not have an existing BackupPolicy targeting the Backup
        Vault
          * the source-bucket must not have a BackupPolicy with the same policy_name
          * the source-bucket must have fewer than 3 total BackupPolicies.

        :param str bucket: Name of the COS Bucket name.
        :param DeleteAfterDays initial_retention: The number of days to retain data
               within a RecoveryRange.
        :param str policy_name: The name granted to the policy. Validation :
                 * chars limited to alphanumeric, underscore, hyphen and period.
        :param str target_backup_vault_crn: The CRN for a COS BackupVault.
        :param str backup_type: The type of backup to support. For LA+GA this is
               limited to "continuous".
        :param str m_d5: (optional) MD5 hash of content. If provided, the hash of
               the request must match.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupPolicy` object
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        if initial_retention is None:
            raise ValueError('initial_retention must be provided')
        if policy_name is None:
            raise ValueError('policy_name must be provided')
        if target_backup_vault_crn is None:
            raise ValueError('target_backup_vault_crn must be provided')
        if backup_type is None:
            raise ValueError('backup_type must be provided')
        initial_retention = convert_model(initial_retention)
        headers = {
            'MD5': m_d5,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_backup_policy',
        )
        headers.update(sdk_headers)

        data = {
            'initial_retention': initial_retention,
            'policy_name': policy_name,
            'target_backup_vault_crn': target_backup_vault_crn,
            'backup_type': backup_type,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket']
        path_param_values = self.encode_path_vars(bucket)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/buckets/{bucket}/backup_policies'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_backup_policies(
        self,
        bucket: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List BackupPolicies.

        Get all backup policies on a bucket.
        Requires that the user has `cloud-object-storage.bucket.list_backup_policies`
        permissions on the source bucket.
        This request generates the "cloud-object-storage.bucket-backup-policy.list"
        ActivityTracking event.

        :param str bucket: Name of the COS Bucket name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupPolicyCollection` object
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_backup_policies',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket']
        path_param_values = self.encode_path_vars(bucket)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/buckets/{bucket}/backup_policies'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_backup_policy(
        self,
        bucket: str,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get BackupPolicy.

        Read a specific backup policy on a bucket.
        Requires that the user has `cloud-object-storage.bucket.get_backup_policy`
        permissions on the bucket.

        :param str bucket: name of the bucket affected.
        :param str policy_id: uuid of the BackupPolicy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupPolicy` object
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_backup_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket', 'policy_id']
        path_param_values = self.encode_path_vars(bucket, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/buckets/{bucket}/backup_policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_backup_policy(
        self,
        bucket: str,
        policy_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a BackupPolicy.

        Delete a specific BackupPolicy.
        Requires that the user has `cloud-object-storage.bucket.delete_backup_policy`
        permissions on the bucket.

        :param str bucket: name of the bucket affected.
        :param str policy_id: uuid of the BackupPolicy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not bucket:
            raise ValueError('bucket must be provided')
        if not policy_id:
            raise ValueError('policy_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_backup_policy',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['bucket', 'policy_id']
        path_param_values = self.encode_path_vars(bucket, policy_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/buckets/{bucket}/backup_policies/{policy_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # backupVault
    #########################

    def list_backup_vaults(
        self,
        service_instance_id: str,
        *,
        token: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        list BackupVaults.

        Returns a list of BackupVault CRNs owned by the account.
        Requires that the user has
        `cloud-object-storage.backup_vault.list_account_backup_vaults` permissions for the
        account.

        :param str service_instance_id: Name of the service_instance to list
               BackupVaults for.
        :param str token: (optional) the continuation token for controlling
               pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupVaultCollection` object
        """

        if not service_instance_id:
            raise ValueError('service_instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_backup_vaults',
        )
        headers.update(sdk_headers)

        params = {
            'service_instance_id': service_instance_id,
            'token': token,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/backup_vaults'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_backup_vault(
        self,
        service_instance_id: str,
        backup_vault_name: str,
        region: str,
        *,
        activity_tracking: Optional['BackupVaultActivityTracking'] = None,
        metrics_monitoring: Optional['BackupVaultMetricsMonitoring'] = None,
        sse_kp_customer_root_key_crn: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        create a BackupVault.

        Creates a BackupVault.
        Requires that the user has `cloud-object-storage.backup_vault.post_backup_vault`
        permissions for the account.
        Certain fields will be returned only if the user has specific permissions:
          - `activity_tracking` requires
        `cloud-object-storage.backup_vault.put_activity_tracking`
          - `metrics_monitoring` requires
        `cloud-object-storage.backup_vault.put_metrics_monitoring`.

        :param str service_instance_id: Name of the service_instance to list
               BackupVaults for.
        :param str backup_vault_name: The name given to a Bucket.
               Bucket names must be between 3 and 63 characters long must be made of
               lowercase letters, numbers, dots (periods), and dashes (hyphens). Bucket
               names must begin and end with a lowercase letter or number. Bucket names
               canâ€t contain consecutive dots or dashes. Bucket names that resemble IP
               addresses are not allowed.
               Bucket and BackupVault names exist in a global namespace and therefore must
               be unique.
        :param str region: the region in which this backup-vault should be created
               within.
        :param BackupVaultActivityTracking activity_tracking: (optional) Activity
               Tracking configuration. An empty object (`{}`) indicates no configuration,
               and no events will be sent (This is the same behavior as
               `{"management_events":false}`). Note that read/write events cannot be
               enabled, and events cannot be routed to a non-default Activity Tracker
               instance.
        :param BackupVaultMetricsMonitoring metrics_monitoring: (optional) Metrics
               Monitoring configuration. An empty object (`{}`) indicates no
               configuration, and no metrics will be collected (This is the same behavior
               as `{"usage_metrics_enabled":false}`). Note that request metrics cannot be
               enabled, and metrics cannot be routed to a non-default metrics router
               instance.
        :param str sse_kp_customer_root_key_crn: (optional) The CRN for a
               KeyProtect root key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupVault` object
        """

        if not service_instance_id:
            raise ValueError('service_instance_id must be provided')
        if backup_vault_name is None:
            raise ValueError('backup_vault_name must be provided')
        if region is None:
            raise ValueError('region must be provided')
        if activity_tracking is not None:
            activity_tracking = convert_model(activity_tracking)
        if metrics_monitoring is not None:
            metrics_monitoring = convert_model(metrics_monitoring)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_backup_vault',
        )
        headers.update(sdk_headers)

        params = {
            'service_instance_id': service_instance_id,
        }

        data = {
            'backup_vault_name': backup_vault_name,
            'region': region,
            'activity_tracking': activity_tracking,
            'metrics_monitoring': metrics_monitoring,
            'sse_kp_customer_root_key_crn': sse_kp_customer_root_key_crn,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/backup_vaults'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_backup_vault(
        self,
        backup_vault_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        get the config for a Backup Vault.

        Gets configuration information for a Backup Vault.
        Requires that the user has `cloud-object-storage.backup_vault.get_basic`
        permissions on the backup vault.
        Certain fields will be returned only if the user has specific permissions:
          - `activity_tracking` requires
        `cloud-object-storage.backup_vault.get_activity_tracking`
          - `metrics_monitoring` requires
        `cloud-object-storage.backup_vault.get_metrics_monitoring`
          - `sse_kp_customer_root_key_crn` requires
        `cloud-object-storage.backup_vault.get_crk_id`.

        :param str backup_vault_name: Name of the backup-vault to create or update.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupVault` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_backup_vault',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_backup_vault(
        self,
        backup_vault_name: str,
        backup_vault_patch: 'BackupVaultPatch',
        *,
        if_match: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the config on a Backup Vault.

        Update the Backup Vault config via JSON Merge Patch update semantics.
        In particular, note that providing an empty object (`{}`) to either field in the
        request body will remove any existing configuration.
        Requires that the user have specific permissions depending on what is being
        changed:
          - `activity_tracking` requires
        `cloud-object-storage.backup_vault.put_activity_tracking`
          - `metrics_monitoring` requires
        `cloud-object-storage.backup_vault.put_metrics_monitoring`.

        :param str backup_vault_name: Name of the backup-vault to create or update.
        :param BackupVaultPatch backup_vault_patch: A Backup Vault config object
               containing changes to apply to the existing Backup Vault config.
        :param str if_match: (optional) Conditionally update the Backup Vault
               config if and only if the ETag of the existing config exactly matches the
               provided If-Match MD5.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BackupVault` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        if backup_vault_patch is None:
            raise ValueError('backup_vault_patch must be provided')
        if isinstance(backup_vault_patch, BackupVaultPatch):
            backup_vault_patch = convert_model(backup_vault_patch)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_backup_vault',
        )
        headers.update(sdk_headers)

        data = json.dumps(backup_vault_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_backup_vault(
        self,
        backup_vault_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an empty Backup Vault.

        Delete the Backup Vault.
        Requires that the BackupVault not contain any RecoveryRanges.  Requires that the
        user has `cloud-object-storage.backup_vault.delete_backup_vault` permissions for
        the account.

        :param str backup_vault_name: Name of the backup-vault to create or update.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_backup_vault',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

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

    #########################
    # recoveryRanges
    #########################

    def list_recovery_ranges(
        self,
        backup_vault_name: str,
        *,
        source_resource_crn: Optional[str] = None,
        latest: Optional[str] = None,
        token: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List RecoveryRanges on a backup vault.

        List RecoveryRanges on a backup vault. Lists all available ranges for all source
        resources by default. The `?source_resource_crn` query parameter will limit the
        list to only ranges for the specified resource.
        Requires the user have `cloud-object-storage.backup_vault.list_recovery_ranges`
        permissions to the Backup Vault.

        :param str backup_vault_name: name of BackupVault.
        :param str source_resource_crn: (optional) CRN of source resource to filter
               on. This limits ranges returned to only ranges where the
               source_resource_crn matches the parameter value.
        :param str latest: (optional) If "true", then return only the latest
               RecoveryRange for each source-resource that is backed up.
               If "false" or not specified, then the default behavior is produced.
               Value is can insensative. If any value is provided other than "true" or
               "false" then return 400.
        :param str token: (optional) the continuation token for controlling
               pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecoveryRangeCollection` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_recovery_ranges',
        )
        headers.update(sdk_headers)

        params = {
            'source_resource_crn': source_resource_crn,
            'latest': latest,
            'token': token,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/recovery_ranges'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_source_resource_recovery_range(
        self,
        backup_vault_name: str,
        recovery_range_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        get RecoveryRange info.

        Get info for a specific RecoveryRange.
        Requires the user have `cloud-object-storage.backup_vault.get_recovery_range`
        permissions to the Backup Vault.

        :param str backup_vault_name: name of BackupVault to update.
        :param str recovery_range_id: ID of the RecoveryRange to update.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecoveryRange` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        if not recovery_range_id:
            raise ValueError('recovery_range_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_source_resource_recovery_range',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name', 'recovery_range_id']
        path_param_values = self.encode_path_vars(backup_vault_name, recovery_range_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/recovery_ranges/{recovery_range_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def patch_source_resource_recovery_range(
        self,
        backup_vault_name: str,
        recovery_range_id: str,
        recovery_range_patch: 'RecoveryRangePatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        patch RecoveryRange info.

        Update a RecoveryRange via JSON-merge-patch semantics.
        Requires the user have `cloud-object-storage.backup_vault.put_retention`
        permissions to the Backup Vault.
        The retention.delete_after_days value may only be extended.

        :param str backup_vault_name: name of BackupVault to update.
        :param str recovery_range_id: ID of the RecoveryRange to update.
        :param RecoveryRangePatch recovery_range_patch: The RecoveryRange
               configuration elements that are to be changed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecoveryRange` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        if not recovery_range_id:
            raise ValueError('recovery_range_id must be provided')
        if recovery_range_patch is None:
            raise ValueError('recovery_range_patch must be provided')
        if isinstance(recovery_range_patch, RecoveryRangePatch):
            recovery_range_patch = convert_model(recovery_range_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='patch_source_resource_recovery_range',
        )
        headers.update(sdk_headers)

        data = json.dumps(recovery_range_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name', 'recovery_range_id']
        path_param_values = self.encode_path_vars(backup_vault_name, recovery_range_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/recovery_ranges/{recovery_range_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # restore
    #########################

    def create_restore(
        self,
        backup_vault_name: str,
        recovery_range_id: str,
        restore_type: str,
        restore_point_in_time: datetime,
        target_resource_crn: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Initiate a Restore.

        Initiates a restore operation against some RecoveryRange to some destination
        bucket.
        The following shall be validated. Any failure to validate shall cause a HTTP 400
        to be returned.
          * The specified RecoveryRange must exist
          * The restore time must be within the RecoveryRange
          * the user has `cloud-object-storage.backup-vault.post_restore` permissions on
        the backup-vault
          * the target-bucket must exist and be able to be contacted by the Backup Vault
          * target-bucket must have versioning-on
          * the Backup Vault must have `cloud-object-storage.bucket.restore_sync`
        permissions on the target-bucket.

        :param str backup_vault_name: name of BackupVault to restore from.
        :param str recovery_range_id: A UUID that uniquely identifies a resource.
        :param str restore_type: The type of restore to support. More options will
               be available in the future.
        :param datetime restore_point_in_time: Timestamp format used throughout the
               API.
               Accepts the following formats:
               YYYY-MM-DDTHH:mm:ssZ YYYY-MM-DDTHH:mm:ss YYYY-MM-DDTHH:mm:ss-hh:mm
               YYYY-MM-DDTHH:mm:ss+hh:mm YYYY-MM-DDTHH:mm:ss.sssZ YYYY-MM-DDTHH:mm:ss.sss
               YYYY-MM-DDTHH:mm:ss.sss-hh:mm YYYY-MM-DDTHH:mm:ss.sss+hh:mm.
        :param str target_resource_crn: The CRN for a COS Bucket.
               Note that Softlayer CRNs do not contain dashes within the
               service_instance_id, whereas regular CRNs do. Although bucket backup is not
               supported for softlayer accounts, this need not be enforced at the CRN
               parsing level.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Restore` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        if recovery_range_id is None:
            raise ValueError('recovery_range_id must be provided')
        if restore_type is None:
            raise ValueError('restore_type must be provided')
        if restore_point_in_time is None:
            raise ValueError('restore_point_in_time must be provided')
        if target_resource_crn is None:
            raise ValueError('target_resource_crn must be provided')
        restore_point_in_time = datetime_to_string(restore_point_in_time)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_restore',
        )
        headers.update(sdk_headers)

        data = {
            'recovery_range_id': recovery_range_id,
            'restore_type': restore_type,
            'restore_point_in_time': restore_point_in_time,
            'target_resource_crn': target_resource_crn,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/restores'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_restores(
        self,
        backup_vault_name: str,
        *,
        token: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List Restores.

        List all current and complete restores.
        Requires that the user have `cloud-object-storage.backup_vault.list_restores`
        permission on the backup vault.

        :param str backup_vault_name: name of BackupVault to restore from.
        :param str token: (optional) the continuation token for controlling
               pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RestoreCollection` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_restores',
        )
        headers.update(sdk_headers)

        params = {
            'token': token,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name']
        path_param_values = self.encode_path_vars(backup_vault_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/restores'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_restore(
        self,
        backup_vault_name: str,
        restore_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Restore.

        Introspect on a specific restore.
        Requires that the user have `cloud-object-storage.backup_vault.get_restore`
        permission on the backup vault.

        :param str backup_vault_name: name of BackupVault that the restore occured
               on.
        :param str restore_id: id of the restore to introspect on.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Restore` object
        """

        if not backup_vault_name:
            raise ValueError('backup_vault_name must be provided')
        if not restore_id:
            raise ValueError('restore_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_restore',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_vault_name', 'restore_id']
        path_param_values = self.encode_path_vars(backup_vault_name, restore_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backup_vaults/{backup_vault_name}/restores/{restore_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
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


class BackupPolicy:
    """
    The current backup coverage for a COS Bucket.

    :param DeleteAfterDays initial_retention: The number of days to retain data
          within a RecoveryRange.
    :param str policy_name: The name granted to the policy. Validation :
            * chars limited to alphanumeric, underscore, hyphen and period.
    :param str target_backup_vault_crn: The CRN for a COS BackupVault.
    :param str backup_type: The type of backup to support. For LA+GA this is limited
          to "continuous".
    :param str policy_id: A UUID that uniquely identifies a resource.
    :param str policy_status: The current status of the backup policy.
          pending : the policy has been received and has begun processing. initializing :
          pre-existing objects are being sync to the backup vault. active : the policy is
          active and healthy. action_needed : the policy is unhealthy and requires some
          intervention to recover degraded : the policy is unhealthy failed : the policy
          has failed unrecoverably.
    :param float initial_sync_progress: (optional) Reports percent-doneness of init.
          Only present when policy_status=INITIALIZING/PENDING.
    :param str error_cause: (optional) reports error cause. Only present when
          policy_status=ERROR/FAILED.
    """

    def __init__(
        self,
        initial_retention: 'DeleteAfterDays',
        policy_name: str,
        target_backup_vault_crn: str,
        backup_type: str,
        policy_id: str,
        policy_status: str,
        *,
        initial_sync_progress: Optional[float] = None,
        error_cause: Optional[str] = None,
    ) -> None:
        """
        Initialize a BackupPolicy object.

        :param DeleteAfterDays initial_retention: The number of days to retain data
               within a RecoveryRange.
        :param str policy_name: The name granted to the policy. Validation :
                 * chars limited to alphanumeric, underscore, hyphen and period.
        :param str target_backup_vault_crn: The CRN for a COS BackupVault.
        :param str backup_type: The type of backup to support. For LA+GA this is
               limited to "continuous".
        :param str policy_id: A UUID that uniquely identifies a resource.
        :param str policy_status: The current status of the backup policy.
               pending : the policy has been received and has begun processing.
               initializing : pre-existing objects are being sync to the backup vault.
               active : the policy is active and healthy. action_needed : the policy is
               unhealthy and requires some intervention to recover degraded : the policy
               is unhealthy failed : the policy has failed unrecoverably.
        :param float initial_sync_progress: (optional) Reports percent-doneness of
               init. Only present when policy_status=INITIALIZING/PENDING.
        :param str error_cause: (optional) reports error cause. Only present when
               policy_status=ERROR/FAILED.
        """
        self.initial_retention = initial_retention
        self.policy_name = policy_name
        self.target_backup_vault_crn = target_backup_vault_crn
        self.backup_type = backup_type
        self.policy_id = policy_id
        self.policy_status = policy_status
        self.initial_sync_progress = initial_sync_progress
        self.error_cause = error_cause

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupPolicy':
        """Initialize a BackupPolicy object from a json dictionary."""
        args = {}
        if (initial_retention := _dict.get('initial_retention')) is not None:
            args['initial_retention'] = DeleteAfterDays.from_dict(initial_retention)
        else:
            raise ValueError('Required property \'initial_retention\' not present in BackupPolicy JSON')
        if (policy_name := _dict.get('policy_name')) is not None:
            args['policy_name'] = policy_name
        else:
            raise ValueError('Required property \'policy_name\' not present in BackupPolicy JSON')
        if (target_backup_vault_crn := _dict.get('target_backup_vault_crn')) is not None:
            args['target_backup_vault_crn'] = target_backup_vault_crn
        else:
            raise ValueError('Required property \'target_backup_vault_crn\' not present in BackupPolicy JSON')
        if (backup_type := _dict.get('backup_type')) is not None:
            args['backup_type'] = backup_type
        else:
            raise ValueError('Required property \'backup_type\' not present in BackupPolicy JSON')
        if (policy_id := _dict.get('policy_id')) is not None:
            args['policy_id'] = policy_id
        else:
            raise ValueError('Required property \'policy_id\' not present in BackupPolicy JSON')
        if (policy_status := _dict.get('policy_status')) is not None:
            args['policy_status'] = policy_status
        else:
            raise ValueError('Required property \'policy_status\' not present in BackupPolicy JSON')
        if (initial_sync_progress := _dict.get('initial_sync_progress')) is not None:
            args['initial_sync_progress'] = initial_sync_progress
        if (error_cause := _dict.get('error_cause')) is not None:
            args['error_cause'] = error_cause
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupPolicy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'initial_retention') and self.initial_retention is not None:
            if isinstance(self.initial_retention, dict):
                _dict['initial_retention'] = self.initial_retention
            else:
                _dict['initial_retention'] = self.initial_retention.to_dict()
        if hasattr(self, 'policy_name') and self.policy_name is not None:
            _dict['policy_name'] = self.policy_name
        if hasattr(self, 'target_backup_vault_crn') and self.target_backup_vault_crn is not None:
            _dict['target_backup_vault_crn'] = self.target_backup_vault_crn
        if hasattr(self, 'backup_type') and self.backup_type is not None:
            _dict['backup_type'] = self.backup_type
        if hasattr(self, 'policy_id') and self.policy_id is not None:
            _dict['policy_id'] = self.policy_id
        if hasattr(self, 'policy_status') and self.policy_status is not None:
            _dict['policy_status'] = self.policy_status
        if hasattr(self, 'initial_sync_progress') and self.initial_sync_progress is not None:
            _dict['initial_sync_progress'] = self.initial_sync_progress
        if hasattr(self, 'error_cause') and self.error_cause is not None:
            _dict['error_cause'] = self.error_cause
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupPolicy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupPolicy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupPolicy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class BackupTypeEnum(str, Enum):
        """
        The type of backup to support. For LA+GA this is limited to "continuous".
        """

        CONTINUOUS = 'continuous'


    class PolicyStatusEnum(str, Enum):
        """
        The current status of the backup policy.
        pending : the policy has been received and has begun processing. initializing :
        pre-existing objects are being sync to the backup vault. active : the policy is
        active and healthy. action_needed : the policy is unhealthy and requires some
        intervention to recover degraded : the policy is unhealthy failed : the policy has
        failed unrecoverably.
        """

        PENDING = 'pending'
        INITIALIZING = 'initializing'
        ACTIVE = 'active'
        ACTION_NEEDED = 'action_needed'
        DEGRADED = 'degraded'
        FAILED = 'failed'



class BackupPolicyCollection:
    """
    A collection of backup policies.

    :param List[BackupPolicy] backup_policies: A collection of backup policies.
    """

    def __init__(
        self,
        backup_policies: List['BackupPolicy'],
    ) -> None:
        """
        Initialize a BackupPolicyCollection object.

        :param List[BackupPolicy] backup_policies: A collection of backup policies.
        """
        self.backup_policies = backup_policies

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupPolicyCollection':
        """Initialize a BackupPolicyCollection object from a json dictionary."""
        args = {}
        if (backup_policies := _dict.get('backup_policies')) is not None:
            args['backup_policies'] = [BackupPolicy.from_dict(v) for v in backup_policies]
        else:
            raise ValueError('Required property \'backup_policies\' not present in BackupPolicyCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupPolicyCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'backup_policies') and self.backup_policies is not None:
            backup_policies_list = []
            for v in self.backup_policies:
                if isinstance(v, dict):
                    backup_policies_list.append(v)
                else:
                    backup_policies_list.append(v.to_dict())
            _dict['backup_policies'] = backup_policies_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupPolicyCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupPolicyCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupPolicyCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BackupVault:
    """
    Metadata associated with a backup vault.

    :param BackupVaultActivityTracking activity_tracking: (optional) Activity
          Tracking configuration. An empty object (`{}`) indicates no configuration, and
          no events will be sent (This is the same behavior as
          `{"management_events":false}`). Note that read/write events cannot be enabled,
          and events cannot be routed to a non-default Activity Tracker instance.
    :param BackupVaultMetricsMonitoring metrics_monitoring: (optional) Metrics
          Monitoring configuration. An empty object (`{}`) indicates no configuration, and
          no metrics will be collected (This is the same behavior as
          `{"usage_metrics_enabled":false}`). Note that request metrics cannot be enabled,
          and metrics cannot be routed to a non-default metrics router instance.
    :param str backup_vault_name: The name given to a Bucket.
          Bucket names must be between 3 and 63 characters long must be made of lowercase
          letters, numbers, dots (periods), and dashes (hyphens). Bucket names must begin
          and end with a lowercase letter or number. Bucket names canâ€t contain
          consecutive dots or dashes. Bucket names that resemble IP addresses are not
          allowed.
          Bucket and BackupVault names exist in a global namespace and therefore must be
          unique.
    :param str region: the region in which this backup-vault should be created
          within.
    :param str sse_kp_customer_root_key_crn: (optional) The CRN for a KeyProtect
          root key.
    :param str crn: (optional) The CRN for a COS BackupVault.
    :param str service_instance_crn: (optional) A COS ServiceInstance CRN.
    :param datetime time_created: (optional) creation time of the backup-vault.
          Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
    :param datetime time_updated: (optional) time of last update to the backup-vault
          Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
    :param int bytes_used: (optional) byte useage of the backup-vault. This should
          include all usage, including non-current versions. A maximum value is not
          defined.
    """

    def __init__(
        self,
        backup_vault_name: str,
        region: str,
        *,
        activity_tracking: Optional['BackupVaultActivityTracking'] = None,
        metrics_monitoring: Optional['BackupVaultMetricsMonitoring'] = None,
        sse_kp_customer_root_key_crn: Optional[str] = None,
        crn: Optional[str] = None,
        service_instance_crn: Optional[str] = None,
        time_created: Optional[datetime] = None,
        time_updated: Optional[datetime] = None,
        bytes_used: Optional[int] = None,
    ) -> None:
        """
        Initialize a BackupVault object.

        :param str backup_vault_name: The name given to a Bucket.
               Bucket names must be between 3 and 63 characters long must be made of
               lowercase letters, numbers, dots (periods), and dashes (hyphens). Bucket
               names must begin and end with a lowercase letter or number. Bucket names
               canâ€t contain consecutive dots or dashes. Bucket names that resemble IP
               addresses are not allowed.
               Bucket and BackupVault names exist in a global namespace and therefore must
               be unique.
        :param str region: the region in which this backup-vault should be created
               within.
        :param BackupVaultActivityTracking activity_tracking: (optional) Activity
               Tracking configuration. An empty object (`{}`) indicates no configuration,
               and no events will be sent (This is the same behavior as
               `{"management_events":false}`). Note that read/write events cannot be
               enabled, and events cannot be routed to a non-default Activity Tracker
               instance.
        :param BackupVaultMetricsMonitoring metrics_monitoring: (optional) Metrics
               Monitoring configuration. An empty object (`{}`) indicates no
               configuration, and no metrics will be collected (This is the same behavior
               as `{"usage_metrics_enabled":false}`). Note that request metrics cannot be
               enabled, and metrics cannot be routed to a non-default metrics router
               instance.
        :param str sse_kp_customer_root_key_crn: (optional) The CRN for a
               KeyProtect root key.
        :param str crn: (optional) The CRN for a COS BackupVault.
        :param str service_instance_crn: (optional) A COS ServiceInstance CRN.
        :param datetime time_created: (optional) creation time of the backup-vault.
               Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
        :param datetime time_updated: (optional) time of last update to the
               backup-vault Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
        :param int bytes_used: (optional) byte useage of the backup-vault. This
               should include all usage, including non-current versions. A maximum value
               is not defined.
        """
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring
        self.backup_vault_name = backup_vault_name
        self.region = region
        self.sse_kp_customer_root_key_crn = sse_kp_customer_root_key_crn
        self.crn = crn
        self.service_instance_crn = service_instance_crn
        self.time_created = time_created
        self.time_updated = time_updated
        self.bytes_used = bytes_used

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupVault':
        """Initialize a BackupVault object from a json dictionary."""
        args = {}
        if (activity_tracking := _dict.get('activity_tracking')) is not None:
            args['activity_tracking'] = BackupVaultActivityTracking.from_dict(activity_tracking)
        if (metrics_monitoring := _dict.get('metrics_monitoring')) is not None:
            args['metrics_monitoring'] = BackupVaultMetricsMonitoring.from_dict(metrics_monitoring)
        if (backup_vault_name := _dict.get('backup_vault_name')) is not None:
            args['backup_vault_name'] = backup_vault_name
        else:
            raise ValueError('Required property \'backup_vault_name\' not present in BackupVault JSON')
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        else:
            raise ValueError('Required property \'region\' not present in BackupVault JSON')
        if (sse_kp_customer_root_key_crn := _dict.get('sse_kp_customer_root_key_crn')) is not None:
            args['sse_kp_customer_root_key_crn'] = sse_kp_customer_root_key_crn
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        if (service_instance_crn := _dict.get('service_instance_crn')) is not None:
            args['service_instance_crn'] = service_instance_crn
        if (time_created := _dict.get('time_created')) is not None:
            args['time_created'] = string_to_datetime(time_created)
        if (time_updated := _dict.get('time_updated')) is not None:
            args['time_updated'] = string_to_datetime(time_updated)
        if (bytes_used := _dict.get('bytes_used')) is not None:
            args['bytes_used'] = bytes_used
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupVault object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        if hasattr(self, 'backup_vault_name') and self.backup_vault_name is not None:
            _dict['backup_vault_name'] = self.backup_vault_name
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'sse_kp_customer_root_key_crn') and self.sse_kp_customer_root_key_crn is not None:
            _dict['sse_kp_customer_root_key_crn'] = self.sse_kp_customer_root_key_crn
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'service_instance_crn') and self.service_instance_crn is not None:
            _dict['service_instance_crn'] = self.service_instance_crn
        if hasattr(self, 'time_created') and self.time_created is not None:
            _dict['time_created'] = datetime_to_string(self.time_created)
        if hasattr(self, 'time_updated') and self.time_updated is not None:
            _dict['time_updated'] = datetime_to_string(self.time_updated)
        if hasattr(self, 'bytes_used') and self.bytes_used is not None:
            _dict['bytes_used'] = self.bytes_used
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupVault object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupVault') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupVault') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BackupVaultActivityTracking:
    """
    Activity Tracking configuration. An empty object (`{}`) indicates no configuration,
    and no events will be sent (This is the same behavior as
    `{"management_events":false}`). Note that read/write events cannot be enabled, and
    events cannot be routed to a non-default Activity Tracker instance.

    :param bool management_events: (optional) Whether to send notifications for
          management events on the BackupVault.
    """

    def __init__(
        self,
        *,
        management_events: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BackupVaultActivityTracking object.

        :param bool management_events: (optional) Whether to send notifications for
               management events on the BackupVault.
        """
        self.management_events = management_events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupVaultActivityTracking':
        """Initialize a BackupVaultActivityTracking object from a json dictionary."""
        args = {}
        if (management_events := _dict.get('management_events')) is not None:
            args['management_events'] = management_events
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupVaultActivityTracking object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'management_events') and self.management_events is not None:
            _dict['management_events'] = self.management_events
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupVaultActivityTracking object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupVaultActivityTracking') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupVaultActivityTracking') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BackupVaultCollection:
    """
    A listing of backup vaults.

    :param NextPagination next: (optional) Pagination response body.
    :param List[str] backup_vaults: List of Backup Vaults. If no Backup Vaults
          exist, this array will be empty.
    """

    def __init__(
        self,
        backup_vaults: List[str],
        *,
        next: Optional['NextPagination'] = None,
    ) -> None:
        """
        Initialize a BackupVaultCollection object.

        :param List[str] backup_vaults: List of Backup Vaults. If no Backup Vaults
               exist, this array will be empty.
        :param NextPagination next: (optional) Pagination response body.
        """
        self.next = next
        self.backup_vaults = backup_vaults

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupVaultCollection':
        """Initialize a BackupVaultCollection object from a json dictionary."""
        args = {}
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPagination.from_dict(next)
        if (backup_vaults := _dict.get('backup_vaults')) is not None:
            args['backup_vaults'] = backup_vaults
        else:
            raise ValueError('Required property \'backup_vaults\' not present in BackupVaultCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupVaultCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'backup_vaults') and self.backup_vaults is not None:
            _dict['backup_vaults'] = self.backup_vaults
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupVaultCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupVaultCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupVaultCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BackupVaultMetricsMonitoring:
    """
    Metrics Monitoring configuration. An empty object (`{}`) indicates no configuration,
    and no metrics will be collected (This is the same behavior as
    `{"usage_metrics_enabled":false}`). Note that request metrics cannot be enabled, and
    metrics cannot be routed to a non-default metrics router instance.

    :param bool usage_metrics_enabled: (optional) Whether usage metrics are
          collected for this BackupVault.
    """

    def __init__(
        self,
        *,
        usage_metrics_enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BackupVaultMetricsMonitoring object.

        :param bool usage_metrics_enabled: (optional) Whether usage metrics are
               collected for this BackupVault.
        """
        self.usage_metrics_enabled = usage_metrics_enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupVaultMetricsMonitoring':
        """Initialize a BackupVaultMetricsMonitoring object from a json dictionary."""
        args = {}
        if (usage_metrics_enabled := _dict.get('usage_metrics_enabled')) is not None:
            args['usage_metrics_enabled'] = usage_metrics_enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupVaultMetricsMonitoring object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'usage_metrics_enabled') and self.usage_metrics_enabled is not None:
            _dict['usage_metrics_enabled'] = self.usage_metrics_enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupVaultMetricsMonitoring object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupVaultMetricsMonitoring') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupVaultMetricsMonitoring') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BackupVaultPatch:
    """
    Metadata elements on a backup vault that can be updated.

    :param BackupVaultActivityTracking activity_tracking: (optional) Activity
          Tracking configuration. An empty object (`{}`) indicates no configuration, and
          no events will be sent (This is the same behavior as
          `{"management_events":false}`). Note that read/write events cannot be enabled,
          and events cannot be routed to a non-default Activity Tracker instance.
    :param BackupVaultMetricsMonitoring metrics_monitoring: (optional) Metrics
          Monitoring configuration. An empty object (`{}`) indicates no configuration, and
          no metrics will be collected (This is the same behavior as
          `{"usage_metrics_enabled":false}`). Note that request metrics cannot be enabled,
          and metrics cannot be routed to a non-default metrics router instance.
    """

    def __init__(
        self,
        *,
        activity_tracking: Optional['BackupVaultActivityTracking'] = None,
        metrics_monitoring: Optional['BackupVaultMetricsMonitoring'] = None,
    ) -> None:
        """
        Initialize a BackupVaultPatch object.

        :param BackupVaultActivityTracking activity_tracking: (optional) Activity
               Tracking configuration. An empty object (`{}`) indicates no configuration,
               and no events will be sent (This is the same behavior as
               `{"management_events":false}`). Note that read/write events cannot be
               enabled, and events cannot be routed to a non-default Activity Tracker
               instance.
        :param BackupVaultMetricsMonitoring metrics_monitoring: (optional) Metrics
               Monitoring configuration. An empty object (`{}`) indicates no
               configuration, and no metrics will be collected (This is the same behavior
               as `{"usage_metrics_enabled":false}`). Note that request metrics cannot be
               enabled, and metrics cannot be routed to a non-default metrics router
               instance.
        """
        self.activity_tracking = activity_tracking
        self.metrics_monitoring = metrics_monitoring

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BackupVaultPatch':
        """Initialize a BackupVaultPatch object from a json dictionary."""
        args = {}
        if (activity_tracking := _dict.get('activity_tracking')) is not None:
            args['activity_tracking'] = BackupVaultActivityTracking.from_dict(activity_tracking)
        if (metrics_monitoring := _dict.get('metrics_monitoring')) is not None:
            args['metrics_monitoring'] = BackupVaultMetricsMonitoring.from_dict(metrics_monitoring)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BackupVaultPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BackupVaultPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BackupVaultPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BackupVaultPatch') -> bool:
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


class DeleteAfterDays:
    """
    The number of days to retain data within a RecoveryRange.

    :param int delete_after_days: (optional) The number of days to retain data
          within a RecoveryRange.
    """

    def __init__(
        self,
        *,
        delete_after_days: Optional[int] = None,
    ) -> None:
        """
        Initialize a DeleteAfterDays object.

        :param int delete_after_days: (optional) The number of days to retain data
               within a RecoveryRange.
        """
        self.delete_after_days = delete_after_days

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAfterDays':
        """Initialize a DeleteAfterDays object from a json dictionary."""
        args = {}
        if (delete_after_days := _dict.get('delete_after_days')) is not None:
            args['delete_after_days'] = delete_after_days
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAfterDays object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'delete_after_days') and self.delete_after_days is not None:
            _dict['delete_after_days'] = self.delete_after_days
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteAfterDays object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAfterDays') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAfterDays') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteAfterDaysWithIndefinite:
    """
    The retention configuration for a RecoveryRange.

    :param int delete_after_days: (optional) The number of days to retain data
          within a RecoveryRange. -1 is a special value that denotes "indefinite"
          retention. This value can only be set implicitly via a policy created during the
          LA release being upgraded to the GA release.
    """

    def __init__(
        self,
        *,
        delete_after_days: Optional[int] = None,
    ) -> None:
        """
        Initialize a DeleteAfterDaysWithIndefinite object.

        :param int delete_after_days: (optional) The number of days to retain data
               within a RecoveryRange. -1 is a special value that denotes "indefinite"
               retention. This value can only be set implicitly via a policy created
               during the LA release being upgraded to the GA release.
        """
        self.delete_after_days = delete_after_days

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAfterDaysWithIndefinite':
        """Initialize a DeleteAfterDaysWithIndefinite object from a json dictionary."""
        args = {}
        if (delete_after_days := _dict.get('delete_after_days')) is not None:
            args['delete_after_days'] = delete_after_days
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAfterDaysWithIndefinite object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'delete_after_days') and self.delete_after_days is not None:
            _dict['delete_after_days'] = self.delete_after_days
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteAfterDaysWithIndefinite object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAfterDaysWithIndefinite') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAfterDaysWithIndefinite') -> bool:
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


class NextPagination:
    """
    Pagination response body.

    :param str href: A URL to the continuation of results.
    :param str token: The continuation token utilized for paginated results.
    """

    def __init__(
        self,
        href: str,
        token: str,
    ) -> None:
        """
        Initialize a NextPagination object.

        :param str href: A URL to the continuation of results.
        :param str token: The continuation token utilized for paginated results.
        """
        self.href = href
        self.token = token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NextPagination':
        """Initialize a NextPagination object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in NextPagination JSON')
        if (token := _dict.get('token')) is not None:
            args['token'] = token
        else:
            raise ValueError('Required property \'token\' not present in NextPagination JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NextPagination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'token') and self.token is not None:
            _dict['token'] = self.token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NextPagination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NextPagination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NextPagination') -> bool:
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


class RecoveryRange:
    """
    Metadata associated with a recovery range.

    :param str source_resource_crn: (optional) The CRN for a COS Bucket.
          Note that Softlayer CRNs do not contain dashes within the service_instance_id,
          whereas regular CRNs do. Although bucket backup is not supported for softlayer
          accounts, this need not be enforced at the CRN parsing level.
    :param str backup_policy_name: (optional) The name granted to the policy.
          Validation :
            * chars limited to alphanumeric, underscore, hyphen and period.
    :param datetime range_start_time: (optional) The point in time at which backup
          coverage of the sourceResource begins.
          Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
    :param datetime range_end_time: (optional) the point in time at which backup
          coverage of the sourceResource ends. Returns "YYYY-MM-DDTHH:mm:ss.sssZ"
          timestamp format.
    :param datetime range_create_time: (optional) The time at which this
          recoveryRange was initially created.
          Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format
          NOTE : this can be before the start-time.
    :param DeleteAfterDaysWithIndefinite retention: (optional) The retention
          configuration for a RecoveryRange.
    :param str recovery_range_id: (optional) A UUID that uniquely identifies a
          resource.
    """

    def __init__(
        self,
        *,
        source_resource_crn: Optional[str] = None,
        backup_policy_name: Optional[str] = None,
        range_start_time: Optional[datetime] = None,
        range_end_time: Optional[datetime] = None,
        range_create_time: Optional[datetime] = None,
        retention: Optional['DeleteAfterDaysWithIndefinite'] = None,
        recovery_range_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a RecoveryRange object.

        :param str source_resource_crn: (optional) The CRN for a COS Bucket.
               Note that Softlayer CRNs do not contain dashes within the
               service_instance_id, whereas regular CRNs do. Although bucket backup is not
               supported for softlayer accounts, this need not be enforced at the CRN
               parsing level.
        :param str backup_policy_name: (optional) The name granted to the policy.
               Validation :
                 * chars limited to alphanumeric, underscore, hyphen and period.
        :param datetime range_start_time: (optional) The point in time at which
               backup coverage of the sourceResource begins.
               Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
        :param datetime range_end_time: (optional) the point in time at which
               backup coverage of the sourceResource ends. Returns
               "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
        :param datetime range_create_time: (optional) The time at which this
               recoveryRange was initially created.
               Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format
               NOTE : this can be before the start-time.
        :param DeleteAfterDaysWithIndefinite retention: (optional) The retention
               configuration for a RecoveryRange.
        :param str recovery_range_id: (optional) A UUID that uniquely identifies a
               resource.
        """
        self.source_resource_crn = source_resource_crn
        self.backup_policy_name = backup_policy_name
        self.range_start_time = range_start_time
        self.range_end_time = range_end_time
        self.range_create_time = range_create_time
        self.retention = retention
        self.recovery_range_id = recovery_range_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecoveryRange':
        """Initialize a RecoveryRange object from a json dictionary."""
        args = {}
        if (source_resource_crn := _dict.get('source_resource_crn')) is not None:
            args['source_resource_crn'] = source_resource_crn
        if (backup_policy_name := _dict.get('backup_policy_name')) is not None:
            args['backup_policy_name'] = backup_policy_name
        if (range_start_time := _dict.get('range_start_time')) is not None:
            args['range_start_time'] = string_to_datetime(range_start_time)
        if (range_end_time := _dict.get('range_end_time')) is not None:
            args['range_end_time'] = string_to_datetime(range_end_time)
        if (range_create_time := _dict.get('range_create_time')) is not None:
            args['range_create_time'] = string_to_datetime(range_create_time)
        if (retention := _dict.get('retention')) is not None:
            args['retention'] = DeleteAfterDaysWithIndefinite.from_dict(retention)
        if (recovery_range_id := _dict.get('recovery_range_id')) is not None:
            args['recovery_range_id'] = recovery_range_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecoveryRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source_resource_crn') and self.source_resource_crn is not None:
            _dict['source_resource_crn'] = self.source_resource_crn
        if hasattr(self, 'backup_policy_name') and self.backup_policy_name is not None:
            _dict['backup_policy_name'] = self.backup_policy_name
        if hasattr(self, 'range_start_time') and self.range_start_time is not None:
            _dict['range_start_time'] = datetime_to_string(self.range_start_time)
        if hasattr(self, 'range_end_time') and self.range_end_time is not None:
            _dict['range_end_time'] = datetime_to_string(self.range_end_time)
        if hasattr(self, 'range_create_time') and self.range_create_time is not None:
            _dict['range_create_time'] = datetime_to_string(self.range_create_time)
        if hasattr(self, 'retention') and self.retention is not None:
            if isinstance(self.retention, dict):
                _dict['retention'] = self.retention
            else:
                _dict['retention'] = self.retention.to_dict()
        if hasattr(self, 'recovery_range_id') and self.recovery_range_id is not None:
            _dict['recovery_range_id'] = self.recovery_range_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecoveryRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecoveryRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecoveryRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecoveryRangeCollection:
    """
    A collection of recovery ranges.

    :param NextPagination next: (optional) Pagination response body.
    :param List[RecoveryRange] recovery_ranges: A list of recovery ranges.
    """

    def __init__(
        self,
        recovery_ranges: List['RecoveryRange'],
        *,
        next: Optional['NextPagination'] = None,
    ) -> None:
        """
        Initialize a RecoveryRangeCollection object.

        :param List[RecoveryRange] recovery_ranges: A list of recovery ranges.
        :param NextPagination next: (optional) Pagination response body.
        """
        self.next = next
        self.recovery_ranges = recovery_ranges

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecoveryRangeCollection':
        """Initialize a RecoveryRangeCollection object from a json dictionary."""
        args = {}
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPagination.from_dict(next)
        if (recovery_ranges := _dict.get('recovery_ranges')) is not None:
            args['recovery_ranges'] = [RecoveryRange.from_dict(v) for v in recovery_ranges]
        else:
            raise ValueError('Required property \'recovery_ranges\' not present in RecoveryRangeCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecoveryRangeCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'recovery_ranges') and self.recovery_ranges is not None:
            recovery_ranges_list = []
            for v in self.recovery_ranges:
                if isinstance(v, dict):
                    recovery_ranges_list.append(v)
                else:
                    recovery_ranges_list.append(v.to_dict())
            _dict['recovery_ranges'] = recovery_ranges_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecoveryRangeCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecoveryRangeCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecoveryRangeCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecoveryRangePatch:
    """
    The retention configuration for a RecoveryRange.

    :param DeleteAfterDays retention: (optional) The number of days to retain data
          within a RecoveryRange.
    """

    def __init__(
        self,
        *,
        retention: Optional['DeleteAfterDays'] = None,
    ) -> None:
        """
        Initialize a RecoveryRangePatch object.

        :param DeleteAfterDays retention: (optional) The number of days to retain
               data within a RecoveryRange.
        """
        self.retention = retention

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecoveryRangePatch':
        """Initialize a RecoveryRangePatch object from a json dictionary."""
        args = {}
        if (retention := _dict.get('retention')) is not None:
            args['retention'] = DeleteAfterDays.from_dict(retention)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecoveryRangePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'retention') and self.retention is not None:
            if isinstance(self.retention, dict):
                _dict['retention'] = self.retention
            else:
                _dict['retention'] = self.retention.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecoveryRangePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecoveryRangePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecoveryRangePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Restore:
    """
    Metadata associated with a requested restore operation.

    :param str recovery_range_id: A UUID that uniquely identifies a resource.
    :param str restore_type: The type of restore to support. More options will be
          available in the future.
    :param datetime restore_point_in_time: Timestamp format used throughout the API.
          Accepts the following formats:
          YYYY-MM-DDTHH:mm:ssZ YYYY-MM-DDTHH:mm:ss YYYY-MM-DDTHH:mm:ss-hh:mm
          YYYY-MM-DDTHH:mm:ss+hh:mm YYYY-MM-DDTHH:mm:ss.sssZ YYYY-MM-DDTHH:mm:ss.sss
          YYYY-MM-DDTHH:mm:ss.sss-hh:mm YYYY-MM-DDTHH:mm:ss.sss+hh:mm.
    :param str target_resource_crn: The CRN for a COS Bucket.
          Note that Softlayer CRNs do not contain dashes within the service_instance_id,
          whereas regular CRNs do. Although bucket backup is not supported for softlayer
          accounts, this need not be enforced at the CRN parsing level.
    :param str source_resource_crn: (optional) The CRN for a COS Bucket.
          Note that Softlayer CRNs do not contain dashes within the service_instance_id,
          whereas regular CRNs do. Although bucket backup is not supported for softlayer
          accounts, this need not be enforced at the CRN parsing level.
    :param str restore_id: (optional) A UUID that uniquely identifies a resource.
    :param str restore_status: (optional) The current status for this restore
          operation.
          initializing: The operation is initializing. Do not expect to see restored
          objects on the target bucket.  running : The operation is ongoing. Expect to see
          some restored objects on the target bucket.  complete: The operation has
          completed successfully.  failed: The operation has completed unsuccessfully.
    :param datetime init_time: (optional) The time at which this restore was
          initiated Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
    :param datetime complete_time: (optional) The time at which this restore ended
          (in both success and error cases) Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp
          format.
    :param int restore_percent_progress: (optional) reports percent-doneness of
          init. Only present when restore_status=running.
    :param str error_cause: (optional) Only present when restore_status=running.
    """

    def __init__(
        self,
        recovery_range_id: str,
        restore_type: str,
        restore_point_in_time: datetime,
        target_resource_crn: str,
        *,
        source_resource_crn: Optional[str] = None,
        restore_id: Optional[str] = None,
        restore_status: Optional[str] = None,
        init_time: Optional[datetime] = None,
        complete_time: Optional[datetime] = None,
        restore_percent_progress: Optional[int] = None,
        error_cause: Optional[str] = None,
    ) -> None:
        """
        Initialize a Restore object.

        :param str recovery_range_id: A UUID that uniquely identifies a resource.
        :param str restore_type: The type of restore to support. More options will
               be available in the future.
        :param datetime restore_point_in_time: Timestamp format used throughout the
               API.
               Accepts the following formats:
               YYYY-MM-DDTHH:mm:ssZ YYYY-MM-DDTHH:mm:ss YYYY-MM-DDTHH:mm:ss-hh:mm
               YYYY-MM-DDTHH:mm:ss+hh:mm YYYY-MM-DDTHH:mm:ss.sssZ YYYY-MM-DDTHH:mm:ss.sss
               YYYY-MM-DDTHH:mm:ss.sss-hh:mm YYYY-MM-DDTHH:mm:ss.sss+hh:mm.
        :param str target_resource_crn: The CRN for a COS Bucket.
               Note that Softlayer CRNs do not contain dashes within the
               service_instance_id, whereas regular CRNs do. Although bucket backup is not
               supported for softlayer accounts, this need not be enforced at the CRN
               parsing level.
        :param str source_resource_crn: (optional) The CRN for a COS Bucket.
               Note that Softlayer CRNs do not contain dashes within the
               service_instance_id, whereas regular CRNs do. Although bucket backup is not
               supported for softlayer accounts, this need not be enforced at the CRN
               parsing level.
        :param str restore_id: (optional) A UUID that uniquely identifies a
               resource.
        :param str restore_status: (optional) The current status for this restore
               operation.
               initializing: The operation is initializing. Do not expect to see restored
               objects on the target bucket.  running : The operation is ongoing. Expect
               to see some restored objects on the target bucket.  complete: The operation
               has completed successfully.  failed: The operation has completed
               unsuccessfully.
        :param datetime init_time: (optional) The time at which this restore was
               initiated Returns "YYYY-MM-DDTHH:mm:ss.sssZ" timestamp format.
        :param datetime complete_time: (optional) The time at which this restore
               ended (in both success and error cases) Returns "YYYY-MM-DDTHH:mm:ss.sssZ"
               timestamp format.
        :param int restore_percent_progress: (optional) reports percent-doneness of
               init. Only present when restore_status=running.
        :param str error_cause: (optional) Only present when
               restore_status=running.
        """
        self.recovery_range_id = recovery_range_id
        self.restore_type = restore_type
        self.restore_point_in_time = restore_point_in_time
        self.target_resource_crn = target_resource_crn
        self.source_resource_crn = source_resource_crn
        self.restore_id = restore_id
        self.restore_status = restore_status
        self.init_time = init_time
        self.complete_time = complete_time
        self.restore_percent_progress = restore_percent_progress
        self.error_cause = error_cause

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Restore':
        """Initialize a Restore object from a json dictionary."""
        args = {}
        if (recovery_range_id := _dict.get('recovery_range_id')) is not None:
            args['recovery_range_id'] = recovery_range_id
        else:
            raise ValueError('Required property \'recovery_range_id\' not present in Restore JSON')
        if (restore_type := _dict.get('restore_type')) is not None:
            args['restore_type'] = restore_type
        else:
            raise ValueError('Required property \'restore_type\' not present in Restore JSON')
        if (restore_point_in_time := _dict.get('restore_point_in_time')) is not None:
            args['restore_point_in_time'] = string_to_datetime(restore_point_in_time)
        else:
            raise ValueError('Required property \'restore_point_in_time\' not present in Restore JSON')
        if (target_resource_crn := _dict.get('target_resource_crn')) is not None:
            args['target_resource_crn'] = target_resource_crn
        else:
            raise ValueError('Required property \'target_resource_crn\' not present in Restore JSON')
        if (source_resource_crn := _dict.get('source_resource_crn')) is not None:
            args['source_resource_crn'] = source_resource_crn
        if (restore_id := _dict.get('restore_id')) is not None:
            args['restore_id'] = restore_id
        if (restore_status := _dict.get('restore_status')) is not None:
            args['restore_status'] = restore_status
        if (init_time := _dict.get('init_time')) is not None:
            args['init_time'] = string_to_datetime(init_time)
        if (complete_time := _dict.get('complete_time')) is not None:
            args['complete_time'] = string_to_datetime(complete_time)
        if (restore_percent_progress := _dict.get('restore_percent_progress')) is not None:
            args['restore_percent_progress'] = restore_percent_progress
        if (error_cause := _dict.get('error_cause')) is not None:
            args['error_cause'] = error_cause
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Restore object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'recovery_range_id') and self.recovery_range_id is not None:
            _dict['recovery_range_id'] = self.recovery_range_id
        if hasattr(self, 'restore_type') and self.restore_type is not None:
            _dict['restore_type'] = self.restore_type
        if hasattr(self, 'restore_point_in_time') and self.restore_point_in_time is not None:
            _dict['restore_point_in_time'] = datetime_to_string(self.restore_point_in_time)
        if hasattr(self, 'target_resource_crn') and self.target_resource_crn is not None:
            _dict['target_resource_crn'] = self.target_resource_crn
        if hasattr(self, 'source_resource_crn') and self.source_resource_crn is not None:
            _dict['source_resource_crn'] = self.source_resource_crn
        if hasattr(self, 'restore_id') and self.restore_id is not None:
            _dict['restore_id'] = self.restore_id
        if hasattr(self, 'restore_status') and self.restore_status is not None:
            _dict['restore_status'] = self.restore_status
        if hasattr(self, 'init_time') and self.init_time is not None:
            _dict['init_time'] = datetime_to_string(self.init_time)
        if hasattr(self, 'complete_time') and self.complete_time is not None:
            _dict['complete_time'] = datetime_to_string(self.complete_time)
        if hasattr(self, 'restore_percent_progress') and self.restore_percent_progress is not None:
            _dict['restore_percent_progress'] = self.restore_percent_progress
        if hasattr(self, 'error_cause') and self.error_cause is not None:
            _dict['error_cause'] = self.error_cause
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Restore object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Restore') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Restore') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RestoreTypeEnum(str, Enum):
        """
        The type of restore to support. More options will be available in the future.
        """

        IN_PLACE = 'in_place'


    class RestoreStatusEnum(str, Enum):
        """
        The current status for this restore operation.
        initializing: The operation is initializing. Do not expect to see restored objects
        on the target bucket.  running : The operation is ongoing. Expect to see some
        restored objects on the target bucket.  complete: The operation has completed
        successfully.  failed: The operation has completed unsuccessfully.
        """

        INITIALIZING = 'initializing'
        RUNNING = 'running'
        COMPLETE = 'complete'
        FAILED = 'failed'



class RestoreCollection:
    """
    A list of restore operations.

    :param NextPagination next: (optional) Pagination response body.
    :param List[Restore] restores: A collection of active and completed restore
          operations.
    """

    def __init__(
        self,
        restores: List['Restore'],
        *,
        next: Optional['NextPagination'] = None,
    ) -> None:
        """
        Initialize a RestoreCollection object.

        :param List[Restore] restores: A collection of active and completed restore
               operations.
        :param NextPagination next: (optional) Pagination response body.
        """
        self.next = next
        self.restores = restores

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RestoreCollection':
        """Initialize a RestoreCollection object from a json dictionary."""
        args = {}
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPagination.from_dict(next)
        if (restores := _dict.get('restores')) is not None:
            args['restores'] = [Restore.from_dict(v) for v in restores]
        else:
            raise ValueError('Required property \'restores\' not present in RestoreCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RestoreCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'restores') and self.restores is not None:
            restores_list = []
            for v in self.restores:
                if isinstance(v, dict):
                    restores_list.append(v)
                else:
                    restores_list.append(v.to_dict())
            _dict['restores'] = restores_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RestoreCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RestoreCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RestoreCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################


class BackupVaultsPager:
    """
    BackupVaultsPager can be used to simplify the use of the "list_backup_vaults" method.
    """

    def __init__(
        self,
        *,
        client: ResourceConfigurationV1,
        service_instance_id: str,
    ) -> None:
        """
        Initialize a BackupVaultsPager object.
        :param str service_instance_id: Name of the service_instance to list
               BackupVaults for.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._service_instance_id = service_instance_id

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of .
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_backup_vaults(
            service_instance_id=self._service_instance_id,
            token=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('token')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('backup_vaults')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of .
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class RecoveryRangesPager:
    """
    RecoveryRangesPager can be used to simplify the use of the "list_recovery_ranges" method.
    """

    def __init__(
        self,
        *,
        client: ResourceConfigurationV1,
        backup_vault_name: str,
        source_resource_crn: str = None,
        latest: str = None,
    ) -> None:
        """
        Initialize a RecoveryRangesPager object.
        :param str backup_vault_name: name of BackupVault.
        :param str source_resource_crn: (optional) CRN of source resource to filter
               on. This limits ranges returned to only ranges where the
               source_resource_crn matches the parameter value.
        :param str latest: (optional) If "true", then return only the latest
               RecoveryRange for each source-resource that is backed up.
               If "false" or not specified, then the default behavior is produced.
               Value is can insensative. If any value is provided other than "true" or
               "false" then return 400.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._backup_vault_name = backup_vault_name
        self._source_resource_crn = source_resource_crn
        self._latest = latest

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of RecoveryRange.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_recovery_ranges(
            backup_vault_name=self._backup_vault_name,
            source_resource_crn=self._source_resource_crn,
            latest=self._latest,
            token=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('token')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('recovery_ranges')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of RecoveryRange.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class RestoresPager:
    """
    RestoresPager can be used to simplify the use of the "list_restores" method.
    """

    def __init__(
        self,
        *,
        client: ResourceConfigurationV1,
        backup_vault_name: str,
    ) -> None:
        """
        Initialize a RestoresPager object.
        :param str backup_vault_name: name of BackupVault to restore from.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._backup_vault_name = backup_vault_name

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Restore.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_restores(
            backup_vault_name=self._backup_vault_name,
            token=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('token')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('restores')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Restore.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
