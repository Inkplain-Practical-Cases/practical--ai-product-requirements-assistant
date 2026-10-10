"""User story builder: human-reviewable drafts with testable acceptance criteria.
ICS service; component be.build_user_stories. STEP-3.
"""
from app.features.requirements.providers.requirement_extractor import extract_requirements

def build_user_stories(brief:str)->list[dict]:
    """Create explicit actor/action drafts without inventing unprovided business outcomes."""
    extracted=extract_requirements(brief)
    stories=[]
    for actor in extracted["actors"]:
        for action in extracted["actions"]:
            if "unspecified" in (actor,action):continue
            stories.append({"story":f"As a {actor}, I want to {action} so that the requested business action can be performed.",
              "acceptance_criteria":[f"Given an authorized {actor}, when I request {action}, then the service returns an explicit result.",f"Given missing input, when I request {action}, then validation fails."],
              "requires_human_review":True})
    return stories
