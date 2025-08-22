from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np

X = np.random.random((10, 2))
y = np.random.random((10, 1))

model = Sequential([
    Input(shape=(2,)),
    Dense(64, activation='linear'),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=1)

