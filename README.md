# Game AI Controller

Este proyecto implementa un sistema basado en aprendizaje automático para controlar un juego mediante una red neuronal. El sistema captura imágenes de la pantalla, predice las acciones a realizar y simula la pulsación de teclas para interactuar con el juego.

## 📂 Estructura del Proyecto

- `__main__.py`: Ejecuta el sistema de control del juego en tiempo real.
- `capture_train_data.py`: Captura datos de entrenamiento (imágenes y entradas del teclado).
- `inference.py`: Carga el modelo entrenado y realiza inferencias sobre las imágenes capturadas.
- `training.ipynb`: Script en Jupyter Notebook para entrenar el modelo de aprendizaje automático.

## 📌 Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install tensorflow numpy opencv-python keyboard pygetwindow pillow
```

## 🔍 Captura de Datos para Entrenamiento

Para capturar imágenes y sus respectivas entradas del teclado:

```bash
python capture_train_data.py
```

El script capturará la pantalla y las teclas presionadas, guardándolas en el directorio `train_data`.

## 🎯 Entrenamiento del Modelo

El entrenamiento se realiza en el archivo `training.ipynb`. Asegúrate de cargar los datos capturados antes de entrenar el modelo.

![image](https://github.com/user-attachments/assets/fc221a3b-4251-45ba-af90-60cda437a0e5)


## 🕹️ Ejecución del Controlador del Juego

Para ejecutar el modelo en tiempo real y controlar el juego:

```bash
python __main__.py
```

El script tomará capturas de pantalla del juego, realizará predicciones y enviará comandos de teclado en consecuencia.

## 🔧 Funcionamiento

1. **Captura de pantalla**: Se obtiene la imagen de la ventana del juego.
2. **Preprocesamiento**: Se ajusta el tamaño de la imagen y se normaliza.
3. **Inferencia**: Se pasa la imagen al modelo para predecir las acciones.
4. **Control del teclado**: Se activan las teclas correspondientes a la predicción.

## ⚙️ Configuración Importante

- `GAME_WINDOW_NAME`: Nombre exacto de la ventana del juego.
- `THRESHOLD`: Umbral de activación de teclas basado en la predicción del modelo.
- `MODEL_PATH`: Ruta del modelo de red neuronal entrenado.

## 🚀 Mejoras Futuras

- Mejorar la precisión del modelo con más datos de entrenamiento.
- Optimización del tiempo de inferencia.
- Soporte para múltiples juegos.

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.

