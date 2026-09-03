from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routes import aircraft,flights,health,history
from app.core.config import get_settings
s=get_settings();app=FastAPI(title=s.app_name,version='1.0.0',description='Normalized aviation tracking API for AeroTrack')
app.add_middleware(CORSMiddleware,allow_origins=[s.frontend_url.rstrip('/')],allow_credentials=True,allow_methods=['GET','POST','OPTIONS'],allow_headers=['*'])
app.include_router(health.router,prefix='/api',tags=['system']);app.include_router(aircraft.router,prefix='/api',tags=['aircraft']);app.include_router(flights.router,prefix='/api',tags=['flights']);app.include_router(history.router,prefix='/api',tags=['history'])
@app.exception_handler(Exception)
async def unexpected(_:Request,exc:Exception):return JSONResponse(status_code=500,content={'detail':'An unexpected error occurred','type':type(exc).__name__})
