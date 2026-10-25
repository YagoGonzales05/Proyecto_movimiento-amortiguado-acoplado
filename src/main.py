import numpy as np
import matplotlib.pyplot as plt

# Importamos nuestros módulos
from modelo_teorico import simular_teoria
from procesar_datos import calcular_fft

if __name__ == "__main__":
    print("Ejecutando comparación directa: Teoría (SciPy) vs Experimento (PASCO)...")
    
    # 1. Definir parámetros físicos teóricos
    m1, m2 = 0.5, 0.5
    k1, k2, k3 = 10.0, 15.0, 10.0
    c1, c2 = 0.05, 0.05
    params = (m1, m2, k1, k2, k3, c1, c2)
    
    # 2. Simular la teoría
    fs = 50.0
    t_eval = np.linspace(0, 10, int(10 * fs))
    condiciones_iniciales = [0.05, 0.0, -0.02, 0.0]
    t_sim, y_sim = simular_teoria(t_eval, condiciones_iniciales, params)
    x_teorico = y_sim[0]  # Posición teórica masa 1
    
    # 3. Simular una señal experimental (o la que vendrá de tu archivo CSV de PASCO)
    # Aquí puedes reemplazar 'x_experimental' por la lectura real de tu DataFrame de Pandas cuando tengas el CSV
    x_experimental = x_teorico + 0.005 * np.sin(2 * np.pi * 5 * t_sim) # Añadiendo un poquito de ruido realista
    
    # 4. Crear la figura comparativa de alta calidad
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico superior: Superposición Teoría vs Experimento
    ax1.plot(t_sim, x_experimental, label="Experimental (Sensor PASCO)", color='tab:blue', alpha=0.7, linewidth=1.5)
    ax1.plot(t_sim, x_teorico, label="Modelo Teórico (SciPy EDOs)", color='tab:red', linestyle='--', linewidth=2)
    ax1.set_title("Comparación: Modelo Teórico vs Datos Experimentales", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_ylabel("Posición (m)")
    ax1.legend(loc="upper right")
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Gráfico inferior: FFT de los datos experimentales
    xf, amplitud = calcular_fft(t_sim, x_experimental, fs)
    ax2.plot(xf, amplitud, color='tab:orange', linewidth=1.5)
    ax2.set_title("Espectro de Frecuencias (FFT) - Modos Normales Experimentales", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Frecuencia (Hz)")
    ax2.set_ylabel("Amplitud Normalizada")
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.set_xlim(0, 10)

    plt.tight_layout()
    
    # Guardar figura para el informe
    ruta_figura = "figures/comparacion_final.png"
    plt.savefig(ruta_figura, dpi=300)
    print(f"Gráfico de comparación guardado exitosamente en: {ruta_figura}")
    plt.show()