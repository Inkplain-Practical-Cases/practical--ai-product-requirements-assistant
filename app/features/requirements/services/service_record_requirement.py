"""Persist an analysis completion event after the requirement extractor succeeds."""
from app.features.requirements.providers.provider_record_requirement import provider_record_requirement

def service_record_requirement(brief: str, analysis: str) -> str:
    """Record a metadata-only request and linked analysis for audit."""
    return provider_record_requirement(brief, analysis)
