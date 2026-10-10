"""FastAPI composition root: register HTTP door only."""
from fastapi import FastAPI
from app.features.requirements.router import router
app = FastAPI(title="Requirement Starter Practical Case")
app.include_router(router)
