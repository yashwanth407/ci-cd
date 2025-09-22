import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model():
    # Load data
    df = pd.read_csv('data.csv')
    X = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    # Define model using Input layer to avoid warnings
    model = Sequential([
        tf.keras.Input(shape=(2,)),  # Recommended way to specify input shape
        Dense(32, activation='linear'),
        Dense(16, activation='relu'),
        Dense(1)
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train model
    model.fit(X, y, epochs=1000, verbose=0)

    return model

if __name__ == '__main__':
    model = train_model()
    model.save('trained_model.h5')
    print("Model trained and saved as trained_model.h5")
