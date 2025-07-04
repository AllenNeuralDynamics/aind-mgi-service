"""Tests for handler module"""

import pytest

from aind_mgi_service_server.handler import SessionHandler


class TestHandler:
    """Test SessionHandler"""

    def test_get_quick_search_info(
        self, get_test_session, mock_get_example_response
    ):
        """Tests get_quick_search_info."""
        session_handler = SessionHandler(get_test_session)
        quick_search_info = session_handler.get_quick_search_info(
            allele_name="Parvalbumin-IRES-Cre"
        )
        assert len(quick_search_info) == 1


if __name__ == "__main__":
    pytest.main([__file__])
