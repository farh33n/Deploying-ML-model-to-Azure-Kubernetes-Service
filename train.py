# trains a regression model and saves it

import numpy as np
import pandas as pd
import os
import sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

#loads the data set
diabetes_dataset = load_diabetes()

x_train, x_test, y_train, y_test = train_test_split(diabetes_dataset.data, diabetes_dataset.target)


# implements linear regression model
reg_model = LinearRegression()
reg_model.fit (x_train, y_train)

# saves the trained model
os.makedirs("outputs", exist_ok=True)
model_name = "reg_model.pkl"
model_dir = "outputs"
joblib.dump(value=reg_model, filename=model_dir + "/" + model_name)
