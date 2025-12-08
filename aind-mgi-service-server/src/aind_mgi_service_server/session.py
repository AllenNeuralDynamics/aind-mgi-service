"""Module to handle requests session"""

from typing import AsyncGenerator

import httpx

from aind_mgi_service_server.configs import Settings

settings = Settings()


async def get_session() -> AsyncGenerator[httpx.AsyncClient, None]:
    """
    Yield an async session object. This will automatically close the session
    when finished.
    """
    async with httpx.AsyncClient(
        base_url=settings.host.unicode_string()
    ) as session:
        yield session
