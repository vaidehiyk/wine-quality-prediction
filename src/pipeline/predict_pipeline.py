import pickle
import numpy as np

class PredictPipeline:
    def __init__(self):
        self.model = pickle.load(open('artifacts/wine_prediction_model.pkl', 'rb'))
        self.scaler = pickle.load(open('artifacts/scaler.pkl', 'rb'))

    def predict(self, features):
        data = np.array(features).reshape(1, -1)
        scaled_data = self.scaler.transform(data)
        prediction = self.model.predict(scaled_data)
        return prediction[0]