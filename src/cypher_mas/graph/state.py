from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

from ..models.measurement import Measurement
from ..models.reports import PointReport, ClusterReport, StationReport


class PointAgentState(TypedDict):
    measurement: Measurement
    cluster_info: dict[str, list[str]]
    messages: Annotated[list[BaseMessage], add_messages]
    point_report: PointReport | None
    is_leader: bool
    peer_points: list[PointReport]
    cluster_report: ClusterReport | None
    error: str | None


class StationAgentState(TypedDict):
    raw_measurements: list[Measurement]
    clusters: dict[str, list[str]]
    messages: Annotated[list[BaseMessage], add_messages]
    cluster_reports: list[ClusterReport]
    station_report: StationReport | None
    error: str | None


class InterstationAgentState(TypedDict):
    station_measurements: dict[str, list[Measurement]]
    messages: Annotated[list[BaseMessage], add_messages]
    interstation_clusters: dict[str, list[str]]
    station_reports: list[StationReport]
    error: str | None
