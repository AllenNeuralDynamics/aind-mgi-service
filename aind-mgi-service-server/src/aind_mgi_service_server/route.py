"""Module to handle endpoint responses"""

from typing import List

from fastapi import APIRouter, Path, status
from fastapi_cache.decorator import cache
from httpx import AsyncClient

from aind_mgi_service_server.configs import settings
from aind_mgi_service_server.handler import SessionHandler
from aind_mgi_service_server.models import HealthCheck, MgiSummaryRow

router = APIRouter()


@cache(expire=86400)
async def get_mgi_allele_data(allele_name: str) -> List[MgiSummaryRow]:
    """Fetch and cache MGI allele information."""
    async with AsyncClient(
        base_url=settings.host.unicode_string(), timeout=30.0
    ) as session:
        mgi_summary_rows = await SessionHandler(
            session=session
        ).get_quick_search_info(allele_name=allele_name)
    return mgi_summary_rows


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
):
    """
    ## Allele Info
    Retrieve MGI allele information.
    """
    return await get_mgi_allele_data(allele_name=allele_name)
