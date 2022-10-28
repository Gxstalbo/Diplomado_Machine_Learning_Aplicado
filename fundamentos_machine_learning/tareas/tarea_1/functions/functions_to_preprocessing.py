import numpy as np
import string

def vectorizar_palabra(strng, alphabet=string.ascii_lowercase):
  vector = np.zeros(len(alphabet))
  for letter in strng:
    vector += np.array([0 if char != letter else 1 for char in alphabet])
  return vector

def normalizar_vector(vector):
  v = vector / np.sum(vector)
  return v

def lista_a_matriz(lista, vert = True):
  if vert:
    return np.vstack(lista)
  else:
    return np.hstack(lista)