# openapi_client.3ChatsApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_participant**](3ChatsApi.md#add_group_participant) | **POST** /addGroupParticipant | Adding participant to a group
[**demote_group_participant**](3ChatsApi.md#demote_group_participant) | **POST** /demoteGroupParticipant | Demote group participant
[**get_chats**](3ChatsApi.md#get_chats) | **GET** /dialogs | Get the chat list.
[**group**](3ChatsApi.md#group) | **POST** /group | Creates a group and sends the message to the created group.
[**promote_group_participant**](3ChatsApi.md#promote_group_participant) | **POST** /promoteGroupParticipant | Make participant in the group an administrator
[**read_chat**](3ChatsApi.md#read_chat) | **POST** /readChat | Open chat for reading messages
[**remove_group_participant**](3ChatsApi.md#remove_group_participant) | **POST** /removeGroupParticipant | Remove participant from a group


# **add_group_participant**
> group_participant_status.GroupParticipantStatus add_group_participant(group_participant_action_group_participant_action)

Adding participant to a group

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
    api_instance = openapi_client.3ChatsApi(api_client)
    group_participant_action_group_participant_action = openapi_client.GroupParticipantAction() # group_participant_action.GroupParticipantAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Adding participant to a group
        api_response = api_instance.add_group_participant(group_participant_action_group_participant_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->add_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_participant_action_group_participant_action** | [**group_participant_action.GroupParticipantAction**](GroupParticipantAction.md)|  |

### Return type

[**group_participant_status.GroupParticipantStatus**](GroupParticipantStatus.md)

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

# **demote_group_participant**
> group_participant_status.GroupParticipantStatus demote_group_participant(group_participant_action_group_participant_action)

Demote group participant

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
    api_instance = openapi_client.3ChatsApi(api_client)
    group_participant_action_group_participant_action = openapi_client.GroupParticipantAction() # group_participant_action.GroupParticipantAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Demote group participant
        api_response = api_instance.demote_group_participant(group_participant_action_group_participant_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->demote_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_participant_action_group_participant_action** | [**group_participant_action.GroupParticipantAction**](GroupParticipantAction.md)|  |

### Return type

[**group_participant_status.GroupParticipantStatus**](GroupParticipantStatus.md)

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

# **get_chats**
> chats.Chats get_chats()

Get the chat list.

The chat list includes avatars.

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
    api_instance = openapi_client.3ChatsApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get the chat list.
        api_response = api_instance.get_chats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->get_chats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**chats.Chats**](Chats.md)

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

# **group**
> create_group_status.CreateGroupStatus group(create_group_action_create_group_action)

Creates a group and sends the message to the created group.

The group will be added to the queue for sending and sooner or later it will be created, even if the phone is disconnected from the Internet or the authorization is not passed.   2 Oct 2018 update: chatId parameter will be returned if group was created on your phone within 20 second.

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
    api_instance = openapi_client.3ChatsApi(api_client)
    create_group_action_create_group_action = openapi_client.CreateGroupAction() # create_group_action.CreateGroupAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Creates a group and sends the message to the created group.
        api_response = api_instance.group(create_group_action_create_group_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_action_create_group_action** | [**create_group_action.CreateGroupAction**](CreateGroupAction.md)|  |

### Return type

[**create_group_status.CreateGroupStatus**](CreateGroupStatus.md)

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

# **promote_group_participant**
> group_participant_status.GroupParticipantStatus promote_group_participant(group_participant_action_group_participant_action)

Make participant in the group an administrator

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
    api_instance = openapi_client.3ChatsApi(api_client)
    group_participant_action_group_participant_action = openapi_client.GroupParticipantAction() # group_participant_action.GroupParticipantAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Make participant in the group an administrator
        api_response = api_instance.promote_group_participant(group_participant_action_group_participant_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->promote_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_participant_action_group_participant_action** | [**group_participant_action.GroupParticipantAction**](GroupParticipantAction.md)|  |

### Return type

[**group_participant_status.GroupParticipantStatus**](GroupParticipantStatus.md)

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

# **read_chat**
> read_chat_status.ReadChatStatus read_chat(read_chat_action_read_chat_action)

Open chat for reading messages

Use this method to make users see their messages read.

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
    api_instance = openapi_client.3ChatsApi(api_client)
    read_chat_action_read_chat_action = openapi_client.ReadChatAction() # read_chat_action.ReadChatAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Open chat for reading messages
        api_response = api_instance.read_chat(read_chat_action_read_chat_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->read_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_chat_action_read_chat_action** | [**read_chat_action.ReadChatAction**](ReadChatAction.md)|  |

### Return type

[**read_chat_status.ReadChatStatus**](ReadChatStatus.md)

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

# **remove_group_participant**
> group_participant_status.GroupParticipantStatus remove_group_participant(group_participant_action_group_participant_action)

Remove participant from a group

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
    api_instance = openapi_client.3ChatsApi(api_client)
    group_participant_action_group_participant_action = openapi_client.GroupParticipantAction() # group_participant_action.GroupParticipantAction | 
    
    # example passing only required values which don't have defaults set
    try:
        # Remove participant from a group
        api_response = api_instance.remove_group_participant(group_participant_action_group_participant_action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 3ChatsApi->remove_group_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_participant_action_group_participant_action** | [**group_participant_action.GroupParticipantAction**](GroupParticipantAction.md)|  |

### Return type

[**group_participant_status.GroupParticipantStatus**](GroupParticipantStatus.md)

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

