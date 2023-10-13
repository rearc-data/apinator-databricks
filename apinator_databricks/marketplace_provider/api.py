from apinator import EndpointAction, EndpointGroup

from .._common.api import DatabricksApi, DatabricksSubApi
from . import model


class DatabricksMarketplaceProviderApi(DatabricksApi):
    sub_api = DatabricksSubApi(prefix="marketplace-provider", version="2.0")

    listings = EndpointGroup(
        "/listings",
        actions=[
            EndpointAction.list(model.ListingList),
            EndpointAction.retrieve(model.Listing),
            EndpointAction.create(model.Listing),
            EndpointAction.update(model.Listing),
            EndpointAction.partial_update(model.Listing),
            EndpointAction.destroy(),
        ],
    )
