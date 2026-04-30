from datetime import datetime, timezone

from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field

from .measurement import Measurement
from .analytics_result import AnalyticsResult


class BaseReport(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    diagnosis: str


class PointReport(BaseReport):
    point_agent_id: str
    measurement: Measurement
    analytic_results: list[AnalyticsResult]


class ClusterReport(BaseReport):
    cluster_id: str
    point_reports: list[PointReport]


class StationReport(BaseReport):
    station_id: str
    cluster_reports: list[ClusterReport]
