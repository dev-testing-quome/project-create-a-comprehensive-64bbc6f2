import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
from .routers import users, appointments, messages, medical_records, prescriptions, billing
from . import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency Injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router inclusion
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(messages.router)
app.include_router(medical_records.router)
app.include_router(prescriptions.router)
app.include_router(billing.router)

# Health check endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Static files serving
if os.path.exists('static'):
    app.mount('/static', StaticFiles(directory='static'), name='static')

    @app.get('/{file_path:path}')
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith('api'):
            return None
        static_file = os.path.join('static', file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse(os.path.join('static', 'index.html'))

# Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})

# Start the server
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
