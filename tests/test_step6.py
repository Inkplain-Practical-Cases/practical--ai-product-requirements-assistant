from app.features.requirements.services.end_to_end import analyse_brief

def test_full_traceability():
    out=analyse_brief("manager can approve request")
    assert len(out["stories"])==1
    assert out["design"]["traceability"][0]["process"] in out["design"]["flow"]["nodes"]
def test_unknowns_preserved():
    assert analyse_brief("missing details")["requires_review"]
