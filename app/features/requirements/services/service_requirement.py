"""STEP-2 requirement extraction service. ICS service, be.service_requirement."""
from app.features.requirements.providers.requirement_extractor import extract_requirements

def service_requirement(value:str)->str:
    """Expose deterministic actor/action extraction, without pretending full design."""
    result=extract_requirements(value)
    return "Actors: "+", ".join(result["actors"])+"; actions: "+", ".join(result["actions"])
