# wishlist.WishlistApi

All URIs are relative to *https://wishlist.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wishlist_add_item_to_wishlist**](WishlistApi.md#wishlist_add_item_to_wishlist) | **POST** /wishlist.Wishlist/AddItemToWishlist | 
[**wishlist_are_items_in_wishlists**](WishlistApi.md#wishlist_are_items_in_wishlists) | **POST** /wishlist.Wishlist/AreItemsInWishlists | 
[**wishlist_bulk_create_sharing**](WishlistApi.md#wishlist_bulk_create_sharing) | **POST** /wishlist.Wishlist/BulkCreateSharing | Sharing endpoints
[**wishlist_bulk_remove_items_from_wishlists**](WishlistApi.md#wishlist_bulk_remove_items_from_wishlists) | **POST** /wishlist.Wishlist/BulkRemoveItemsFromWishlists | BulkRemoveItemsFromWishlists removes items from wishlists.
[**wishlist_bulk_revoke_sharing**](WishlistApi.md#wishlist_bulk_revoke_sharing) | **POST** /wishlist.Wishlist/BulkRevokeSharing | 
[**wishlist_create_wishlist**](WishlistApi.md#wishlist_create_wishlist) | **POST** /wishlist.Wishlist/CreateWishlist | 
[**wishlist_delete_wishlist**](WishlistApi.md#wishlist_delete_wishlist) | **POST** /wishlist.Wishlist/DeleteWishlist | 
[**wishlist_get_item_from_wishlist**](WishlistApi.md#wishlist_get_item_from_wishlist) | **POST** /wishlist.Wishlist/GetItemFromWishlist | 
[**wishlist_get_wishlist_by_id**](WishlistApi.md#wishlist_get_wishlist_by_id) | **POST** /wishlist.Wishlist/GetWishlistById | 
[**wishlist_get_wishlist_by_shared_code**](WishlistApi.md#wishlist_get_wishlist_by_shared_code) | **POST** /wishlist.Wishlist/GetWishlistBySharedCode | 
[**wishlist_list_wishlist_items**](WishlistApi.md#wishlist_list_wishlist_items) | **POST** /wishlist.Wishlist/ListWishlistItems | 
[**wishlist_list_wishlists**](WishlistApi.md#wishlist_list_wishlists) | **POST** /wishlist.Wishlist/ListWishlists | 
[**wishlist_merge_wishlists**](WishlistApi.md#wishlist_merge_wishlists) | **POST** /wishlist.Wishlist/MergeWishlists | 
[**wishlist_remove_item_from_wishlist**](WishlistApi.md#wishlist_remove_item_from_wishlist) | **POST** /wishlist.Wishlist/RemoveItemFromWishlist | 
[**wishlist_update_item_in_wishlist**](WishlistApi.md#wishlist_update_item_in_wishlist) | **POST** /wishlist.Wishlist/UpdateItemInWishlist | 
[**wishlist_update_wishlist**](WishlistApi.md#wishlist_update_wishlist) | **POST** /wishlist.Wishlist/UpdateWishlist | 


# **wishlist_add_item_to_wishlist**
> WishlistWishlistItemResponse wishlist_add_item_to_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_add_item_to_wishlist_request import WishlistAddItemToWishlistRequest
from wishlist.models.wishlist_wishlist_item_response import WishlistWishlistItemResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistAddItemToWishlistRequest() # WishlistAddItemToWishlistRequest | 

    try:
        api_response = api_instance.wishlist_add_item_to_wishlist(body)
        print("The response of WishlistApi->wishlist_add_item_to_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_add_item_to_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistAddItemToWishlistRequest**](WishlistAddItemToWishlistRequest.md)|  | 

### Return type

[**WishlistWishlistItemResponse**](WishlistWishlistItemResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_are_items_in_wishlists**
> WishlistAreItemsInWishlistsResponse wishlist_are_items_in_wishlists(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_are_items_in_wishlists_request import WishlistAreItemsInWishlistsRequest
from wishlist.models.wishlist_are_items_in_wishlists_response import WishlistAreItemsInWishlistsResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistAreItemsInWishlistsRequest() # WishlistAreItemsInWishlistsRequest | 

    try:
        api_response = api_instance.wishlist_are_items_in_wishlists(body)
        print("The response of WishlistApi->wishlist_are_items_in_wishlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_are_items_in_wishlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistAreItemsInWishlistsRequest**](WishlistAreItemsInWishlistsRequest.md)|  | 

### Return type

[**WishlistAreItemsInWishlistsResponse**](WishlistAreItemsInWishlistsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_bulk_create_sharing**
> WishlistBulkCreateSharingResponse wishlist_bulk_create_sharing(body)

Sharing endpoints

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_bulk_create_sharing_request import WishlistBulkCreateSharingRequest
from wishlist.models.wishlist_bulk_create_sharing_response import WishlistBulkCreateSharingResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistBulkCreateSharingRequest() # WishlistBulkCreateSharingRequest | 

    try:
        # Sharing endpoints
        api_response = api_instance.wishlist_bulk_create_sharing(body)
        print("The response of WishlistApi->wishlist_bulk_create_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_bulk_create_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistBulkCreateSharingRequest**](WishlistBulkCreateSharingRequest.md)|  | 

### Return type

[**WishlistBulkCreateSharingResponse**](WishlistBulkCreateSharingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_bulk_remove_items_from_wishlists**
> object wishlist_bulk_remove_items_from_wishlists(body)

BulkRemoveItemsFromWishlists removes items from wishlists.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_bulk_remove_items_from_wishlists_request import WishlistBulkRemoveItemsFromWishlistsRequest
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistBulkRemoveItemsFromWishlistsRequest() # WishlistBulkRemoveItemsFromWishlistsRequest | 

    try:
        # BulkRemoveItemsFromWishlists removes items from wishlists.
        api_response = api_instance.wishlist_bulk_remove_items_from_wishlists(body)
        print("The response of WishlistApi->wishlist_bulk_remove_items_from_wishlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_bulk_remove_items_from_wishlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistBulkRemoveItemsFromWishlistsRequest**](WishlistBulkRemoveItemsFromWishlistsRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_bulk_revoke_sharing**
> object wishlist_bulk_revoke_sharing(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_bulk_revoke_sharing_request import WishlistBulkRevokeSharingRequest
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistBulkRevokeSharingRequest() # WishlistBulkRevokeSharingRequest | 

    try:
        api_response = api_instance.wishlist_bulk_revoke_sharing(body)
        print("The response of WishlistApi->wishlist_bulk_revoke_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_bulk_revoke_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistBulkRevokeSharingRequest**](WishlistBulkRevokeSharingRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_create_wishlist**
> WishlistWishlistResponse wishlist_create_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_create_wishlist_request import WishlistCreateWishlistRequest
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistCreateWishlistRequest() # WishlistCreateWishlistRequest | 

    try:
        api_response = api_instance.wishlist_create_wishlist(body)
        print("The response of WishlistApi->wishlist_create_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_create_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistCreateWishlistRequest**](WishlistCreateWishlistRequest.md)|  | 

### Return type

[**WishlistWishlistResponse**](WishlistWishlistResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_delete_wishlist**
> object wishlist_delete_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_delete_wishlist_request import WishlistDeleteWishlistRequest
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistDeleteWishlistRequest() # WishlistDeleteWishlistRequest | 

    try:
        api_response = api_instance.wishlist_delete_wishlist(body)
        print("The response of WishlistApi->wishlist_delete_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_delete_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistDeleteWishlistRequest**](WishlistDeleteWishlistRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_get_item_from_wishlist**
> WishlistWishlistItemResponse wishlist_get_item_from_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_get_item_from_wishlist_request import WishlistGetItemFromWishlistRequest
from wishlist.models.wishlist_wishlist_item_response import WishlistWishlistItemResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistGetItemFromWishlistRequest() # WishlistGetItemFromWishlistRequest | 

    try:
        api_response = api_instance.wishlist_get_item_from_wishlist(body)
        print("The response of WishlistApi->wishlist_get_item_from_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_get_item_from_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistGetItemFromWishlistRequest**](WishlistGetItemFromWishlistRequest.md)|  | 

### Return type

[**WishlistWishlistItemResponse**](WishlistWishlistItemResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_get_wishlist_by_id**
> WishlistWishlistResponse wishlist_get_wishlist_by_id(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_get_wishlist_by_id_request import WishlistGetWishlistByIdRequest
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistGetWishlistByIdRequest() # WishlistGetWishlistByIdRequest | 

    try:
        api_response = api_instance.wishlist_get_wishlist_by_id(body)
        print("The response of WishlistApi->wishlist_get_wishlist_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_get_wishlist_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistGetWishlistByIdRequest**](WishlistGetWishlistByIdRequest.md)|  | 

### Return type

[**WishlistWishlistResponse**](WishlistWishlistResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_get_wishlist_by_shared_code**
> WishlistWishlistResponse wishlist_get_wishlist_by_shared_code(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_get_wishlist_by_shared_code_request import WishlistGetWishlistBySharedCodeRequest
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistGetWishlistBySharedCodeRequest() # WishlistGetWishlistBySharedCodeRequest | 

    try:
        api_response = api_instance.wishlist_get_wishlist_by_shared_code(body)
        print("The response of WishlistApi->wishlist_get_wishlist_by_shared_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_get_wishlist_by_shared_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistGetWishlistBySharedCodeRequest**](WishlistGetWishlistBySharedCodeRequest.md)|  | 

### Return type

[**WishlistWishlistResponse**](WishlistWishlistResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_list_wishlist_items**
> WishlistListWishlistItemsResponse wishlist_list_wishlist_items(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_list_wishlist_items_request import WishlistListWishlistItemsRequest
from wishlist.models.wishlist_list_wishlist_items_response import WishlistListWishlistItemsResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistListWishlistItemsRequest() # WishlistListWishlistItemsRequest | 

    try:
        api_response = api_instance.wishlist_list_wishlist_items(body)
        print("The response of WishlistApi->wishlist_list_wishlist_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_list_wishlist_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistListWishlistItemsRequest**](WishlistListWishlistItemsRequest.md)|  | 

### Return type

[**WishlistListWishlistItemsResponse**](WishlistListWishlistItemsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_list_wishlists**
> WishlistListWishlistsResponse wishlist_list_wishlists(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_list_wishlists_request import WishlistListWishlistsRequest
from wishlist.models.wishlist_list_wishlists_response import WishlistListWishlistsResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistListWishlistsRequest() # WishlistListWishlistsRequest | 

    try:
        api_response = api_instance.wishlist_list_wishlists(body)
        print("The response of WishlistApi->wishlist_list_wishlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_list_wishlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistListWishlistsRequest**](WishlistListWishlistsRequest.md)|  | 

### Return type

[**WishlistListWishlistsResponse**](WishlistListWishlistsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_merge_wishlists**
> WishlistWishlistResponse wishlist_merge_wishlists(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_merge_wishlists_request import WishlistMergeWishlistsRequest
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistMergeWishlistsRequest() # WishlistMergeWishlistsRequest | 

    try:
        api_response = api_instance.wishlist_merge_wishlists(body)
        print("The response of WishlistApi->wishlist_merge_wishlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_merge_wishlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistMergeWishlistsRequest**](WishlistMergeWishlistsRequest.md)|  | 

### Return type

[**WishlistWishlistResponse**](WishlistWishlistResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_remove_item_from_wishlist**
> object wishlist_remove_item_from_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_remove_item_from_wishlist_request import WishlistRemoveItemFromWishlistRequest
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistRemoveItemFromWishlistRequest() # WishlistRemoveItemFromWishlistRequest | 

    try:
        api_response = api_instance.wishlist_remove_item_from_wishlist(body)
        print("The response of WishlistApi->wishlist_remove_item_from_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_remove_item_from_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistRemoveItemFromWishlistRequest**](WishlistRemoveItemFromWishlistRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_update_item_in_wishlist**
> WishlistWishlistItemResponse wishlist_update_item_in_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_update_item_in_wishlist_request import WishlistUpdateItemInWishlistRequest
from wishlist.models.wishlist_wishlist_item_response import WishlistWishlistItemResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistUpdateItemInWishlistRequest() # WishlistUpdateItemInWishlistRequest | 

    try:
        api_response = api_instance.wishlist_update_item_in_wishlist(body)
        print("The response of WishlistApi->wishlist_update_item_in_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_update_item_in_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistUpdateItemInWishlistRequest**](WishlistUpdateItemInWishlistRequest.md)|  | 

### Return type

[**WishlistWishlistItemResponse**](WishlistWishlistItemResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wishlist_update_wishlist**
> WishlistWishlistResponse wishlist_update_wishlist(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import wishlist
from wishlist.models.wishlist_update_wishlist_request import WishlistUpdateWishlistRequest
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse
from wishlist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://wishlist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wishlist.Configuration(
    host = "https://wishlist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with wishlist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wishlist.WishlistApi(api_client)
    body = wishlist.WishlistUpdateWishlistRequest() # WishlistUpdateWishlistRequest | 

    try:
        api_response = api_instance.wishlist_update_wishlist(body)
        print("The response of WishlistApi->wishlist_update_wishlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishlistApi->wishlist_update_wishlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WishlistUpdateWishlistRequest**](WishlistUpdateWishlistRequest.md)|  | 

### Return type

[**WishlistWishlistResponse**](WishlistWishlistResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

