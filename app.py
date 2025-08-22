from flask import Flask
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

app = Flask(__name__)

def build_model():
    model = Sequential([
        Input(shape=(2,)),          # Correct input layer, no input_dim in Dense
        Dense(64, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

model = build_model()

def train_model():
    # Make sure 'data.csv' exists in the same folder with columns: Feature1, Feature2, Output
    df = pd.read_csv('data.csv')
    X = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    model.fit(X, y, epochs=1000, verbose=0)
    return model

@app.route('/')
def index():
    return 'Model is built and ready!'

if __name__ == '__main__':
    app.run(debug=True)
