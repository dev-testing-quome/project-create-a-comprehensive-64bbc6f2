import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models
from .routers import users, appointments, messages, medical_records, prescriptions, billing
from .schemas import HTTPError

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Configuration
origins = ["*"]  # In production, replace with your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency Injection for Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router Inclusion
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(messages.router)
app.include_router(medical_records.router)
app.include_router(prescriptions.router)
app.include_router(billing.router)

# Health Check Endpoint
@app.get("/health", status_code=200)
def health_check():
    return {"status": "healthy"}

# Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    # Log the error
    print(f'Unhandled exception: {exc}')
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

# Static File Serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path.startswith("static"):
            return None  # Let API routes and static files handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")  # SPA routing

# OpenAPI Documentation
app.openapi_url = "/openapi.json"

# Run the application (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)