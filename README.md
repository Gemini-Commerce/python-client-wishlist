# wishlist_client
API for managing wishlists

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.3.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-wishlist.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-wishlist.git`)

Then import the package:
```python
import wishlist
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wishlist
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wishlist
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
    except ApiException as e:
        print("Exception when calling WishlistApi->wishlist_add_item_to_wishlist: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://wishlist.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WishlistApi* | [**wishlist_add_item_to_wishlist**](docs/WishlistApi.md#wishlist_add_item_to_wishlist) | **POST** /wishlist.Wishlist/AddItemToWishlist | 
*WishlistApi* | [**wishlist_are_items_in_wishlists**](docs/WishlistApi.md#wishlist_are_items_in_wishlists) | **POST** /wishlist.Wishlist/AreItemsInWishlists | 
*WishlistApi* | [**wishlist_bulk_create_sharing**](docs/WishlistApi.md#wishlist_bulk_create_sharing) | **POST** /wishlist.Wishlist/BulkCreateSharing | Sharing endpoints
*WishlistApi* | [**wishlist_bulk_remove_items_from_wishlists**](docs/WishlistApi.md#wishlist_bulk_remove_items_from_wishlists) | **POST** /wishlist.Wishlist/BulkRemoveItemsFromWishlists | BulkRemoveItemsFromWishlists removes items from wishlists.
*WishlistApi* | [**wishlist_bulk_revoke_sharing**](docs/WishlistApi.md#wishlist_bulk_revoke_sharing) | **POST** /wishlist.Wishlist/BulkRevokeSharing | 
*WishlistApi* | [**wishlist_create_wishlist**](docs/WishlistApi.md#wishlist_create_wishlist) | **POST** /wishlist.Wishlist/CreateWishlist | 
*WishlistApi* | [**wishlist_delete_wishlist**](docs/WishlistApi.md#wishlist_delete_wishlist) | **POST** /wishlist.Wishlist/DeleteWishlist | 
*WishlistApi* | [**wishlist_get_item_from_wishlist**](docs/WishlistApi.md#wishlist_get_item_from_wishlist) | **POST** /wishlist.Wishlist/GetItemFromWishlist | 
*WishlistApi* | [**wishlist_get_wishlist_by_id**](docs/WishlistApi.md#wishlist_get_wishlist_by_id) | **POST** /wishlist.Wishlist/GetWishlistById | 
*WishlistApi* | [**wishlist_get_wishlist_by_shared_code**](docs/WishlistApi.md#wishlist_get_wishlist_by_shared_code) | **POST** /wishlist.Wishlist/GetWishlistBySharedCode | 
*WishlistApi* | [**wishlist_list_wishlist_items**](docs/WishlistApi.md#wishlist_list_wishlist_items) | **POST** /wishlist.Wishlist/ListWishlistItems | 
*WishlistApi* | [**wishlist_list_wishlists**](docs/WishlistApi.md#wishlist_list_wishlists) | **POST** /wishlist.Wishlist/ListWishlists | 
*WishlistApi* | [**wishlist_merge_wishlists**](docs/WishlistApi.md#wishlist_merge_wishlists) | **POST** /wishlist.Wishlist/MergeWishlists | 
*WishlistApi* | [**wishlist_remove_item_from_wishlist**](docs/WishlistApi.md#wishlist_remove_item_from_wishlist) | **POST** /wishlist.Wishlist/RemoveItemFromWishlist | 
*WishlistApi* | [**wishlist_update_item_in_wishlist**](docs/WishlistApi.md#wishlist_update_item_in_wishlist) | **POST** /wishlist.Wishlist/UpdateItemInWishlist | 
*WishlistApi* | [**wishlist_update_wishlist**](docs/WishlistApi.md#wishlist_update_wishlist) | **POST** /wishlist.Wishlist/UpdateWishlist | 


## Documentation For Models

 - [ListWishlistsRequestFilter](docs/ListWishlistsRequestFilter.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [WishlistAddItemToWishlistRequest](docs/WishlistAddItemToWishlistRequest.md)
 - [WishlistAreItemsInWishlistsRequest](docs/WishlistAreItemsInWishlistsRequest.md)
 - [WishlistAreItemsInWishlistsResponse](docs/WishlistAreItemsInWishlistsResponse.md)
 - [WishlistAreItemsInWishlistsResponsePayload](docs/WishlistAreItemsInWishlistsResponsePayload.md)
 - [WishlistBulkCreateSharingRequest](docs/WishlistBulkCreateSharingRequest.md)
 - [WishlistBulkCreateSharingResponse](docs/WishlistBulkCreateSharingResponse.md)
 - [WishlistBulkRemoveItemsFromWishlistsRequest](docs/WishlistBulkRemoveItemsFromWishlistsRequest.md)
 - [WishlistBulkRevokeSharingRequest](docs/WishlistBulkRevokeSharingRequest.md)
 - [WishlistCreateWishlistRequest](docs/WishlistCreateWishlistRequest.md)
 - [WishlistDeleteWishlistRequest](docs/WishlistDeleteWishlistRequest.md)
 - [WishlistGetItemFromWishlistRequest](docs/WishlistGetItemFromWishlistRequest.md)
 - [WishlistGetWishlistByIdRequest](docs/WishlistGetWishlistByIdRequest.md)
 - [WishlistGetWishlistBySharedCodeRequest](docs/WishlistGetWishlistBySharedCodeRequest.md)
 - [WishlistListWishlistItemsRequest](docs/WishlistListWishlistItemsRequest.md)
 - [WishlistListWishlistItemsResponse](docs/WishlistListWishlistItemsResponse.md)
 - [WishlistListWishlistsRequest](docs/WishlistListWishlistsRequest.md)
 - [WishlistListWishlistsResponse](docs/WishlistListWishlistsResponse.md)
 - [WishlistLocalizedText](docs/WishlistLocalizedText.md)
 - [WishlistMergeWishlistsRequest](docs/WishlistMergeWishlistsRequest.md)
 - [WishlistPermission](docs/WishlistPermission.md)
 - [WishlistPrivacy](docs/WishlistPrivacy.md)
 - [WishlistRemoveItemFromWishlistRequest](docs/WishlistRemoveItemFromWishlistRequest.md)
 - [WishlistSharingRequest](docs/WishlistSharingRequest.md)
 - [WishlistSharingResponse](docs/WishlistSharingResponse.md)
 - [WishlistUpdateItemInWishlistRequest](docs/WishlistUpdateItemInWishlistRequest.md)
 - [WishlistUpdateItemInWishlistRequestPayload](docs/WishlistUpdateItemInWishlistRequestPayload.md)
 - [WishlistUpdateWishlistRequest](docs/WishlistUpdateWishlistRequest.md)
 - [WishlistUpdateWishlistRequestPayload](docs/WishlistUpdateWishlistRequestPayload.md)
 - [WishlistWishlistItemResponse](docs/WishlistWishlistItemResponse.md)
 - [WishlistWishlistResponse](docs/WishlistWishlistResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


