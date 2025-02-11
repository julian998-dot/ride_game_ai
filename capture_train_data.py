import cv2
import numpy as np
import keyboard
from PIL import ImageGrab
import time
import os
import pygetwindow as gw

# Configuración
GAME_WINDOW_NAME = "RIDE 5"
IMG_SIZE = (224, 224)
DATA_DIR = "train_data"
FRAME_RATE = 0.1  # Segundos entre capturas

# Crear directorio si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_game_window():
    # Capturar la ventana del juego (requiere nombre exacto)
    try:
        win = gw.getWindowsWithTitle(GAME_WINDOW_NAME)[0]
        return win.left, win.top, win.right, win.bottom
    except:
        print("No se encuentra la ventana del juego!")
        return None

def capture_data():
    print("Presiona 'q' para terminar la captura")
    labels = []
    frame_count = 0
    bbox = get_game_window()
    
    while True:
        if keyboard.is_pressed('q'):
            break
            
        # Capturar pantalla
        img = ImageGrab.grab(bbox=bbox)
        img = np.array(img)
        img = cv2.resize(img, IMG_SIZE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Capturar teclas
        keys = [
            keyboard.is_pressed('up'),
            keyboard.is_pressed('down'),
            keyboard.is_pressed('left'),
            keyboard.is_pressed('right'),
            keyboard.is_pressed('w'),
            keyboard.is_pressed('a'),
            keyboard.is_pressed('s'),
            keyboard.is_pressed('d')
        ]
        
        # Guardar datos
        np.save(f"{DATA_DIR}/frame_{frame_count}.npy", img)
        labels.append(keys)
        
        frame_count += 1
        time.sleep(FRAME_RATE)
    
    # Guardar labels
    np.save(f"{DATA_DIR}/labels.npy", np.array(labels))
    print(f"Datos capturados: {frame_count} frames")

if __name__ == "__main__":
    capture_data()