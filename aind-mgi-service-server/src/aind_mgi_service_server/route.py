"""Module to handle endpoint responses"""

from typing import List

from httpx import AsyncClient
from fastapi import APIRouter, Depends, Path, status
from fastapi_cache.decorator import cache

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
def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@cache(expire=86400)
@router.get(
    "/allele_info/{allele_name}",
    response_model=List[MgiSummaryRow],
)
async def get_allele_info(
    allele_name: str = Path(
        ...,
        openapi_examples={
            "cre_line": {
                "summary": "Cre line example",
                "description": "Example using a Cre recombinase line",
                "value": "Parvalbumin-IRES-Cre",
            },
            "gene_symbol": {
                "summary": "Gene symbol example",
                "description": "Example using a gene symbol",
                "value": "Pvalb",
            },
        },
    ),
    session: AsyncClient = Depends(get_session),
):
    """
    ## Allele Info
    Retrieve MGI allele information.
    """
    mgi_summary_rows = await SessionHandler(
        session=session
    ).get_quick_search_info(allele_name=allele_name)
    return mgi_summary_rows
