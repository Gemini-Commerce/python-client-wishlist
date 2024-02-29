# coding: utf-8

"""
    Wishlist Service

    API for managing wishlists

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class WishlistPrivacy(str, Enum):
    """
    WishlistPrivacy
    """

    """
    allowed enum values
    """
    PRIVACY_UNKNOWN = 'PRIVACY_UNKNOWN'
    PRIVACY_PUBLIC = 'PRIVACY_PUBLIC'
    PRIVACY_PRIVATE = 'PRIVACY_PRIVATE'
    PRIVACY_SHARED = 'PRIVACY_SHARED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WishlistPrivacy from a JSON string"""
        return cls(json.loads(json_str))

