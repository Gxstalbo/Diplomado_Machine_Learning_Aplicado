import os
import pandas as pd

file=r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1\datasets\files"
os.chdir(file)

# Lee toda la carpeta
list_sentences=[]
with os.scandir('input') as ficheros:
    for fichero in ficheros:
        df_sentences= pd.read_csv('input/'+fichero.name, sep="\t", names=['SENTENCE','CLASS'], encoding='utf8', lineterminator='\n')
        list_sentences.append(df_sentences)

df_total_sentences= pd.concat(list_sentences)

df_total_sentences.to_csv(r"output\total_sentences.csv", index=False)

