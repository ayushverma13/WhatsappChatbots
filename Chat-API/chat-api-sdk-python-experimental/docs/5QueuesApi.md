# openapi_client.5QueuesApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_actions_queue**](5QueuesApi.md#clear_actions_queue) | **POST** /clearActionsQueue | Clear outbound actions queue.
[**clear_messages_queue**](5QueuesApi.md#clear_messages_queue) | **POST** /clearMessagesQueue | Clear outbound messages queue.
[**show_actions_queue**](5QueuesApi.md#show_actions_queue) | **GET** /showActionsQueue | Get outbound messages queue.
[**show_messages_queue**](5QueuesApi.md#show_messages_queue) | **GET** /showMessagesQueue | Get outbound messages queue.


# **clear_actions_queue**
> clear_actions_queue_status.ClearActionsQueueStatus clear_actions_queue()

Clear outbound actions queue.

This method is needed when you accidentally sent thousands of actions in a row.

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
    api_instance = openapi_client.5QueuesApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Clear outbound actions queue.
        api_response = api_instance.clear_actions_queue()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 5QueuesApi->clear_actions_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**clear_actions_queue_status.ClearActionsQueueStatus**](ClearActionsQueueStatus.md)

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

# **clear_messages_queue**
> clear_messages_queue_status.ClearMessagesQueueStatus clear_messages_queue()

Clear outbound messages queue.

This method is needed when you accidentally sent thousands of messages in a row.

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
    api_instance = openapi_client.5QueuesApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Clear outbound messages queue.
        api_response = api_instance.clear_messages_queue()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 5QueuesApi->clear_messages_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**clear_messages_queue_status.ClearMessagesQueueStatus**](ClearMessagesQueueStatus.md)

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

# **show_actions_queue**
> outbound_actions.OutboundActions show_actions_queue()

Get outbound messages queue.

When you create an action, all actions are queued up. If an action is not executed, it remains in the queue and will be sent for execution in time. again. The action cannot be executed due to the status of the device connected to the account.  This method give the last 100 actions in the queue.

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
    api_instance = openapi_client.5QueuesApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get outbound messages queue.
        api_response = api_instance.show_actions_queue()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 5QueuesApi->show_actions_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**outbound_actions.OutboundActions**](OutboundActions.md)

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

# **show_messages_queue**
> outbound_messages.OutboundMessages show_messages_queue()

Get outbound messages queue.

When sending messages, all messages are in the queue. If the message is not sent, then it remains in the queue and in time it will be sent again. The message may not be sent due to the status of the device connected to the account.   This method give the last 100 messages in the queue.

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
    api_instance = openapi_client.5QueuesApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get outbound messages queue.
        api_response = api_instance.show_messages_queue()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 5QueuesApi->show_messages_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**outbound_messages.OutboundMessages**](OutboundMessages.md)

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

