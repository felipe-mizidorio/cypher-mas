from enum import StrEnum
from typing import Any
from pydantic import BaseModel, ConfigDict


class AlgorithmType(StrEnum):
    STATELESS = "stateless"
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"


class AnalyticsResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    algorithm_name: str
    algorithm_type: AlgorithmType
    value: float | str | dict[str, Any]
