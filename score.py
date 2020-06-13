import json
import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path(model_name='regression_model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = np.array(json.loads(raw_data)['data']).reshape(1,-1)
        # make prediction
        y_pred = model.predict(data)
        # you can return any data type as long as it is JSON-serializable
        return y_pred.tolist()
    except Exception as e:
        error = str(e)
        return error

  
