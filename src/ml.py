import keras
import numpy as np
class ML:
    model = None
    def __init__(self,filename):
        self.model = keras.models.load_model('./src/' + filename)

    def predict(self,seq_x):
        preidction = self.model.predict(seq_x)
        preidction = preidction[0][0]
        return preidction

