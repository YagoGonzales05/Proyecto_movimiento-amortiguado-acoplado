import numpy as np
from scipy.integrate import solve_ivp

def sistema_osciladores_acoplados(t, y, m1, m2, k1, k2, k3, c1, c2):
    """
    Define el sistema de EDOs para dos masas acopladas por resortes con amortiguamiento.
    y = [x1, v1, x2, v2]
    """
    x1, v1, x2, v2 = y
    
    # Aceleraciones basadas en la segunda ley de Newton
    dv1_dt = (- (k1 + k2) * x1 + k2 * x2 - c1 * v1) / m1
    dv2_dt = (k2 * x1 - (k2 + k3) * x2 - c2 * v2) / m2
    
    dx1_dt = v1
    dx2_dt = v2
    
    return [dx1_dt, dv1_dt, dx2_dt, dv2_dt]

def simular_teoria(t_eval, condiciones_iniciales, params):
    """
    Resuelve numéricamente el sistema de EDOs usando SciPy (solve_ivp).
    """
    m1, m2, k1, k2, k3, c1, c2 = params
    t_span = (t_eval[0], t_eval[-1])
    
    sol = solve_ivp(
        fun=lambda t, y: sistema_osciladores_acoplados(t, y, m1, m2, k1, k2, k3, c1, c2),
        t_span=t_span,
        y0=condiciones_iniciales,
        t_eval=t_eval
    )
    
    return sol.t, sol.y

if __name__ == "__main__":
    print("Módulo teórico con SciPy listo.")