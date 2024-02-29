# coding: utf-8

# flake8: noqa
"""
    Wishlist Service

    API for managing wishlists

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from wishlist.models.list_wishlists_request_filter import ListWishlistsRequestFilter
from wishlist.models.protobuf_any import ProtobufAny
from wishlist.models.rpc_status import RpcStatus
from wishlist.models.wishlist_add_item_to_wishlist_request import WishlistAddItemToWishlistRequest
from wishlist.models.wishlist_are_items_in_wishlists_request import WishlistAreItemsInWishlistsRequest
from wishlist.models.wishlist_are_items_in_wishlists_response import WishlistAreItemsInWishlistsResponse
from wishlist.models.wishlist_are_items_in_wishlists_response_payload import WishlistAreItemsInWishlistsResponsePayload
from wishlist.models.wishlist_bulk_create_sharing_request import WishlistBulkCreateSharingRequest
from wishlist.models.wishlist_bulk_create_sharing_response import WishlistBulkCreateSharingResponse
from wishlist.models.wishlist_bulk_remove_items_from_wishlists_request import WishlistBulkRemoveItemsFromWishlistsRequest
from wishlist.models.wishlist_bulk_revoke_sharing_request import WishlistBulkRevokeSharingRequest
from wishlist.models.wishlist_create_wishlist_request import WishlistCreateWishlistRequest
from wishlist.models.wishlist_delete_wishlist_request import WishlistDeleteWishlistRequest
from wishlist.models.wishlist_get_item_from_wishlist_request import WishlistGetItemFromWishlistRequest
from wishlist.models.wishlist_get_wishlist_by_id_request import WishlistGetWishlistByIdRequest
from wishlist.models.wishlist_get_wishlist_by_shared_code_request import WishlistGetWishlistBySharedCodeRequest
from wishlist.models.wishlist_list_wishlist_items_request import WishlistListWishlistItemsRequest
from wishlist.models.wishlist_list_wishlist_items_response import WishlistListWishlistItemsResponse
from wishlist.models.wishlist_list_wishlists_request import WishlistListWishlistsRequest
from wishlist.models.wishlist_list_wishlists_response import WishlistListWishlistsResponse
from wishlist.models.wishlist_localized_text import WishlistLocalizedText
from wishlist.models.wishlist_merge_wishlists_request import WishlistMergeWishlistsRequest
from wishlist.models.wishlist_permission import WishlistPermission
from wishlist.models.wishlist_privacy import WishlistPrivacy
from wishlist.models.wishlist_remove_item_from_wishlist_request import WishlistRemoveItemFromWishlistRequest
from wishlist.models.wishlist_sharing_request import WishlistSharingRequest
from wishlist.models.wishlist_sharing_response import WishlistSharingResponse
from wishlist.models.wishlist_update_item_in_wishlist_request import WishlistUpdateItemInWishlistRequest
from wishlist.models.wishlist_update_item_in_wishlist_request_payload import WishlistUpdateItemInWishlistRequestPayload
from wishlist.models.wishlist_update_wishlist_request import WishlistUpdateWishlistRequest
from wishlist.models.wishlist_update_wishlist_request_payload import WishlistUpdateWishlistRequestPayload
from wishlist.models.wishlist_wishlist_item_response import WishlistWishlistItemResponse
from wishlist.models.wishlist_wishlist_response import WishlistWishlistResponse