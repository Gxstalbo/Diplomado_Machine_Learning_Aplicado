import pandas as pd
import os

os.chdir(r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1.2")

# Lee toda la carpeta
list_fifa=[]
with os.scandir(r'datasets\files\input') as ficheros:
    for fichero in ficheros:
        df_sentences= pd.read_csv('datasets/files/input/'+fichero.name, sep=",", encoding='utf8')
        df_sentences['FIFA_YEAR']= "20"+fichero.name[-6:-4]
        list_fifa.append(df_sentences)

df_total_fifa= pd.concat(list_fifa)

df_total_fifa.to_csv(r"datasets\files\intermedia\fifa_dataset.csv", index=False, sep=",")
