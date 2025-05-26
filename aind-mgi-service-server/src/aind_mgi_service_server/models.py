"""Models and schema definitions for backend data structures"""

from typing import Any, List, Literal, Optional

from pydantic import BaseModel, Field

from aind_mgi_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


class MgiSummaryRow(BaseModel):
    """Model of Summary Row dictionary returned"""

    detailUri: Optional[str] = Field(default=None)
    featureType: Optional[str] = Field(default=None)
    strand: Optional[str] = Field(default=None)
    chromosome: Optional[str] = Field(default=None)
    stars: Optional[str] = Field(default=None)
    bestMatchText: Optional[str] = Field(default=None)
    bestMatchType: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)
    symbol: Optional[str] = Field(default=None)


class MgiContent(BaseModel):
    """Model for response from MGI"""

    summaryRows: List[MgiSummaryRow]
    totalCount: Optional[int] = Field(default=None)
    meta: Optional[Any] = Field(default=None)
