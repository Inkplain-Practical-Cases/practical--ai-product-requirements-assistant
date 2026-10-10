"""Traceable conceptual data-flow model from explicit user stories."""
def build_data_flow(stories:list[dict])->dict:
    """Create named actor/process/store edges; never infer extra services."""
    nodes={};edges=[]
    for i,record in enumerate(stories):
        story=record.get("story","")
        actor=story.split(",")[0].removeprefix("As a ").strip() or "unknown"
        a="actor:"+actor;p=f"process:{i}"
        nodes[a]={"kind":"actor","name":actor}
        nodes[p]={"kind":"process","name":"Review story "+str(i+1)}
        edges.append({"from":a,"to":p,"data":"requested action"})
    return {"nodes":nodes,"edges":edges,"human_review":True}
