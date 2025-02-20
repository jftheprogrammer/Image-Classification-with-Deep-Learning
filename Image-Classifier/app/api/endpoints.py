from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from app.models.classifier import ImageClassifier
from app.utils.database import SessionLocal, Prediction
from app.utils.auth import get_current_user
from PIL import Image
import requests
from io import BytesIO

router = APIRouter()
classifier = ImageClassifier()

class PredictionRequest(BaseModel):
    image_url: str

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float

@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, user: str = Depends(get_current_user)):
    try:
        response = requests.get(request.image_url)
        image = Image.open(BytesIO(response.content))
        prediction = classifier.predict(image)
        
        # Save prediction to database
        db = SessionLocal()
        db_prediction = Prediction(image_url=request.image_url, prediction=prediction, confidence=abs(prediction - 0.5))
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        db.close()
        
        return {"prediction": prediction, "confidence": abs(prediction - 0.5)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))