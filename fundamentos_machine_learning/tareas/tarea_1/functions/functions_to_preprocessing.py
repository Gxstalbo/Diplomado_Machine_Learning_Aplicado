import numpy as np
import string

def vectorizar_palabra(strng, alphabet=string.ascii_lowercase):
  vector = np.zeros(len(alphabet))
  for letter in strng:
    vector += np.array([0 if char != letter else 1 for char in alphabet])
  return vector

def normalizar_vector(vector):
  list_v=[]
  for vect in vector:
    for vect2 in vect:
      v = vect2 / np.sum(vect2)
      list_v.append(v)
  return list_v

def lista_a_matriz(lista, vert = True):
  if vert:
    return np.vstack(lista)
  else:
    return np.hstack(lista)

def vectorizar_frase(string):
  sentence= string.split()
  list_palabra=[]
  for palabra in sentence:
    list_palabra.append(vectorizar_palabra(palabra.lower()))
  return list_palabra