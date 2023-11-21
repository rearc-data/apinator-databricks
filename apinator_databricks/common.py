from typing import Union

from pydantic import BaseModel, SecretStr, StringConstraints
from typing_extensions import Annotated


class DatabricksContext(BaseModel):
    access_token: Union[SecretStr, str]
    account: Annotated[str, StringConstraints(pattern=r"^[a-z0-9_-]+$")]
