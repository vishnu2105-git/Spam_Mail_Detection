from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np


model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

class_names = np.array(['spam', 'not spam'])

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # Allow requests from your React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {'message': 'Spam Mail Classifier API'}


@app.post("/predict")
def predict_spam(data: dict):
    try:

        message = data.get('message')
        if not message:
            raise HTTPException(status_code=400, detail="Message text is required")

        # Transform the input text using the loaded vectorizer
        features = vectorizer.transform([message])

        prediction = model.predict(features)
        class_name = class_names[prediction[0]]

        return {'Predicted_Class': class_name}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
