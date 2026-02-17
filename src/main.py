# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Aprendizaje Automático
# Profesor: Jesús Salvador López Ortega
# Archivo: main.py
# Descripción: Evaluación del primer bloque
# ============================================================

import os
import sys
from logging import DEBUG, ERROR, INFO, WARNING

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.logger import get_logger, plogger, set_logger

set_logger(file_path=__file__, level=INFO)
logger = get_logger(__name__)


def plot_model(pipeline, X_test, y_test, y_pred, dir="./build/out"):
    """
    Genera gráficos para evaluar el modelo:
    1. Valores reales vs predichos.
    2. Distribución de residuos.
    """
    # Gráfico de valores reales vs predichos
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, color="blue", edgecolor="k")
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--",
        lw=2,
    )
    plt.xlabel("Ventas reales")
    plt.ylabel("Ventas predichas")
    plt.title("Regresión lineal múltiple: Ventas reales vs predichas")
    plt.grid(True)
    plt.savefig(os.path.join(dir, "real_vs_predicted.png"))

    # Gráfico de residuos
    residuals = y_test - y_pred
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.7, color="green", edgecolor="k")
    plt.axhline(y=0, color="red", linestyle="--")
    plt.xlabel("Ventas predichas")
    plt.ylabel("Residuos")
    plt.title("Distribución de residuos")
    plt.grid(True)
    plt.savefig(os.path.join(dir, "residuals.png"))


def run_pipeline(csv_path="./inputs/ventas_motores.csv"):
    """
    Ejecuta el flujo de trabajo de regresión lineal múltiple:
    1. Carga datos.
    2. Preprocesa variables.
    3. Entrena y evalúa el modelo.
    4. Genera gráficos y coeficientes.
    """

    # Inicializar todas las variables en None
    df = None
    X = None
    y = None
    pipeline = None
    y_pred = None

    try:
        # TODO: Cargar los datos desde el archivo CSV
        # Se requiere que guardes los datos en un DataFrame llamado "df"
        df = None

        # TODO: Definir las variables independientes (X) y la variable objetivo (y) como objetos Series
        #       - "X" debe incluir todas las columnas relevantes, menos la de la variable 
        #         objetivo y datos sin correlacion como el año del modelo. 
        #       - "y" debe ser la columna del valor que estamos tratando de predecir, revisa
        #         los detalles del problema planteado para deducirla.
        X = None
        y = None

        # TODO: Preprocesamiento de las variables
        # En este paso se construye un objeto ColumnTransformer que aplica diferentes
        # transformaciones según el tipo de variable:
        #
        # - OneHotEncoder: convierte variables categóricas de X (como "Modelo") en vectores
        #   binarios. Cada categoría se transforma en una columna independiente con 0/1.
        #
        # - StandardScaler: normaliza las variables numéricas de X ("Potencia_HP",
        #   "Precio_Base", "Promociones") para que tengan media 0 y desviación estándar 1.
        #
        # Debes completar la estructura para que el preprocesador aplique estas
        # transformaciones correctamente.
        preprocessor = ColumnTransformer(
            transformers=[
                ("cat", OneHotEncoder(), None),
                ("num", StandardScaler(), None),
            ]
        )

        # TODO: Construir un Pipeline para la regresión lineal múltiple
        # Concepto:
        # Un Pipeline en scikit-learn permite encadenar varios pasos de procesamiento
        # y modelado en una sola estructura. Esto asegura que:
        #   - Los datos siempre pasen primero por el preprocesamiento (transformaciones).
        #   - Después se apliquen al modelo de regresión lineal.
        #
        # En este caso:
        #   - Paso "preprocessor": aplica OneHotEncoder a la variable categórica
        #     y StandardScaler a las variables numéricas. 
        #     Hiciste esto en el paso anterior.
        #   - Paso "regressor": entrena un modelo de regresión lineal múltiple
        #     sobre los datos ya transformados.
        #
        # La idea es que el Pipeline automatiza el flujo completo:
        #   X → preprocesamiento → regresión lineal → predicciones
        #
        # Debes completar la estructura para que el Pipeline incluya estos dos pasos.
        pipeline = Pipeline(
            [
                (None, None)
            ]
        )

        # TODO: Entrenar y evaluar el modelo
        # Concepto:
        # En esta etapa separamos los datos en dos conjuntos:
        #   - X_train, y_train: datos de entrenamiento, usados para ajustar el modelo.
        #   - X_test, y_test: datos de prueba, usados para evaluar el modelo con
        #     información que nunca ha visto durante el entrenamiento.
        #
        # La función train_test_split realiza esta división. El parámetro test_size=0.2
        # indica que el 20% de los datos se reserva para prueba. El random_state=42
        # asegura reproducibilidad (siempre la misma división).
        #
        # Después:
        #   - Entrena el modelo con los datos de entrenamiento.
        #   - Genera predicciones sobre los datos de prueba.
        #
        # El objetivo es comparar y_test (valores reales) con y_pred (valores predichos)
        # para medir el desempeño del modelo.
        #
        # Debes completar el código para que el modelo se entrene y se evalúe.
        X_train, X_test, y_train, y_test = None, None, None, None
        y_pred = None

        # Evaluación de métricas
        plogger(f"R²: {r2_score(y_test, y_pred)}")
        plogger(f"RMSE: {root_mean_squared_error(y_test, y_pred)}")

        # Interpretación de coeficientes
        regressor = pipeline.named_steps["regressor"]
        plogger(f"Coeficientes: {regressor.coef_[0]}")
        plogger(f"Intercepto: {regressor.intercept_}")

        # Graficación del modelo
        plot_model(pipeline, X_test, y_test, y_pred)
        
    except Exception as e:
        plogger(f"Revisa tu procedimiento: {e}", level=ERROR)

    # Return para evaluación       
    return {
        "df": df             if df       != None else None,
        "X": X               if X        != None else None,
        "y": y               if y        != None else None,
        "pipeline": pipeline if pipeline != None else None,
        "y_pred": y_pred     if y_pred   != None else None,
    }


def main():
    """Función principal del programa."""
    try:
        logger.info("Iniciando programa...")
        run_pipeline()

    except OSError as e:
        plogger(f"OSError [{e.errno}]: {os.strerror(e.errno)}", level=ERROR)
        return os.EX_SOFTWARE

    except Exception:
        logger.exception("Error inesperado")
        return os.EX_SOFTWARE

    logger.info("Programa finalizado correctamente.")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())