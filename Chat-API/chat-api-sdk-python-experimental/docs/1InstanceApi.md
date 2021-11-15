# openapi_client.1InstanceApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expiry**](1InstanceApi.md#expiry) | **POST** /expiry | Updates the QR code after its expired
[**get_qr_code**](1InstanceApi.md#get_qr_code) | **GET** /qr_code | Direct link to QR-code in the form of an image, not base64.
[**get_settings**](1InstanceApi.md#get_settings) | **GET** /settings | Get settings
[**get_status**](1InstanceApi.md#get_status) | **GET** /status | Get the account status and QR code for authorization.
[**logout**](1InstanceApi.md#logout) | **POST** /logout | Logout from WhatsApp Web to get new QR code.
[**reboot**](1InstanceApi.md#reboot) | **POST** /reboot | Reboot your whatsapp instance.
[**retry**](1InstanceApi.md#retry) | **POST** /retry | Repeat the manual synchronization attempt with the device
[**set_settings**](1InstanceApi.md#set_settings) | **POST** /settings | Set settings
[**takeover**](1InstanceApi.md#takeover) | **POST** /takeover | Returns the active session if the device has connected another instance of Web WhatsApp


# **expiry**
> inline_response2002.InlineResponse2002 expiry()

Updates the QR code after its expired

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Updates the QR code after its expired
        api_response = api_instance.expiry()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->expiry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**inline_response2002.InlineResponse2002**](InlineResponse2002.md)

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

# **get_qr_code**
> file_type get_qr_code()

Direct link to QR-code in the form of an image, not base64.

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Direct link to QR-code in the form of an image, not base64.
        api_response = api_instance.get_qr_code()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->get_qr_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QR code image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> settings.Settings get_settings()

Get settings

**webhookUrl** - Http or https URL for receiving notifications. For testing, we recommend using [our RequestBin](http://bin.chat-api.com).  **ackNotificationsOn** - Turn on/off ack (message delivered and message viewed) notifications in webhooks. GET method works for the same address.  **chatUpdateOn** - Turn on/off chat update notifications in webhooks. GET method works for the same address.  **videoUploadOn** - Turn on/off receiving video messages.  **proxy** - Socks5 IP address and port proxy for instance.  **guaranteedHooks** - Guarantee webhook delivery. Each webhook will make 20 attempts to send until it receives 200 status from the server.  **ignoreOldMessages** - Do not send webhooks with old messages during authorization.  **processArchive** - Process messages from archived chats.  **instanceStatuses** - Turn on/off collecting instance status changing history.  **webhookStatuses** - Turn on/off collecting messages webhooks statuses.  **statusNotificationsOn** - Turn on/off instance changind status notifications in webhooks.

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get settings
        api_response = api_instance.get_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**settings.Settings**](Settings.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |
**401** | Invalid token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> instance_status.InstanceStatus get_status()

Get the account status and QR code for authorization.

Reauthorization is necessary only in case of changing the device or manually pressing \"Logout on all devices\" on the phone. Keep the WhastsApp application open during authorization.  Instance statuses:  **authenticated** -  Authorization passed successfully  **init** -  Initial status   **loading** -  The system is still loading, try again in 1 minute   **got qr code** -  There is a QR code and you need to take a picture of it in the Whatsapp application by going to Menu -> WhatsApp Web -> Add. QR code is valid for one minute.   [Example showing base64 images on a page.](https://stackoverflow.com/questions/31526085/how-to-encode-an-image-into-an-html-file)  Manually easier to get [QR-code as an image](/#getQRCode)    When you request the status of the instance in standby mode (status **\"init\"**), it will automatically turn on. To avoid this behavior, use the **no_wakeup** parameter

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
    api_instance = openapi_client.1InstanceApi(api_client)
    full = False # bool | Get full information on the current status (optional) if omitted the server will use the default value of False
no_wakeup = False # bool | Ignore autowakeup (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the account status and QR code for authorization.
        api_response = api_instance.get_status(full=full, no_wakeup=no_wakeup)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **bool**| Get full information on the current status | [optional] if omitted the server will use the default value of False
 **no_wakeup** | **bool**| Ignore autowakeup | [optional] if omitted the server will use the default value of False

### Return type

[**instance_status.InstanceStatus**](InstanceStatus.md)

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

# **logout**
> inline_response200.InlineResponse200 logout()

Logout from WhatsApp Web to get new QR code.

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Logout from WhatsApp Web to get new QR code.
        api_response = api_instance.logout()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**inline_response200.InlineResponse200**](InlineResponse200.md)

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

# **reboot**
> inline_response2004.InlineResponse2004 reboot()

Reboot your whatsapp instance.

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Reboot your whatsapp instance.
        api_response = api_instance.reboot()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->reboot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**inline_response2004.InlineResponse2004**](InlineResponse2004.md)

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

# **retry**
> inline_response2003.InlineResponse2003 retry()

Repeat the manual synchronization attempt with the device

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Repeat the manual synchronization attempt with the device
        api_response = api_instance.retry()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->retry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**inline_response2003.InlineResponse2003**](InlineResponse2003.md)

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

# **set_settings**
> inline_response2005.InlineResponse2005 set_settings(settings_settings)

Set settings

**webhookUrl** - Http or https URL for receiving notifications. For testing, we recommend using [our RequestBin](http://bin.chat-api.com).  **ackNotificationsOn** - Turn on/off ack (message delivered and message viewed) notifications in webhooks. GET method works for the same address.  **chatUpdateOn** - Turn on/off chat update notifications in webhooks. GET method works for the same address.  **videoUploadOn** - Turn on/off receiving video messages.  **proxy** - Socks5 IP address and port proxy for instance.  **guaranteedHooks** - Guarantee webhook delivery. Each webhook will make 20 attempts to send until it receives 200 status from the server.  **ignoreOldMessages** - Do not send webhooks with old messages during authorization.  **processArchive** - Process messages from archived chats.  **instanceStatuses** - Turn on/off collecting instance status changing history.  **webhookStatuses** - Turn on/off collecting messages webhooks statuses.  **statusNotificationsOn** - Turn on/off instance changind status notifications in webhooks.

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
    api_instance = openapi_client.1InstanceApi(api_client)
    settings_settings = openapi_client.Settings() # settings.Settings | 
    
    # example passing only required values which don't have defaults set
    try:
        # Set settings
        api_response = api_instance.set_settings(settings_settings)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->set_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_settings** | [**settings.Settings**](Settings.md)|  |

### Return type

[**inline_response2005.InlineResponse2005**](InlineResponse2005.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |
**401** | Invalid token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **takeover**
> inline_response2001.InlineResponse2001 takeover()

Returns the active session if the device has connected another instance of Web WhatsApp

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
    api_instance = openapi_client.1InstanceApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Returns the active session if the device has connected another instance of Web WhatsApp
        api_response = api_instance.takeover()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1InstanceApi->takeover: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**inline_response2001.InlineResponse2001**](InlineResponse2001.md)

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

