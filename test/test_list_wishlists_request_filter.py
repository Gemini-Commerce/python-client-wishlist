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

from wishlist.models.list_wishlists_request_filter import ListWishlistsRequestFilter

class TestListWishlistsRequestFilter(unittest.TestCase):
    """ListWishlistsRequestFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListWishlistsRequestFilter:
        """Test ListWishlistsRequestFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWishlistsRequestFilter`
        """
        model = ListWishlistsRequestFilter()
        if include_optional:
            return ListWishlistsRequestFilter(
                customer_grn = ''
            )
        else:
            return ListWishlistsRequestFilter(
        )
        """

    def testListWishlistsRequestFilter(self):
        """Test ListWishlistsRequestFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
