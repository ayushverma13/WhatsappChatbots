# openapi_client.6BanApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_test**](6BanApi.md#ban_test) | **POST** /banTest | Test ban settings
[**get_ban_settings**](6BanApi.md#get_ban_settings) | **GET** /banSettings | Get settings
[**set_ban_settings**](6BanApi.md#set_ban_settings) | **POST** /banSettings | Set settings


# **ban_test**
> ban_test_status.BanTestStatus ban_test(ban_test_action_ban_test_action)

Test ban settings

Send the phone number to find out if the instance is banning it

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
    api_instance = openapi_client.6BanApi(api_client)
    ban_test_action_ban_test_action = openapi_client.BanTestAction() # ban_test_action.BanTestAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Test ban settings
        api_response = api_instance.ban_test(ban_test_action_ban_test_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 6BanApi->ban_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ban_test_action_ban_test_action** | [**ban_test_action.BanTestAction**](BanTestAction.md)|  |

### Return type

[**ban_test_status.BanTestStatus**](BanTestStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ban_settings**
> ban_settings.BanSettings get_ban_settings()

Get settings

**banPhoneMask** - Regular expression on which bans on numbers will be sent  **preBanMessage** - Warning message If it is set, a message will be sent before sending the ban.

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
    api_instance = openapi_client.6BanApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get settings
        api_response = api_instance.get_ban_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 6BanApi->get_ban_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ban_settings.BanSettings**](BanSettings.md)

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

# **set_ban_settings**
> ban_settings.BanSettings set_ban_settings(ban_settings_ban_settings)

Set settings

**banPhoneMask** - Regular expression on which bans on numbers will be sent  **preBanMessage** - Warning message If it is set, a message will be sent before sending the ban.

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
    api_instance = openapi_client.6BanApi(api_client)
    ban_settings_ban_settings = openapi_client.BanSettings() # ban_settings.BanSettings | 
    
    # example passing only required values which don't have defaults set
    try:
        # Set settings
        api_response = api_instance.set_ban_settings(ban_settings_ban_settings)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 6BanApi->set_ban_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ban_settings_ban_settings** | [**ban_settings.BanSettings**](BanSettings.md)|  |

### Return type

[**ban_settings.BanSettings**](BanSettings.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

