# IBM COS Resource Configuration SDK for Python

This package allows Python developers to write software that interacts with the Resource Configuration API for [IBM Cloud Object Storage](https://cloud.ibm.com/apidocs/cos/cos-configuration).

## Notice

IBM has added a [Language Support Policy](#language-support-policy). Language versions will be deprecated on the published schedule without additional notice.

## Documentation

* [Core documentation for IBM COS](https://cloud.ibm.com/docs/services/cloud-object-storage/getting-started.html)
* [REST API Reference and Code Examples](https://cloud.ibm.com/apidocs/cos/cos-configuration)
* [Python Resource Configuration API reference documentation](https://ibm.github.io/ibm-cos-sdk-python-config)

For release notes, see the [CHANGELOG](CHANGELOG.md).

## Quick start

You will need:

* An instance of COS.
* An API key from [IBM Cloud Identity and Access Management](https://cloud.ibm.com/docs/iam/users_roles.html).

These values can be found in the IBM Cloud Console by [generating a 'service credential'](https://cloud.ibm.com/docs/services/cloud-object-storage/iam/service-credentials.html).

## Getting the SDK

The preferred way to install the IBM COS Resource Configuration SDK for Python is to use the [pip](https://pypi.org/project/pip/) package manager. Simply type the following into a terminal window:

```sh
pip install ibm-cos-sdk-config
```

## Getting Help

Feel free to use GitHub issues for tracking bugs and feature requests, but for help please use one of the following resources:

* Read a quick start guide in [IBM Cloud Docs](https://cloud.ibm.com/docs/services/cloud-object-storage/).
* Ask a question on [Stack Overflow](https://stackoverflow.com/) and tag it with ``ibm`` and ``object-storage``.
* Open a support ticket with [IBM Cloud Support](https://cloud.ibm.com/unifiedsupport/supportcenter)
* If it turns out that you may have found a bug, please [open an issue](https://github.com/ibm/ibm-cos-sdk-python-config/issues/new).

## Language Support Policy

IBM supports [current public releases](https://devguide.python.org/#status-of-python-branches). IBM will deprecate language versions 90 days after a version reaches end-of-life. All clients will need to upgrade to a supported version before the end of the grace period.

## License

This SDK is distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
