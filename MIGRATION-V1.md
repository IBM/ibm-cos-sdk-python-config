# Migration Guide - upgrading to ibm-cos-sdk-config@2.0.0

- [Breaking Changes](#breaking-changes)
  - [Changes in Package Imports](#changes-in-package-imports)
  - [Changes in Create Client](#changes-in-create-client)
  - [Changes in API methods and updating bucket configuration](#changes-in-api-methods-and-updating-bucket-configuration)
  - [Change in Agent Name](#change-in-agent-name)

## Breaking changes

### Changes in Package Imports

```js
=====================================================================================================================================================================
|                                 Current                                  |                                        New                                             |
=====================================================================================================================================================================
| from cos_config import resource_configuration_v1.ResourceConfigurationV1 | from ibm_cos_sdk_config import resource_configuration_v1.ResourceConfigurationV1       |
|                                                                          | from ibm_cloud_sdk_core.authenticators import IAMAuthenticator                         |
```

### Changes in Create Client

Credentials are no longer passed in as constructor parameters. Rather, a single `authenticator` is instantiated and passed in to the constructor.

Example:

#### Using API Key -

```js
=====================================================================================================================================================================
|                                 Current                                  |                                        New                                             |
=====================================================================================================================================================================
|                                                                          | authenticator = IAMAuthenticator(                                                      |
|                                                                          |   apikey="api_key"                                                                     |
|                                                                          |   url="iam_auth_url"                                                                   |
|                                                                          | )                                                                                      |
|                                                                          |                                                                                        |
| rcConfig = ResourceConfigurationV1(                                      | rcConfig = ResourceConfigurationV1(                                                    |
|   iam_apikey: "iam_api_key",                                             |   authenticator=authenticator                                                          |
|   iam_auth_url: "iam_auth_url",                                          | )                                                                                      |
|   iam_rc_endpoint_url: "iam_rc_endpoint_url",                            | rcConfig.set_service_url("iam_rc_endpoint_url")                                        |
| )                                                                        |                                                                                        |

```

### Changes in API methods and updating bucket configuration

- Creating API objects

    Activity-Tracking

    ```js
    =======================================================================================================================================================
    |                                 Current                             |                                  New                                    |
    =======================================================================================================================================================
    | activity_tracking = {"read_data_events": False/True,                | bucket_patch = {'activity_tracking': {"read_data_events": False/True,   |
    |                      "write_data_events": False/True,               |                                       "write_data_events": False/True,  |
    |                      "activity_tracker_crn": activity_tracker_crn}  |                                       "activity_tracker_crn": CRN}}     |
    |                                                                     |                                                                         |
    | rcConfig.update_bucket_config(bucket_name, activity_tracking)       | rcConfig.update_bucket_config(bucket_name, bucket_patch)                |
    ```

    Metrics-Monitoring

    ```js
    ========================================================================================================================================================================
    |                               Current                                    |                                           New                                             |
    ========================================================================================================================================================================
    | metrics_monitoring = {"metrics_monitoring_crn": metrics_monitoring_crn,  | bucket_patch = {'metrics_monitoring': {"metrics_monitoring_crn": metrics_monitoring_crn,  |
    |                       "usage_metrics_enabled": False/True,               |                                        "usage_metrics_enabled": False/True,               |
    |                       "request_metrics_enabled": False/True}             |                                        "request_metrics_enabled": False/True}}            |
    |                                                                          |                                                                                           |
    | rcConfig.update_bucket_config(bucket_name, activity_tracking)            | rcConfig.update_bucket_config(bucket_name, bucket_patch)                                  |
    ```

    Firewall

    ```js
    =====================================================================================================================
    |                        Current                        |                           New                             |
    =====================================================================================================================
    | firewall = {"allowed_ip": [ip-list]}                  | bucket_patch = {'firewall': {"allowed_ip": [ip-list]}}    |
    |                                                       |                                                           |
    | rcConfig.update_bucket_config(bucket_name, firewall)  | rcConfig.update_bucket_config(bucket_name, bucket_patch)  |
    ```

    Hard-Quota

    ```js
    =======================================================================================================================
    |                        Current                          |                           New                             |
    =======================================================================================================================
    | hard_quota = 1024                                       | bucket_patch = {'hard_quota': 1024}                       |
    |                                                         |                                                           |
    | rcConfig.update_bucket_config(bucket_name, hard_quota)  | rcConfig.update_bucket_config(bucket_name, bucket_patch)  |
    ```

### Change in Agent Name

```js
    ibm-cos-resource-config-sdk-python --> ibm-cos-sdk-python-config 
```

This issue will be used to track features and changes we want to make in the next major release of this package.
