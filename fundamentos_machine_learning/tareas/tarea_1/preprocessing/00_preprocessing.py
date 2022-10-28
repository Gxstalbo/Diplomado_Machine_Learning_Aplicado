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
#vectores_positive[-1]
a=[(vectorizar_frase(frase)) for frase in df_positive['SENTENCE'].tolist()]
#Sentencia completa
largo_maximo= largo_maximo_array(a)

len(a[-1])

positive_list=[estandarizar_largo(normalizar_vector((vectorizar_frase(frase))),largo_maximo) for frase in df_positive['SENTENCE'].tolist()]

for i in range(len(positive_list)):
    try:
        var=len(positive_list[i])
    except:
        del(positive_list[i])

np_positive= lista_a_matriz(positive_list)
np_positive[-1]

np_positive

len(np_positive)

#bia=[estandarizar_largo(normalizar_vector((vectorizar_frase(frase))),largo_maximo) for frase in df_positive['SENTENCE'].tolist()]

np_positive= lista_a_matriz(positive_list)
np_positive[-1]


for i in range(len(positive_list)):
    print(i)
    print(len(positive_list[i]))
del(positive_list[948])

#b=[normalizar_vector((vectorizar_frase(frase))) for frase in df_positive['SENTENCE'].tolist()]
b[-1]
#SC
#v = a[-1][-1] / np.sum(a[-1][-1])
max(len(a[-1]))
type(a)
type(vectores_positive)


df_positive['SENTENCE'].tail(1)
#for frase in df_positive['SENTENCE'].tolist():
#    frase.split()
    
