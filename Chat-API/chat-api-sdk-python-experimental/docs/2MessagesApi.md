# openapi_client.2MessagesApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forward_message**](2MessagesApi.md#forward_message) | **POST** /forwardMessage | Forwarding messages to a new or existing chat.
[**get_messages**](2MessagesApi.md#get_messages) | **GET** /messages | Get a list of messages.
[**send_contact**](2MessagesApi.md#send_contact) | **POST** /sendContact | Sending a contact or contact list to a new or existing chat.
[**send_file**](2MessagesApi.md#send_file) | **POST** /sendFile | Send a file to a new or existing chat.
[**send_link**](2MessagesApi.md#send_link) | **POST** /sendLink | Send text with link and link&#39;s preview to a new or existing chat.
[**send_location**](2MessagesApi.md#send_location) | **POST** /sendLocation | Sending a location to a new or existing chat.
[**send_message**](2MessagesApi.md#send_message) | **POST** /sendMessage | Send a message to a new or existing chat.
[**send_ptt**](2MessagesApi.md#send_ptt) | **POST** /sendPTT | Send a ptt-audio to a new or existing chat.
[**send_v_card**](2MessagesApi.md#send_v_card) | **POST** /sendVCard | Sending a vcard to a new or existing chat.


# **forward_message**
> send_message_status.SendMessageStatus forward_message(forward_message_request_forward_message_request)

Forwarding messages to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    forward_message_request_forward_message_request = openapi_client.ForwardMessageRequest() # forward_message_request.ForwardMessageRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Forwarding messages to a new or existing chat.
        api_response = api_instance.forward_message(forward_message_request_forward_message_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->forward_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_message_request_forward_message_request** | [**forward_message_request.ForwardMessageRequest**](ForwardMessageRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> messages.Messages get_messages()

Get a list of messages.

To receive only new messages, pass the **lastMessageNumber** parameter from the last query.  Files from messages are guaranteed to be stored only for 30 days and can be deleted. Download the files as soon as you get to your server.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    last_message_number = 0 # int | The lastMessageNumber parameter from the last response (optional)
last = False # bool | Displays the last 100 messages. If this parameter is passed, then lastMessageNumber is ignored. (optional) if omitted the server will use the default value of False
chat_id = '17633123456@c.us' # str | Filter messages by chatId  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. (optional)
limit = 100 # int | Sets length of the message list. Default 100. With value 0 returns all messages. (optional)
min_time = 946684800 # int | Filter messages received after specified time. Example: 946684800. (optional)
max_time = 946684800 # int | Filter messages received before specified time. Example: 946684800. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of messages.
        api_response = api_instance.get_messages(last_message_number=last_message_number, last=last, chat_id=chat_id, limit=limit, min_time=min_time, max_time=max_time)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_message_number** | **int**| The lastMessageNumber parameter from the last response | [optional]
 **last** | **bool**| Displays the last 100 messages. If this parameter is passed, then lastMessageNumber is ignored. | [optional] if omitted the server will use the default value of False
 **chat_id** | **str**| Filter messages by chatId  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. | [optional]
 **limit** | **int**| Sets length of the message list. Default 100. With value 0 returns all messages. | [optional]
 **min_time** | **int**| Filter messages received after specified time. Example: 946684800. | [optional]
 **max_time** | **int**| Filter messages received before specified time. Example: 946684800. | [optional]

### Return type

[**messages.Messages**](Messages.md)

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

# **send_contact**
> send_message_status.SendMessageStatus send_contact(send_contact_request_send_contact_request)

Sending a contact or contact list to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_contact_request_send_contact_request = openapi_client.SendContactRequest() # send_contact_request.SendContactRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Sending a contact or contact list to a new or existing chat.
        api_response = api_instance.send_contact(send_contact_request_send_contact_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_contact_request_send_contact_request** | [**send_contact_request.SendContactRequest**](SendContactRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_file**
> send_message_status.SendMessageStatus send_file(send_file_request_send_file_request)

Send a file to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_file_request_send_file_request = openapi_client.SendFileRequest() # send_file_request.SendFileRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Send a file to a new or existing chat.
        api_response = api_instance.send_file(send_file_request_send_file_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_file_request_send_file_request** | [**send_file_request.SendFileRequest**](SendFileRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_link**
> send_message_status.SendMessageStatus send_link(send_link_request_send_link_request)

Send text with link and link's preview to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_link_request_send_link_request = openapi_client.SendLinkRequest() # send_link_request.SendLinkRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Send text with link and link's preview to a new or existing chat.
        api_response = api_instance.send_link(send_link_request_send_link_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_link_request_send_link_request** | [**send_link_request.SendLinkRequest**](SendLinkRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_location**
> send_message_status.SendMessageStatus send_location(send_location_request_send_location_request)

Sending a location to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_location_request_send_location_request = openapi_client.SendLocationRequest() # send_location_request.SendLocationRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Sending a location to a new or existing chat.
        api_response = api_instance.send_location(send_location_request_send_location_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_location_request_send_location_request** | [**send_location_request.SendLocationRequest**](SendLocationRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> send_message_status.SendMessageStatus send_message(send_message_request_send_message_request)

Send a message to a new or existing chat.

The message will be added to the queue for sending and delivered even if the phone is disconnected from the Internet or authorization is not passed.  Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_message_request_send_message_request = openapi_client.SendMessageRequest() # send_message_request.SendMessageRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Send a message to a new or existing chat.
        api_response = api_instance.send_message(send_message_request_send_message_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_request_send_message_request** | [**send_message_request.SendMessageRequest**](SendMessageRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_ptt**
> send_message_status.SendMessageStatus send_ptt(send_ptt_request_send_ptt_request)

Send a ptt-audio to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_ptt_request_send_ptt_request = openapi_client.SendPTTRequest() # send_ptt_request.SendPTTRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Send a ptt-audio to a new or existing chat.
        api_response = api_instance.send_ptt(send_ptt_request_send_ptt_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_ptt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_ptt_request_send_ptt_request** | [**send_ptt_request.SendPTTRequest**](SendPTTRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_v_card**
> send_message_status.SendMessageStatus send_v_card(send_v_card_request_send_v_card_request)

Sending a vcard to a new or existing chat.

Only one of two parameters is needed to determine the destination - chatId or phone.

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
    api_instance = openapi_client.2MessagesApi(api_client)
    send_v_card_request_send_v_card_request = openapi_client.SendVCardRequest() # send_v_card_request.SendVCardRequest | 
    
    # example passing only required values which don't have defaults set
    try:
        # Sending a vcard to a new or existing chat.
        api_response = api_instance.send_v_card(send_v_card_request_send_v_card_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 2MessagesApi->send_v_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_v_card_request_send_v_card_request** | [**send_v_card_request.SendVCardRequest**](SendVCardRequest.md)|  |

### Return type

[**send_message_status.SendMessageStatus**](SendMessageStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

