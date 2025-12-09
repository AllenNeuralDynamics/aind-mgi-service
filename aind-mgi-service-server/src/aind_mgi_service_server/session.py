"""Module to handle requests session"""

from typing import AsyncGenerator

from httpx import AsyncClient, Timeout

from aind_mgi_service_server.configs import Settings

settings = Settings()


async def get_session() -> AsyncGenerator[AsyncClient, None]:
    """
    Yield an async session object. This will automatically close the session
    when finished.
    """
    timeout = Timeout(30.0, read=60.0)
    async with AsyncClient(
        base_url=settings.host.unicode_string(), timeout=timeout
    ) as session:
        yield session
