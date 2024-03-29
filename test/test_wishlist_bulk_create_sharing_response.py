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

from wishlist.models.wishlist_bulk_create_sharing_response import WishlistBulkCreateSharingResponse

class TestWishlistBulkCreateSharingResponse(unittest.TestCase):
    """WishlistBulkCreateSharingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WishlistBulkCreateSharingResponse:
        """Test WishlistBulkCreateSharingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WishlistBulkCreateSharingResponse`
        """
        model = WishlistBulkCreateSharingResponse()
        if include_optional:
            return WishlistBulkCreateSharingResponse(
                sharing_responses = [
                    wishlist.models.wishlist_sharing_response.wishlistSharingResponse(
                        sharing_id = '', 
                        sharing_grn = '', 
                        wishlist_id = '', 
                        permission = 'UNKNOWN_PERMISSION', 
                        customer_grn = '', 
                        customer_aggregation_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return WishlistBulkCreateSharingResponse(
        )
        """

    def testWishlistBulkCreateSharingResponse(self):
        """Test WishlistBulkCreateSharingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
