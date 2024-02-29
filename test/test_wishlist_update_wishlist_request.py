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

from wishlist.models.wishlist_update_wishlist_request import WishlistUpdateWishlistRequest

class TestWishlistUpdateWishlistRequest(unittest.TestCase):
    """WishlistUpdateWishlistRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WishlistUpdateWishlistRequest:
        """Test WishlistUpdateWishlistRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WishlistUpdateWishlistRequest`
        """
        model = WishlistUpdateWishlistRequest()
        if include_optional:
            return WishlistUpdateWishlistRequest(
                tenant_id = '',
                id = '',
                payload = wishlist.models.wishlist_update_wishlist_request_payload.wishlistUpdateWishlistRequestPayload(
                    privacy = 'PRIVACY_UNKNOWN', 
                    label = wishlist.models.wishlist_localized_text.wishlistLocalizedText(
                        value = {
                            'key' : ''
                            }, ), 
                    description = wishlist.models.wishlist_localized_text.wishlistLocalizedText(), 
                    is_default = True, ),
                payload_mask = ''
            )
        else:
            return WishlistUpdateWishlistRequest(
                tenant_id = '',
                id = '',
                payload = wishlist.models.wishlist_update_wishlist_request_payload.wishlistUpdateWishlistRequestPayload(
                    privacy = 'PRIVACY_UNKNOWN', 
                    label = wishlist.models.wishlist_localized_text.wishlistLocalizedText(
                        value = {
                            'key' : ''
                            }, ), 
                    description = wishlist.models.wishlist_localized_text.wishlistLocalizedText(), 
                    is_default = True, ),
                payload_mask = '',
        )
        """

    def testWishlistUpdateWishlistRequest(self):
        """Test WishlistUpdateWishlistRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
