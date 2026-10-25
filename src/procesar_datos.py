import pandas as pd
import matplotlib.pyplot as plt
def cargardatos(filepath):
    #CARGA UN ARCHIVO EXPORTADO DE PASCO CAPSTONE (CSV O TXTdelimitado por comas/tabulaciones).
    df=pd.read_csv(filepath, delimiter=None, engine='python')
    df.colums= df.columns.str.strip() #Elimina espacios en blanco de los nombres de las columnas
    return df
if __name__ == "__main__":
    print("Modulo de procesamiento de datos cargado correctamente.")