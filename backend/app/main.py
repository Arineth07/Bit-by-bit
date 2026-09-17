from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HackForge API",
    description="Hackathon & Student Project Management Platform",
    version="0.1.0",
)

# CORS: Allow the frontend (running on a different port) to call our API.
# In development, we allow all origins. In production, lock this down.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """Health check endpoint. If this returns, the server is running."""
    return {"message": "HackForge API is running"}


@app.get("/health")
def health_check():
    """More explicit health check for monitoring tools."""
    return {"status": "healthy"}
