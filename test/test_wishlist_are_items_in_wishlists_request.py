# coding: utf-8

"""
    Wishlist Service

    API for managing wishlists

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from wishlist.models.wishlist_are_items_in_wishlists_request import WishlistAreItemsInWishlistsRequest

class TestWishlistAreItemsInWishlistsRequest(unittest.TestCase):
    """WishlistAreItemsInWishlistsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WishlistAreItemsInWishlistsRequest:
        """Test WishlistAreItemsInWishlistsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WishlistAreItemsInWishlistsRequest`
        """
        model = WishlistAreItemsInWishlistsRequest()
        if include_optional:
            return WishlistAreItemsInWishlistsRequest(
                tenant_id = '',
                wishlist_id = '',
                customer_grn = '',
                item_grns = [
                    ''
                    ]
            )
        else:
            return WishlistAreItemsInWishlistsRequest(
                tenant_id = '',
                item_grns = [
                    ''
                    ],
        )
        """

    def testWishlistAreItemsInWishlistsRequest(self):
        """Test WishlistAreItemsInWishlistsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
