Practica 17, caso de estudio para aplicar el BSPF y visualización de datos

Descripción del proyecto:
El proyecto se divide en dos secciones principales:
1.- Explicación y desglose de los 7 pasos de Business Science Performance Framework aplicado a un caso práctico de "Fuga de cleintes"
2.- Viaualización de datos, implementación de gráficos no convencionales con la herramienta "Orange Data Minning" utilizando el dataset
clínico 'heart_desease.tab'

Graficos implementados en Orange 
1.- Violin plot: Análisis de la distribución completa de los niveles de colesterol según el diagnóstico
2.- Mosaic display: cruce de variables categóricas para identificar patrones del tipo dolor de pecho vs. diagnóstico
3.- Sieve diagram: viasualización de la relación y nivel de independencia entre el sexo de los pacientes y el diagnóstico 

#  Práctica 18: Clasificación de Medicamentos con Enfoque Ágil
**Descripción del proyecto:** 
Este módulo resuelve un caso clínico y de negocio sobre un histórico de 200 pacientes. El objetivo es construir un modelo predictivo capaz de recomendar de forma óptima cuál de 5 medicamentos es el adecuado para un nuevo paciente según sus variables (Edad, Presión Arterial, Colesterol y relación Sodio/Potasio).

*   **Archivo fuente:** `Práctica M18.ows` (Flujo analítico ejecutable).
*   **Enfoque Ágil:** A diferencia del desarrollo tradicional en cascada, se evaluaron 5 algoritmos en paralelo (**Tree, kNN, Random Forest, Gradient Boosting y SVM**), permitiendo detectar fallas tempranas de rendimiento por falta de escalado en kNN y SVM.
*   **Reglas de Negocio Aprendidas (Modelo Tree):** El modelo seleccionado (Árbol de Decisión) identificó que si la relación Sodio/Potasio es **mayor a 14.83**, el fármaco idóneo siempre es el **Fármaco Y**. Si es menor, la Presión Arterial y la Edad definen con precisión los otros tratamientos, logrando un 100% de exactitud (CA=1.000) en el conjunto de prueba.

---

#  Proyecto: Control de Gestión y Análisis Descriptivo (Banco)
**Descripción del proyecto:** 
Script automatizado desarrollado en Python puro orientado a la auditoría presupuestaria, análisis de desvíos financieros y control de calidad del dato para la toma de decisiones estratégicas.

*   **Archivo fuente:** `analisis_descriptivo_variaciones.py`
*   **Manejo de Calidad del Dato:** Implementa un bloque de control de excepciones (`try-except`) que valida la correcta ingesta de archivos independientes (`datos_gestion.csv`) y previene interrupciones mediante generación controlada de datos sintéticos operacionales con la librería **Pandas**.
*   **Interpretación de Hallazgos Estadísticos:** El programa automatiza el cálculo de medias y variaciones. Identifica desviaciones críticas (como variaciones promedio sistemáticas del **10.74%** que requieren auditoría inmediata) y localiza fugas de dinero (máximas variaciones positivas) así como eficiencias operativas (máximas variaciones negativas) para replicar buenas prácticas de costos.
