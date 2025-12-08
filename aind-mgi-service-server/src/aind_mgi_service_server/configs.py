"""Module for settings to connect to MGI backend"""

from typing import Optional

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, HttpUrl, RedisDsn
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Settings needed to connect to MGI website"""

    model_config = SettingsConfigDict(env_prefix="MGI_", case_sensitive=False)
    host: HttpUrl = Field(
        default="https://www.informatics.jax.org",
        description="URL for MGI allele information.",
    )
    redis_url: Optional[RedisDsn] = Field(default=None)


settings = Settings()
