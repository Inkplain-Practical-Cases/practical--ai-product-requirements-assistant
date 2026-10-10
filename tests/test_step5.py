from app.features.requirements.services.system_design import propose_system_design

def test_traceability_links_existing_nodes():
    out=propose_system_design([{"story":"As a manager, I want to approve"}])
    assert all(t["process"] in out["flow"]["nodes"] for t in out["traceability"])
    assert out["status"]=="draft_human_review_required"
