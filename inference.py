import tensorflow as tf
import numpy as np
import cv2

class GameController:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.img_size = (224, 224)
        
    def preprocess(self, img):
        img = cv2.resize(img, self.img_size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img / 255.0
    
    def predict(self, img):
        processed = self.preprocess(img)
        prediction = self.model.predict(np.array([processed]))
        return prediction[0]  # Vector de 8 elementos
