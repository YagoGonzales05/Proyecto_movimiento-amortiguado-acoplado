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

def graficar_resultados(t,x,xf,amplitud,nombre_archivo="osciladores_fft.png"):
    """
    Genera una grafica de dos paneles:
    1. Posicion vs Tiempo (del sensor)
    2. Espectro de frecuencias (FFT)
    """
    fig, (ax1,ax2)=plt.subplots(2,1,figsize=(10,8))
    ax1.plot(t,x,color='tab:blue', linewidth=1.5)
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_ylabel("Posición (m)")
    ax1.set_title("Posición vs Tiempo" "Sensor PASCO")
    ax1.grid(True, linestyle='--',alpha=0.6)
    ax2.plot(xf,amplitud, color='tab:red',linewidth=1.5)
    ax2.set_xlabel("Frecuencia (Hz)")
    ax2.set_ylabel("Amplitud")
    ax2.set_title("Espectro de Frecuencias")
    ax2.grid(True, linestyle='--',alpha=0.6)
    ax2.set_xlim(0,10)
    plt.tight_layout()
    ruta_figura=f"figures/{nombre_archivo}"
    plt.savefig(ruta_figura, dpi=300)
    print(f"Grafica guardada exitosamente en: {nombre_archivo}")
    plt.show()

if __name__ == "__main__":
    print("Ejecutando prueba con datos simulados de osciladores acoplados...")
    
    # 1. Crear un tiempo simulado (ej. 10 segundos a 50 Hz de frecuencia de muestreo)
    fs = 50.0  # Hz
    t = np.linspace(0, 10, int(10 * fs))
    
    # 2. Simular una señal con dos frecuencias características (modo normal 1 y modo normal 2) + amortiguamiento
    f1 = 1.2  # Hz (Modo 1)
    f2 = 3.5  # Hz (Modo 2)
    amortiguamiento = np.exp(-0.1 * t)
    x = amortiguamiento * (np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t))
    
    # 3. Aplicar la FFT
    xf, amplitud = calcular_fft(t, x, fs)
    
    # 4. Generar y mostrar las gráficas
    graficar_resultados(t, x, xf, amplitud, nombre_archivo="prueba_simulacion.png")