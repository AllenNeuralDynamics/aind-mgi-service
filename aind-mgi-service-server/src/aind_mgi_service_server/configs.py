"""Module for settings to connect to MGI backend"""

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, HttpUrl
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Settings needed to connect to MGI website"""

    model_config = SettingsConfigDict(env_prefix="MGI_", case_sensitive=False)
    host: HttpUrl = Field(
        default="https://www.informatics.jax.org",
        description="URL for MGI allele information.",
    )
