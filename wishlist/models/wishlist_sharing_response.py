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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from wishlist.models.wishlist_permission import WishlistPermission
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WishlistSharingResponse(BaseModel):
    """
    WishlistSharingResponse
    """ # noqa: E501
    sharing_id: Optional[StrictStr] = Field(default=None, alias="sharingId")
    sharing_grn: Optional[StrictStr] = Field(default=None, alias="sharingGrn")
    wishlist_id: Optional[StrictStr] = Field(default=None, alias="wishlistId")
    permission: Optional[WishlistPermission] = None
    customer_grn: Optional[StrictStr] = Field(default=None, alias="customerGrn")
    customer_aggregation_id: Optional[StrictStr] = Field(default=None, alias="customerAggregationId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["sharingId", "sharingGrn", "wishlistId", "permission", "customerGrn", "customerAggregationId", "createdAt", "updatedAt"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WishlistSharingResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WishlistSharingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sharingId": obj.get("sharingId"),
            "sharingGrn": obj.get("sharingGrn"),
            "wishlistId": obj.get("wishlistId"),
            "permission": obj.get("permission"),
            "customerGrn": obj.get("customerGrn"),
            "customerAggregationId": obj.get("customerAggregationId"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj

