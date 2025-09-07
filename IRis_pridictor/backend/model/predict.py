import pandas as pd 
import pickle
import os 
# Load the trained model from a pickle file
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

class_labels =  ['setosa', 'versicolor', 'virginica']

def pridict_output(user_input:dict):
    
    df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(df)[0]
    
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    class_probs  = dict(zip(class_labels, probabilities))
    result = {
        "predicted_iris": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probs
    }
    return result
    # input_data = pd.DataFrame([user_input])
    # model_prediction = model.predict(input_data)[0]
    # return model_prediction
