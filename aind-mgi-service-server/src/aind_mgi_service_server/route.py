"""Module to handle endpoint responses"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from requests_toolbelt.sessions import BaseUrlSession

from aind_mgi_service_server.handler import SessionHandler
from aind_mgi_service_server.models import HealthCheck, MgiSummaryRow
from aind_mgi_service_server.session import get_session

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/allele_info/{allele_name}",
    response_model=List[MgiSummaryRow],
)
async def get_allele_info(
    allele_name: str = Path(..., examples=["Parvalbumin-IRES-Cre", "Pvalb"]),
    session: BaseUrlSession = Depends(get_session),
):
    """
    ## Allele Info
    Retrieve MGI allele information.
    """
    mgi_summary_rows = SessionHandler(session=session).get_quick_search_info(
        allele_name=allele_name
    )
    if len(mgi_summary_rows) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return mgi_summary_rows
