from app.features.requirements.services.data_flow_builder import build_data_flow

def test_edges_have_valid_nodes():
    model=build_data_flow([{"story":"As a manager, I want to approve"}])
    assert all(e["from"] in model["nodes"] and e["to"] in model["nodes"] for e in model["edges"])
    assert model["human_review"]
