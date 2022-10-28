import pandas as pd
from functions.functions_to_preprocessing import *
import os

file=r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1\datasets\files"
os.chdir(file)

#Carga datasets
df_sentences= pd.read_csv(r"output\total_sentences.csv", sep=",")

df_positive = df_sentences.query("CLASS==1")
del(df_positive['CLASS'])

df_negative= df_sentences.query("CLASS==0")
del(df_negative['CLASS'])

#vectores_positive= lista_a_matriz([normalizar_vector((vectorizar_frase(frase))) for frase in df_positive['SENTENCE'].tolist()])
to_large=[(vectorizar_frase(frase)) for frase in df_positive['SENTENCE'].tolist()]
#Sentencia completa
largo_maximo= largo_maximo_array(to_large)

positive_list=[estandarizar_largo(normalizar_vector((vectorizar_frase(frase))),largo_maximo) for frase in df_positive['SENTENCE'].tolist()]

for i in range(len(positive_list)):
    try:
        var=len(positive_list[i])
    except:
        del(positive_list[i])

np_positive= lista_a_matriz(positive_list)
np_positive[-1]

    
