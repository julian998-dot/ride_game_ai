from inference import GameController
from PIL import ImageGrab
import numpy as np
import cv2
import time
import keyboard
import pygetwindow as gw

# Configuración
MODEL_PATH = "game_controller_model.h5"
GAME_WINDOW_NAME = "RIDE 5"
THRESHOLD = 0.5  # Umbral para activación de teclas

class GameRunner:
    def __init__(self):
        self.controller = GameController(MODEL_PATH)
        self.game_window = None
        
    def get_game_window(self):
        try:
            win = gw.getWindowsWithTitle(GAME_WINDOW_NAME)[0]
            return win.left, win.top, win.right, win.bottom
        except:
            return None
    
    def press_keys(self, predictions):
        keys = [
            ('up', predictions[0]),
            ('down', predictions[1]),
            ('left', predictions[2]),
            ('right', predictions[3]),
            ('w', predictions[4]),
            ('a', predictions[5]),
            ('s', predictions[6]),
            ('d', predictions[7])
        ]
        
        # Liberar todas las teclas primero
        keyboard.release('up')
        keyboard.release('down')
        keyboard.release('left')
        keyboard.release('right')
        keyboard.release('w')
        keyboard.release('a')
        keyboard.release('s')
        keyboard.release('d')
        
        # Presionar teclas activas
        for key, active in keys:
            if active > THRESHOLD:
                keyboard.press(key)
    
    def run(self):
        self.game_window = self.get_game_window()
        if not self.game_window:
            print("Ventana del juego no encontrada!")
            return
        
        print("Iniciando control del juego (Presiona 'q' para salir)...")
        while True:
            if keyboard.is_pressed('q'):
                break
            
            # Capturar pantalla
            img = ImageGrab.grab(bbox=self.game_window)
            img = np.array(img)
            
            # Predecir
            predictions = self.controller.predict(img)
            
            # Controlar teclado
            self.press_keys(predictions)
            
            time.sleep(0.01)  # Ajustar según necesidad

if __name__ == "__main__":
    runner = GameRunner()
    runner.run()