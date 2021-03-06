from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class Model:

    # This model represents the AI that the game will
    # ask for moves given some data.

    def __init__(self, weights=None):

        # Construct the model below using
        # model.add(...)
        self.model = Sequential()
        self.model.add(Dense(3, input_shape=(4,)))
        self.model.add(Dense(1))

    def get_weights(self):

        return self.model.get_weights()

    def reset_weights(self):

        shapes = [w.shape for w in self.model.get_weights()]

        new_weights = []
        for s in shapes:

            new_weights.append(np.random.uniform(-1.0, 1.0, size=s))

        self.model.set_weights(new_weights)

    def evaluate_move(self, data):

        eval = np.argmax([self.model.predict(np.array(x).reshape(1, 4))[0][0] for x in data])

        if eval == 0:
            return -1
        if eval == 1:
            return 0
        if eval == 2:
            return 1
