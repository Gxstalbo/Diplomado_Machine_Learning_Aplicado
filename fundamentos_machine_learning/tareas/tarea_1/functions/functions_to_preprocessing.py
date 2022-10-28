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
    v = vect / np.sum(vect)
    list_v.append(v)
  return list_v

def lista_a_matriz(lista, vert = True):
  if vert:
    return np.stack(lista)
  else:
    return np.hstack(lista)

def vectorizar_frase(string):
  sentence= string.split()
  list_palabra=[]
  for palabra in sentence:
    list_palabra.append(vectorizar_palabra(palabra.lower()))
  return list_palabra

def largo_maximo_array(vector):
  list_v=[]
  largo_maximo=0
  for vect in vector:
    largo = len(vect)    
    if largo> largo_maximo:
      largo_maximo=largo
    
  return largo_maximo

def estandarizar_largo(vector, largo_maximo):
  try:
    if len(vector) != 31:
      for i in range(len(vector),31):
        vector.append(np.array([0]*26))
      return vector
  except:
    return
