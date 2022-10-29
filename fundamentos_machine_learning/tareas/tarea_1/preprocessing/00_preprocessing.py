import pandas as pd
from functions.functions_to_preprocessing import *
import os
from sklearn.model_selection import train_test_split
from sklearn import metrics, neighbors

file=r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1\datasets\files"
os.chdir(file)

#Carga datasets
df_sentences= pd.read_csv(r"output\total_sentences.csv", sep=",")

df_positive = df_sentences.query("CLASS==1")
del(df_positive['CLASS'])

df_negative= df_sentences.query("CLASS==0")
del(df_negative['CLASS'])

#Preprocess to positive sentences
to_large=[(vectorizar_frase(frase)) for frase in df_positive['SENTENCE'].tolist()]
largo_maximo_pos= largo_maximo_array(to_large)
positive_list=[estandarizar_largo(normalizar_vector((vectorizar_frase(frase))),largo_maximo_pos) for frase in df_positive['SENTENCE'].tolist()]
for i in range(len(positive_list)):
    try:
        if(len(positive_list[i])!=31):
            del(positive_list[i])
    except:
        del(positive_list[i])

np_positive= lista_a_matriz(positive_list)
type(np_positive)

#Preproces to negative sentences
to_large_neg=[(vectorizar_frase(frase_neg)) for frase_neg in df_negative['SENTENCE'].tolist()]
largo_maximo_neg= largo_maximo_array(to_large_neg)
negative_list=[estandarizar_largo(normalizar_vector((vectorizar_frase(frase_neg))),largo_maximo_neg) for frase_neg in df_negative['SENTENCE'].tolist()]
for i in range(len(negative_list)):
    try:
        if(len(negative_list[i])!=31):
            del(negative_list[i])
    except:
        del(negative_list[i])

np_negative= lista_a_matriz(negative_list)

np_positive=np_positive.reshape(len(np_positive),-1)

np_negative=np_negative.reshape(len(np_negative),-1)


###################
X = lista_a_matriz_original([np_positive, np_negative])
X.shape
Y = lista_a_matriz_original([np.ones((len(np_positive))), -np.ones((len(np_negative)))], vert=False)
train_vectors, test_vectors, train_targets, test_targets = train_test_split(X, Y, test_size=0.1, random_state=0)

max_accuracy = 0
best_neighbors = 0
for n_neighbors in range(1,100):
  print(f'Evaluando rendimiento para {n_neighbors} vecinos' )
  classifier = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors).fit(train_vectors, train_targets)
  predicted = classifier.predict(test_vectors)
  accuracy=metrics.balanced_accuracy_score(test_targets, predicted)
  if accuracy > max_accuracy:
    max_accuracy = accuracy
    best_neighbors = n_neighbors
print(f'El mejor rendimiento se alcanza con {best_neighbors} vecinos junto con un accuracy de {max_accuracy}.')



vecinos = neighbors.NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
voc = df_positive.append(df_negative)['SENTENCE'].tolist()
palabras = [0, 220, 300, 995]
for p in palabras:
  distancia, indice = vecinos.kneighbors(X[p].reshape(1,-1))
  print(f'Palabra = {voc[indice[0,0]]},\t Vecino = {voc[indice[0,1]]},\t \
  Sentimiento = {"Positivo" if indice[0,1] < len(df_positive) else "Negativo"},\t Distancia = {distancia[0,1]}')
