from ..models.measurement import Measurement
from ..models.analytics_result import AnalyticsResult, AlgorithmType


def classify_measurement(measurement: Measurement) -> list[AnalyticsResult]:
    results = []
    for metric, value in measurement.values.items():
        limits = measurement.limits[metric]
        lower_rej, upper_rej = limits.rejection
        lower_tol, upper_tol = limits.tolerance
        lower_spec, upper_spec = limits.specification

        if value < lower_rej or value > upper_rej:
            classification = "rejected"
        elif value < lower_tol or value > upper_tol:
            classification = "out_of_tolerance"
        elif value < lower_spec or value > upper_spec:
            classification = "out_of_specification"
        else:
            classification = "within_specification"

        results.append(
            AnalyticsResult(
                algorithm_name="MeasurementClassifier",
                algorithm_type=AlgorithmType.STATELESS,
                value={
                    "point_id": measurement.point_id,
                    "metric": metric,
                    "classification": classification,
                },
            )
        )

    return results
