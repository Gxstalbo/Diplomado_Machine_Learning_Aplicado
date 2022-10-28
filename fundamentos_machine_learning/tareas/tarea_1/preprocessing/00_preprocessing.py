import pandas as pd
from functions.functions_to_preprocessing import *
import os

file=r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1\datasets\files"
os.chdir(file)

#Carga datasets
df_sentences= pd.read_csv(r"output\total_sentences.csv", sep=",")

#