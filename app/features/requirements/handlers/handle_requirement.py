"""Requirement handler orchestrates extraction and durable metadata-only analysis audit."""
from app.features.requirements.services.service_requirement import service_requirement
from app.features.requirements.services.service_record_requirement import service_record_requirement

def handle_requirement(value: str) -> dict[str, str]:
    """Preserve HTTP response while recording one successful requirement evaluation."""
    detail = service_requirement(value)
    service_record_requirement(value, detail)
    return {"status": "accepted", "detail": detail}
