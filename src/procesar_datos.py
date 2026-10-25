import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def cargardatos(filepath):
    #CARGA UN ARCHIVO EXPORTADO DE PASCO CAPSTONE (CSV O TXTdelimitado por comas/tabulaciones).
    df=pd.read_csv(filepath, delimiter=None, engine='python')
    df.colums= df.columns.str.strip() #Elimina espacios en blanco de los nombres de las columnas
    return df

def calcular_fft(t, x, fs):
    "Calcula la Transformada Rápida de"
    "Fourier para identificar frecuencias principales."
    "t: Serie de tiempo (s)"
    "x: Serie de posicion (m)"
    "fs: Frecuencia de muestreo (Hz)"
    N=len(x) #cuenta el numero total de datos que tiene el experimento
    yf= np.fft.fft(x)
    xf=np.fft.fftfreq(N,1/fs)[:N//2]
    amplitud = 2.0/N*np.abs(yf[0:N//2])
    return xf, amplitud

if __name__ == "__main__":
    print("Módulo de procesamiento de datos y FFT para Osciladores PASCO listo.")
