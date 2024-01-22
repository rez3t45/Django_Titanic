# Predicción de Supervivencia en el Titanic

Este proyecto se enfoca en predecir la supervivencia de los pasajeros a bordo del Titanic utilizando machine learning. Varios modelos fueron evaluados, y el K-Nearest Neighbors (KNN) fue seleccionado como el modelo final para realizar las predicciones.

## Contenido del Repositorio

### Archivos del Código Fuente
- `titanic_model.ipynb`: Jupyter Notebook que contiene el análisis de datos, la selección del modelo y el entrenamiento del modelo KNN.
- `titanic_predictor.py`: Script de Python que implementa la funcionalidad de predicción utilizando el modelo KNN entrenado.

### Archivos de Datos
- `Titanic_train.csv`: Conjunto de datos de entrenamiento utilizado para entrenar y evaluar los modelos.
- `Titanic_test.csv`: Conjunto de datos de prueba utilizado para realizar predicciones.

### Archivos de Configuración
- `requirements.txt`: Lista de dependencias y versiones de Python necesarias para ejecutar el código.
- `environment.yml`: Archivo de entorno con las dependencias para crear un entorno de Conda.

### Archivos Web
- `templates/index.html`: Página HTML para ingresar datos y ver la predicción en un entorno web.
- `static/css/styles.css`: Hoja de estilos CSS para dar formato a la interfaz web.

### Otros Archivos
- `README.md`: Este archivo que proporciona información general sobre el proyecto.

## Instrucciones de Uso

1. Instalar las dependencias necesarias ejecutando `pip install -r requirements.txt` o creando un entorno de Conda con `conda env create -f environment.yml`.
2. Ejecutar el archivo Jupyter Notebook `titanic_model.ipynb` para realizar el análisis de datos, seleccionar el modelo y entrenarlo.
3. Ejecutar `python titanic_predictor.py` para realizar predicciones utilizando el modelo KNN entrenado.
4. Para una interfaz web, ejecutar una aplicación Django con `python manage.py runserver` y acceder a `http://localhost:8000` en el navegador.

## Notas Adicionales

- El modelo KNN se eligió después de evaluar varios modelos y se ajustó para obtener resultados óptimos.
- La interfaz web proporciona una forma fácil de ingresar datos y obtener predicciones de supervivencia.
- Asegúrese de tener instaladas las bibliotecas mencionadas en `requirements.txt` antes de ejecutar el código.

Este proyecto ofrece una solución integral para la predicción de supervivencia en el Titanic, desde el análisis de datos hasta la implementación en una interfaz web interactiva.
