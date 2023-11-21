from apinator import JsonApiBase
from pydantic import BaseModel, StringConstraints, validate_arguments
from typing_extensions import Annotated

from apinator_databricks.common import DatabricksContext


class DatabricksSubApi(BaseModel):
    version: Annotated[str, StringConstraints(pattern=r"\d+\.\d+")]
    prefix: Annotated[str, StringConstraints(pattern=r"^[a-z0-9_-]+$")]


class DatabricksApi(JsonApiBase):
    context_type = DatabricksContext
    sub_api: DatabricksSubApi = None

    @validate_arguments
    def __init__(
        self,
        context: DatabricksContext,
    ):
        self.context = context
        path_prefix = f"api/{self.sub_api.version}/{self.sub_api.prefix}"
        host = f"{context.account}.cloud.databricks.com"
        super().__init__(path_prefix=path_prefix, host=host, append_trailing_slash=True)

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.context.access_token.get_secret_value()}"
        }
