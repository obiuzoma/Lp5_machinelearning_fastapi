from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class SepssisFeatures(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: float
    Insurance: float
   
knn_pipeline = joblib.load("./models/knn_pipeline.joblib")
encoder = joblib.load("./models/label_encoder.joblib")
    
@app.get('/')
def home(Name=None):
    return{'status Health:' 'Ok'}


@app.post('/predict_knn')
def knn_predict(data:SepssisFeatures):

    # convert model to dictionary and then to an array
    df = pd.DataFrame([data.model_dump()])

  

    # make prediction
    prediction = knn_pipeline.predict(df)

    # convert prediction to int instade of an array
    prediction = int(prediction[0])

    # converts prediction using encoder
    prediction = encoder.inverse_transform([prediction])[0]

      # convert the prediction to probability
    probability = knn_pipeline.predict_proba(df)

    # conver probabgilities to list
    probability = probability.tolist()
    
    # return prediction
    return {"prediction": prediction, 'probability': probability}

@app.get('/document')
def documentation():
    return{'description': 'All documents'}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
