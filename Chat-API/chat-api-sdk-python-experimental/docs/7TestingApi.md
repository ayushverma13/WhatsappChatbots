# openapi_client.7TestingApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_statuses**](7TestingApi.md#instance_statuses) | **GET** /instanceStatuses | Returns instance status changes history.
[**webhook_statuses**](7TestingApi.md#webhook_statuses) | **GET** /webhookStatus | Returns webhook status for message.


# **instance_statuses**
> statuses.Statuses instance_statuses()

Returns instance status changes history.

Requires enable \"instanceStatuses\" option for collecting data.

### Example

* Api Key Authentication (instanceId):
* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: instanceId
configuration.api_key['instanceId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['instanceId'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Defining host is optional and default to https://api.chat-api.com
configuration.host = "https://api.chat-api.com"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.7TestingApi(api_client)
    min_time = 946684800 # int | Filter statuses received after specified date. Example: 946684800. (optional)
max_time = 946684800 # int | Filter statuses received before specified date. Example: 946684800. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns instance status changes history.
        api_response = api_instance.instance_statuses(min_time=min_time, max_time=max_time)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 7TestingApi->instance_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_time** | **int**| Filter statuses received after specified date. Example: 946684800. | [optional]
 **max_time** | **int**| Filter statuses received before specified date. Example: 946684800. | [optional]

### Return type

[**statuses.Statuses**](Statuses.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_statuses**
> webhook_status.WebhookStatus webhook_statuses(msg_id)

Returns webhook status for message.

Requires enable \"webhookStatuses\" option for collecting data.

### Example

* Api Key Authentication (instanceId):
* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: instanceId
configuration.api_key['instanceId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['instanceId'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Defining host is optional and default to https://api.chat-api.com
configuration.host = "https://api.chat-api.com"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.7TestingApi(api_client)
    msg_id = 'false_17472822486@c.us_DF38E6A25B42CC8CCE57EC40F' # str | Message ID. Example: false_17472822486@c.us_DF38E6A25B42CC8CCE57EC40F.
    
    # example passing only required values which don't have defaults set
    try:
        # Returns webhook status for message.
        api_response = api_instance.webhook_statuses(msg_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 7TestingApi->webhook_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Message ID. Example: false_17472822486@c.us_DF38E6A25B42CC8CCE57EC40F. |

### Return type

[**webhook_status.WebhookStatus**](WebhookStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

