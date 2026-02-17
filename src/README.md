# Evaluación Primer Bloque

## Regresión Lineal Múltiple para Predicción de Ventas

## 1. Contexto del Problema

Una tienda especializada en la venta de motores industriales desea **predecir la cantidad de ventas anuales** de sus distintos modelos.

Se cuenta con una base de datos histórica con información como la siguiente:

| Año  | Modelo | Potencia_HP | Precio_Base | Promociones | Ventas |
| ---- | ------ | ----------- | ----------- | ----------- | ------ |
| 2020 | MTR-A  | 150         | 12000       | 2           | 340    |
| ...  | ...    | ...         | ...         | ...         | ...    |

El objetivo es diseñar un **modelo de regresión lineal múltiple** que permita estimar las ventas (`Ventas`) en función de distintas variables descriptivas del producto y su comercialización.

---

## 2. Fundamento Teórico

### 2.1 ¿Qué es la Regresión Lineal Múltiple?

La **regresión lineal múltiple** es un modelo supervisado que permite predecir una variable numérica continua a partir de varias variables independientes.

Se basa en la siguiente forma matemática:

[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
]

Donde:

* ( y ) → Variable objetivo (Ventas)
* ( x_i ) → Variables independientes (precio, potencia, promociones, etc.)
* ( \beta_i ) → Coeficientes que representan el impacto de cada variable
* ( \beta_0 ) → Intercepto

El modelo aprende los coeficientes que minimizan el error entre valores reales y predichos.

---

### 2.2 Aprendizaje Supervisado

Este problema pertenece al tipo:

* ✅ **Supervisado**
* ✅ **Regresión**
* ✅ **Predicción cuantitativa**

Se dispone de datos históricos etiquetados (sabemos las ventas reales), por lo que el modelo puede aprender la relación entre variables.

---

## 3. Flujo Metodológico del Ejercicio

El ejercicio está estructurado siguiendo una **pipeline profesional de Machine Learning**:

### 3.1 Carga de datos

Se deben cargar los datos desde un archivo CSV y almacenarlos en un DataFrame.

---

### 3.2 Definición del problema

Se deben identificar:

* **Variables independientes (X)**
  Factores que influyen en las ventas.

* **Variable objetivo (y)**
  La variable que queremos predecir.

Se debe reflexionar cuáles columnas aportan información relevante y cuáles no tienen correlación directa con el fenómeno.

---

### 3.3 Preprocesamiento de datos

En Machine Learning, los modelos no trabajan directamente con datos crudos.

Se requiere:

#### Variables categóricas

Ejemplo: `Modelo`

Los modelos matemáticos no entienden texto, por lo que se debe aplicar:

* **One-Hot Encoding**

  * Convierte cada categoría en una columna binaria (0/1).

#### Variables numéricas

Ejemplo:

* Potencia_HP
* Precio_Base
* Promociones

Estas deben escalarse para:

* Evitar sesgos por magnitudes distintas
* Mejorar estabilidad numérica

Se utiliza:

* **StandardScaler**

  * Media = 0
  * Desviación estándar = 1

---

### 3.4 Pipeline

Un **Pipeline** en scikit-learn permite encadenar:

```
Preprocesamiento → Modelo → Predicción
```

Ventajas:

* Automatiza el flujo completo
* Evita errores de fuga de datos
* Hace el código más limpio y profesional
* Permite reproducibilidad

---

### 3.5 División de Datos

Se deben dividir los datos en:

* **Entrenamiento (80%)**
* **Prueba (20%)**

Esto permite evaluar el modelo con datos que no ha visto antes.

Es fundamental para evitar sobreajuste.

---

### 3.6 Evaluación del Modelo

Se utilizarán dos métricas:

#### R² (Coeficiente de determinación)

Mide qué proporción de la varianza de la variable objetivo es explicada por el modelo.

* 1 → Ajuste perfecto
* 0 → No explica nada

---

#### RMSE (Root Mean Squared Error)

Mide el error promedio en las mismas unidades que la variable objetivo.

Interpretación:

* Mientras menor sea, mejor es el modelo.

---

### 3.7 Análisis de Residuos

Se generarán dos gráficas:

* Valores reales vs predichos
* Distribución de residuos

Esto permite analizar:

* Linealidad
* Homocedasticidad
* Posibles patrones no modelados

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)