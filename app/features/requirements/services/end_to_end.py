"""End-to-end requirement analysis: evidence-constrained drafts and traceability."""
from app.features.requirements.services.user_story_builder import build_user_stories
from app.features.requirements.services.system_design import propose_system_design

def analyse_brief(brief:str)->dict:
    """Expose explicit ambiguity to human reviewers without fabricated requirements."""
    if len(brief.strip())<3:raise ValueError("Brief too short")
    stories=build_user_stories(brief)
    design=propose_system_design(stories)
    return {"stories":stories,"design":design,"unknowns":[] if stories else ["Actor/action missing"],"requires_review":True}
