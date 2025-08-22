from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def train_model():
    df = pd.read_csv('data.csv')
    X = df[['Feature1', 'Feature2']].values
    y = df[['Output']].values

    model = Sequential()
    model.add(Input(shape=(2,)))         # Define input shape explicitly
    model.add(Dense(64, activation='linear'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=1000, verbose=0)

    return model


