import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model():
    # Load dataset
    df = pd.read_csv('data.csv')

    # Inputs and outputs
    x = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    # Build improved model
    model = Sequential()
    model.add(Dense(32, input_dim=2, activation='linear'))  # try 'linear' instead of 'relu'
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1))  # output

    # Compile and train
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x, y, epochs=1000, verbose=0)  # train longer

    return model
