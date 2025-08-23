import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def train_model():
    # Load data
    df = pd.read_csv('data.csv')
    X = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    # Define model using Input layer to avoid warnings
    model = Sequential([
        Input(shape=(2,)),   # Correct way
        Dense(64, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1)
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train model
    model.fit(X, y, epochs=1000, verbose=0)

    return model

