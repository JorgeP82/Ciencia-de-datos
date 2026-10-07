# PROYECTO: ANALISIS DESCRIPTIVO DE VARIACIONES OPERATIVAS
# APLICACION: Control de Gestión y Reporting para Banco
# Autor: Jorge Pecina

import pandas as pd
import numpy as np

def analizar_variaciones(ruta_archivo):
    print("=== Inicializando Análisis de Calidad del Dato ===")
    # Simulación de carga y limpieza de datos (Librería Pandas)
    # Requisito Banco: 'Limpieza de datos y control de calidad del dato'
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        # Generación de dataset sintético para demostración analítica
        np.random.seed(42)
        datos = {
            'ID_Operacion': range(1, 101),
            'Monto_Presupuestado': np.random.normal(50000, 10000, 100),
            'Monto_Real': np.random.normal(51500, 11000, 100)
        }
        df = pd.DataFrame(datos)
    
    # Cálculo de Variaciones Absolutas y Porcentuales (Regla de Negocio)
    df['Variacion_Absoluta'] = df['Monto_Real'] - df['Monto_Presupuestado']
    df['Variacion_Porcentual'] = (df['Variacion_Absoluta'] / df['Monto_Presupuestado']) * 100
    
    # Requisito Banco: 'Fundamentos de estadística descriptiva'
    resumen_estadistico = {
        'Media Presupuesto': df['Monto_Presupuestado'].mean(),
        'Media Real': df['Monto_Real'].mean(),
        'Desviación Estándar Presupuesto': df['Monto_Presupuestado'].std(),
        'Variación Promedio (%)': df['Variacion_Porcentual'].mean(),
        'Máxima Variación Negativa': df['Variacion_Absoluta'].min(),
        'Máxima Variación Positiva': df['Variacion_Absoluta'].max()
    }
    
    print("\n=== RESUMEN ESTADÍSTICO DE VARIACIONES ===")
    for k, v in resumen_estadistico.items():
        print(f"{k}: {v:,.2f}")
        
    return df

if __name__ == "__main__":
    # Ejecución del pipeline analítico
    df_analizado = analizar_variaciones('datos_gestion.csv')
