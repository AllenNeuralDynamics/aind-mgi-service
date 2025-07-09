"""Module to retrieve data from a backend using a session object"""

from typing import List

import httpx

from aind_mgi_service_server.models import MgiContent, MgiSummaryRow


class SessionHandler:
    """Handle session object to get data"""

    def __init__(self, session: httpx.AsyncClient):
        """Class constructor"""
        self.session = session

    async def get_quick_search_info(
        self, allele_name: str
    ) -> List[MgiSummaryRow]:
        """
        Retrieve MGI allele information asynchronously.

        Parameters
        ----------
        allele_name : str

        Returns
        -------
        List[MgiResponse]

        """
        params = {
            "queryType": "exactPhrase",
            "query": allele_name,
            "submit": "Quick+Search",
        }
        response = await self.session.get(
            "/quicksearch/alleleBucket", params=params
        )
        response.raise_for_status()
        response_model = MgiContent(**response.json())
        return response_model.summaryRows
