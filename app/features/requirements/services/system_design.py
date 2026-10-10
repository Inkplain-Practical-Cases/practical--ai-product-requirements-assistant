"""Minimal traceable system design proposal for approved user stories."""
from app.features.requirements.services.data_flow_builder import build_data_flow

def propose_system_design(stories:list[dict])->dict:
    """Derive an API proposal only from visible workflow traceability."""
    flow=build_data_flow(stories)
    return {"api":[{"method":"POST","path":"/api/requirements","purpose":"submit reviewable requirements"}],
            "flow":flow,"assumptions":["All proposed interfaces require stakeholder review"],
            "traceability":[{"story_index":i,"process":f"process:{i}"} for i,_ in enumerate(stories)],
            "status":"draft_human_review_required"}
