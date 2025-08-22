from flask import Flask
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import pandas as pd

app = Flask(__name__)

def build_model():
    model = Sequential([
        Input(shape=(2,)),            # Correct way to specify input shape
        Dense(64, activation='relu'), # First hidden layer
        Dense(16, activation='relu'), # Second hidden layer
        Dense(1)                      # Output layer (linear activation by default)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Build model once, outside request handlers
model = build_model()

@app.route('/')
def index():
    return 'Model ready and warning-free!'

if __name__ == '__main__':
    app.run(debug=True)
