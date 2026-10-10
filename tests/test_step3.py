from app.features.requirements.services.user_story_builder import build_user_stories

def test_draft_needs_review():
    story=build_user_stories("manager approve request")[0]
    assert story["requires_human_review"] is True
    assert len(story["acceptance_criteria"])==2
def test_no_fabricated_actor():
    assert build_user_stories("something unknown")==[]
