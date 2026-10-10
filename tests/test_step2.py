from app.features.requirements.providers.requirement_extractor import extract_requirements

def test_extracts_explicit_actor_and_actions():
    assert extract_requirements("Admin can approve and update an order")=={"actors":["admin"],"actions":["approve","update"]}
def test_marks_ambiguity():
    assert extract_requirements("something")["actors"]==["unspecified"]
