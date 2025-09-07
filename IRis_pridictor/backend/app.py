from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import pridict_output, MODEL_VERSION
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
# Initialize FastAPI app
app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the Iris Flower Prediction API!"}

@app.get('/version')
def get_version():
    return {
        'status': 'ok',
        'model_version': MODEL_VERSION,
        'model_type': 'Iris Flower Classification',
        'model_author': 'LAFFI'
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_types(input: UserInput):
    input_dict = input.model_dump()
    user_input = {
        'sepal length (cm)': input_dict['sepal_length'],
        'petal width (cm)': input_dict['petal_width']
    }
    try:
        model_prediction = pridict_output(user_input)
        return JSONResponse(status_code=200, content=model_prediction)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})