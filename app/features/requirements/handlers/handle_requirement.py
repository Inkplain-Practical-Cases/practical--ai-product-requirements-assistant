"""Handler: forward validated input to domain service.
ICS layer: handler
CRD component: be.handle_requirement
Called by: receive_requirement
Calls: service_requirement
Why: separates orchestration from HTTP.
Without: impossible to evolve business logic independently.
Step: added in STEP-1.
"""
from app.features.requirements.services.service_requirement import service_requirement
def handle_requirement(value: str) -> dict[str,str]:
    """Coordinate one input value and map a stable response contract."""
    return {"status": "accepted", "detail": service_requirement(value)}
