"""Module to handle requests session"""

from requests_toolbelt.sessions import BaseUrlSession

from aind_mgi_service_server.configs import Settings

settings = Settings()


def get_session():
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    session = BaseUrlSession(base_url=settings.host.unicode_string())
    try:
        yield session
    finally:
        session.close()
