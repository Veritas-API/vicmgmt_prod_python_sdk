# swagger_client.VeritasInformationClassifierVICApi

All URIs are relative to *http://veritas-prod-prod.apigee.net/vic/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_tag**](VeritasInformationClassifierVICApi.md#create_or_update_tag) | **PUT** /management/tags/{tag} | Create or update tag
[**create_pattern**](VeritasInformationClassifierVICApi.md#create_pattern) | **POST** /management/patterns | Create pattern
[**create_policy**](VeritasInformationClassifierVICApi.md#create_policy) | **POST** /management/policies | Create policy
[**delete_pattern**](VeritasInformationClassifierVICApi.md#delete_pattern) | **DELETE** /management/patterns/{id} | Delete pattern
[**delete_policy**](VeritasInformationClassifierVICApi.md#delete_policy) | **DELETE** /management/policies/{id} | Delete policy
[**delete_tag**](VeritasInformationClassifierVICApi.md#delete_tag) | **DELETE** /management/tags/{tag} | Delete tag
[**get_metadata_definitions**](VeritasInformationClassifierVICApi.md#get_metadata_definitions) | **GET** /management/policies/metadata | List metadata definitions
[**get_pattern**](VeritasInformationClassifierVICApi.md#get_pattern) | **GET** /management/patterns/{id} | Get pattern
[**get_pattern_collection**](VeritasInformationClassifierVICApi.md#get_pattern_collection) | **GET** /management/patterns | List patterns
[**get_policies_by_pattern**](VeritasInformationClassifierVICApi.md#get_policies_by_pattern) | **GET** /management/patterns/{id}/policies | List policies that use a pattern
[**get_policies_by_tag**](VeritasInformationClassifierVICApi.md#get_policies_by_tag) | **GET** /management/tags/{tag}/policies | List policies that use a tag
[**get_policy**](VeritasInformationClassifierVICApi.md#get_policy) | **GET** /management/policies/{id} | Get policy
[**get_policy_collection**](VeritasInformationClassifierVICApi.md#get_policy_collection) | **GET** /management/policies | List policies
[**get_tag**](VeritasInformationClassifierVICApi.md#get_tag) | **GET** /management/tags/{tag} | Get tag
[**get_tag_property_definitions**](VeritasInformationClassifierVICApi.md#get_tag_property_definitions) | **GET** /management/tags/propertyDefinitions | List tag property definitions
[**get_tags_collection**](VeritasInformationClassifierVICApi.md#get_tags_collection) | **GET** /management/tags | List tags
[**patch_policy**](VeritasInformationClassifierVICApi.md#patch_policy) | **PATCH** /management/policies/{id} | Patch policy
[**reset_policy**](VeritasInformationClassifierVICApi.md#reset_policy) | **DELETE** /management/policies/{id}/overrides | Reset policy to defaults
[**update_pattern**](VeritasInformationClassifierVICApi.md#update_pattern) | **PUT** /management/patterns/{id} | Update pattern
[**update_policy**](VeritasInformationClassifierVICApi.md#update_policy) | **PUT** /management/policies/{id} | Update policy


# **create_or_update_tag**
> Tag create_or_update_tag(tag, body, tenant_id=tenant_id)

Create or update tag

Create or update a tag.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tag = 'tag_example' # str | 
body = swagger_client.Tag() # Tag | Tag
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create or update tag
    api_response = api_instance.create_or_update_tag(tag, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->create_or_update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **body** | [**Tag**](Tag.md)| Tag | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pattern**
> Pattern create_pattern(body, tenant_id=tenant_id)

Create pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
body = swagger_client.Pattern() # Pattern | New pattern
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create pattern
    api_response = api_instance.create_pattern(body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->create_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pattern**](Pattern.md)| New pattern | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> Policy create_policy(body, tenant_id=tenant_id)

Create policy

Create a custom policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
body = swagger_client.Policy() # Policy | New policy
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Create policy
    api_response = api_instance.create_policy(body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)| New policy | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pattern**
> delete_pattern(id, tenant_id=tenant_id)

Delete pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The pattern identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete pattern
    api_instance.delete_pattern(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->delete_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id, tenant_id=tenant_id)

Delete policy

Delete a custom policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete policy
    api_instance.delete_policy(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag, tenant_id=tenant_id)

Delete tag

Delete a custom tag.  (Built-in tags cannot be deleted.)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Delete tag
    api_instance.delete_tag(tag, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_definitions**
> MetadataDefinitionCollection get_metadata_definitions(tenant_id=tenant_id)

List metadata definitions



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List metadata definitions
    api_response = api_instance.get_metadata_definitions(tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_metadata_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**MetadataDefinitionCollection**](MetadataDefinitionCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern**
> Pattern get_pattern(id, tenant_id=tenant_id)

Get pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The pattern identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get pattern
    api_response = api_instance.get_pattern(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern_collection**
> PatternCollection get_pattern_collection(tenant_id=tenant_id, if_none_match=if_none_match)

List patterns



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List patterns
    api_response = api_instance.get_pattern_collection(tenant_id=tenant_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_pattern_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **if_none_match** | **str**|  | [optional] 

### Return type

[**PatternCollection**](PatternCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_by_pattern**
> PolicyCollection get_policies_by_pattern(id, tenant_id=tenant_id)

List policies that use a pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List policies that use a pattern
    api_response = api_instance.get_policies_by_pattern(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_policies_by_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_by_tag**
> PolicyCollection get_policies_by_tag(tag, tenant_id=tenant_id)

List policies that use a tag



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List policies that use a tag
    api_response = api_instance.get_policies_by_tag(tag, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_policies_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(id, tenant_id=tenant_id)

Get policy

Retrieve a policy

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get policy
    api_response = api_instance.get_policy(id, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_collection**
> PolicyCollection get_policy_collection(tenant_id=tenant_id, include_disabled=include_disabled, include_engine_body=include_engine_body, if_none_match=if_none_match)

List policies

Retrieve the policies for a tenant.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
include_disabled = true # bool | Include disabled policies (as well as enabled ones) (optional)
include_engine_body = true # bool | Include the engine body for policies, and the engine rule sets. (optional)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List policies
    api_response = api_instance.get_policy_collection(tenant_id=tenant_id, include_disabled=include_disabled, include_engine_body=include_engine_body, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_policy_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **include_disabled** | **bool**| Include disabled policies (as well as enabled ones) | [optional] 
 **include_engine_body** | **bool**| Include the engine body for policies, and the engine rule sets. | [optional] 
 **if_none_match** | **str**|  | [optional] 

### Return type

[**PolicyCollection**](PolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(tag, tenant_id=tenant_id)

Get tag

Get a tag.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tag = 'tag_example' # str | 
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Get tag
    api_response = api_instance.get_tag(tag, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_property_definitions**
> TagPropertyDefinitionCollection get_tag_property_definitions(tenant_id=tenant_id)

List tag property definitions

Get definitions of properties that can be associated with a tag. This is useful, for example, for user interfaces that need to know the supported values for such properties. Generally the tag properties are application-specific and not part of the core service functionality.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # List tag property definitions
    api_response = api_instance.get_tag_property_definitions(tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_tag_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**TagPropertyDefinitionCollection**](TagPropertyDefinitionCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_collection**
> TagsCollection get_tags_collection(tenant_id=tenant_id, if_none_match=if_none_match)

List tags

Retrieve all of the tags for a tenant.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)
if_none_match = 'if_none_match_example' # str |  (optional)

try: 
    # List tags
    api_response = api_instance.get_tags_collection(tenant_id=tenant_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_tags_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]
 **if_none_match** | **str**|  | [optional] 

### Return type

[**TagsCollection**](TagsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy**
> Policy patch_policy(id, patch, tenant_id=tenant_id)

Patch policy

Update part of a policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The policy identifier
patch = [swagger_client.JsonPatchDocument()] # list[JsonPatchDocument] | A patch containing instructions for how the policy should be modified. See RFC 6902.
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Patch policy
    api_response = api_instance.patch_policy(id, patch, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->patch_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **patch** | [**list[JsonPatchDocument]**](JsonPatchDocument.md)| A patch containing instructions for how the policy should be modified. See RFC 6902. | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_policy**
> reset_policy(id, tenant_id=tenant_id)

Reset policy to defaults

Reset a policy to its default settings.  Only valid for built-in policies.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The policy identifier
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Reset policy to defaults
    api_instance.reset_policy(id, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->reset_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pattern**
> Pattern update_pattern(id, body, tenant_id=tenant_id)

Update pattern



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The pattern identifier
body = swagger_client.Pattern() # Pattern | Updated pattern
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Update pattern
    api_response = api_instance.update_pattern(id, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->update_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The pattern identifier | 
 **body** | [**Pattern**](Pattern.md)| Updated pattern | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(id, body, tenant_id=tenant_id)

Update policy

Update a policy.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()
id = 'id_example' # str | The policy identifier
body = swagger_client.Policy() # Policy | Updated policy
tenant_id = '_Default' # str | The tenant identifier (optional) (default to _Default)

try: 
    # Update policy
    api_response = api_instance.update_policy(id, body, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The policy identifier | 
 **body** | [**Policy**](Policy.md)| Updated policy | 
 **tenant_id** | **str**| The tenant identifier | [optional] [default to _Default]

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

