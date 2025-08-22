from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def train_model():
    df = pd.read_csv('data.csv')
    X = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    model = Sequential([
        Input(shape=(2,)),           # Input layer with shape only here
        Dense(64, activation='linear'),
        Dense(16, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=1000, verbose=0)

    return model
