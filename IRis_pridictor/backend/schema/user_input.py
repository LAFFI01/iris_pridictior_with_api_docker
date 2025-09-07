from pydantic import BaseModel, Field
from typing import Annotated

class UserInput(BaseModel):
    sepal_length: Annotated[float, Field(gt=0, lt=10, description="Sepal length in cm", example=5.1)]
    petal_width: Annotated[float, Field(gt=0, lt=10, description="Petal width in cm", example=0.2)]
