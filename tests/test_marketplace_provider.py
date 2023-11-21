import json
import uuid

import pytest
import responses
from responses import matchers

from apinator_databricks.common import DatabricksContext
from apinator_databricks.marketplace_provider import (
    DatabricksMarketplaceProviderApi,
    mp_model,
)


@pytest.fixture
def databricks_context() -> DatabricksContext:
    return DatabricksContext(
        access_token="TOKEN",
        account="account",
    )


@pytest.fixture
def mp_api(databricks_context) -> DatabricksMarketplaceProviderApi:
    return DatabricksMarketplaceProviderApi(context=databricks_context)


@responses.activate
def test_api_basically_works(mp_api):
    sample_obj = mp_model.Listing(
        id=uuid.uuid4(),
        summary=mp_model.ListingSummary(
            name="Test Product",
            subtitle="An example product",
            status=mp_model.ListingStatus.PUBLISHED,
            provider_id=uuid.uuid4(),
            listing_type=mp_model.ListingType.STANDARD,
        ),
        detail=mp_model.ListingDetail(
            description="Just for testing",
        ),
    )
    responses.get(
        f"https://account.cloud.databricks.com/api/2.0/marketplace-provider/listings/{sample_obj.id}/",
        json=json.loads(sample_obj.model_dump_json()),
        match=[matchers.header_matcher({"Authorization": "Bearer TOKEN"})],
    )

    returned_share = mp_api.listings.retrieve(sample_obj.id)
    assert returned_share == sample_obj
