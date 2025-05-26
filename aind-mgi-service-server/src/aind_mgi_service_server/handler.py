"""Module to retrieve data from a backend using a session object"""

from typing import List

from requests_toolbelt.sessions import BaseUrlSession

from aind_mgi_service_server.models import MgiContent, MgiSummaryRow


class SessionHandler:
    """Handle session object to get data"""

    def __init__(self, session: BaseUrlSession):
        """Class constructor"""
        self.session = session

    def get_quick_search_info(self, allele_name: str) -> List[MgiSummaryRow]:
        """
        Get allele info from mgi endpoint
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
        response = self.session.get("/quicksearch/alleleBucket", params=params)
        response.raise_for_status()
        response_model = MgiContent(**response.json())
        return response_model.summaryRows
