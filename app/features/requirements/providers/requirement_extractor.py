"""Deterministic extraction provider for learner fixtures; replaceable with LLM later."""
import re

def extract_requirements(text:str)->dict[str,list[str]]:
    """Capture simple explicit stakeholder actors and functional verbs."""
    words=re.findall(r"[A-Za-z]+",text.lower())
    actors=[w for w in ("customer","admin","employee","recruiter","manager") if w in words]
    verbs=[w for w in ("create","view","approve","search","update") if w in words]
    return {"actors":actors or ["unspecified"],"actions":verbs or ["unspecified"]}
