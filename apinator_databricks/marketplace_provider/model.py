import enum
import uuid
from datetime import datetime
from typing import List, Optional

from apinator.common import StrictBaseModel
from pydantic import BaseModel, ConfigDict, Field


class ShareType(str, enum.Enum):
    SAMPLE = "SAMPLE"
    FULL = "FULL"


class ListingType(str, enum.Enum):
    STANDARD = "STANDARD"
    PERSONALIZED = "PERSONALIZED"


class ListingStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    PUBLISHED = "PUBLISHED"
    SUSPENDED = "SUSPENDED"


class ListingShare(StrictBaseModel):
    name: str
    type: ShareType


class ListingSetting(StrictBaseModel):
    visibility: str = "PUBLIC"  # deprecated


class ListingSummary(StrictBaseModel):
    name: str
    subtitle: str
    status: ListingStatus
    provider_info: Optional[dict] = None  # deprecated
    share: Optional[ListingShare] = None
    setting: Optional[ListingSetting] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    created_by_id: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_by_id: Optional[int] = None
    categories: List[str] = []
    listing_type: ListingType = Field(alias="listingType")
    provider_id: uuid.UUID
    model_config = ConfigDict(populate_by_name=True)


class EmbeddedNotebookFileParent(StrictBaseModel):
    parent_id: uuid.UUID
    file_parent_type: str


class EmbeddedNotebookFileInfo(StrictBaseModel):
    id: uuid.UUID
    display_name: Optional[str]
    marketplace_file_type: str
    file_parent: EmbeddedNotebookFileParent
    mime_type: str
    download_link: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str]  # Keeping this as str as enum values are not documented


class AssetType(str, enum.Enum):
    GIT_REPO = "ASSET_TYPE_GIT_REPO"
    DATA_TABLE = "ASSET_TYPE_DATA_TABLE"
    MODEL = "ASSET_TYPE_MODEL"


class ListingDetail(StrictBaseModel):
    description: str
    documentation_link: str = ""
    terms_of_service: str = ""
    contact_email: str = ""
    support_link: str = ""
    privacy_policy_link: str = ""
    embedded_notebook_file_infos: List[EmbeddedNotebookFileInfo] = []
    license: str = ""
    assets: list[AssetType] = []
    update_frequency: str | None = ""
    data_source: str | None = ""


class Listing(StrictBaseModel):
    id: Optional[uuid.UUID] = None
    summary: ListingSummary
    detail: ListingDetail
    # deployment_name: str


class ListingList(BaseModel):
    listings: List[Listing] = []
