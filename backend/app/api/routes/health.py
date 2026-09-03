from datetime import UTC,datetime
from fastapi import APIRouter
from app.core.config import get_settings
router=APIRouter()
@router.get('/health')
def health():return {'status':'ok','service':'aerotrack-api','mode':'demo' if get_settings().demo_mode else 'live','timestamp':datetime.now(UTC)}
