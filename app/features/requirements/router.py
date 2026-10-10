"""HTTP door: validate typed request and delegate to handler.
ICS layer: door
CRD component: be.receive_requirement
Called by: REST clients
Calls: handle_requirement
Why: keeps HTTP and business rules separate.
Without: validation and orchestration become coupled.
Step: added in STEP-1.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.features.requirements.handlers.handle_requirement import handle_requirement
router = APIRouter(prefix="/api", tags=["requirements"])
class RequirementRequest(BaseModel):
    brief: str = Field(min_length=3, max_length=2500)
class RequirementResponse(BaseModel):
    status: str
    detail: str
@router.post("/requirements", response_model=RequirementResponse)
def receive_requirement(request: RequirementRequest) -> RequirementResponse:
    # Every request is validated before the handler sees it.
    return RequirementResponse(**handle_requirement(request.brief))
