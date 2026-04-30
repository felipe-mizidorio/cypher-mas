from pydantic import BaseModel, ConfigDict
from typing import Annotated
from pydantic.functional_validators import AfterValidator


def check_lower_before_upper(v: tuple[float, float]) -> tuple[float, float]:
    assert v[0] < v[1], "Lower bound must be less than upper bound"
    return v


LimitBound = Annotated[tuple[float, float], AfterValidator(check_lower_before_upper)]


class LimitSet(BaseModel):
    model_config = ConfigDict(frozen=True)

    specification: LimitBound
    tolerance: LimitBound
    rejection: LimitBound


class Measurement(BaseModel):
    model_config = ConfigDict(frozen=True)

    point_id: str
    values: dict[str, float]
    limits: dict[str, LimitSet]
