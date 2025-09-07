from pydantic import BaseModel, Field
from typing import Annotated,Dict 

class PredictionResponse(BaseModel):
    predicted_iris: Annotated[str, Field(description="Predicted Iris species", example="Iris-setosa")]
    confidence: Annotated[float, Field(description="Confidence score of the prediction", example=0.95)] 
    class_probabilities: Annotated[Dict[str, float], Field(description="Probabilities for each Iris species", example={"setosa": 0.95, "versicolor": 0.03, "virginica": 0.02})]
    
    