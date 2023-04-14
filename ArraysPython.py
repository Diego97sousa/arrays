#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Criação de arrays
import numpy as np
#O numpy é usado principalmente para trabalahar com arrays multidimenssionais.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#Esse código cria um array Numpy unidimensional com os valores


# In[4]:


#Também podemos criar um array Numpy bidimensional passando uma lista de lista para função array()
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
#Desta forma criamos um array Numpy bidimensional 2x3 com os valores:


# In[7]:


#Também podemos criar um array Numpy bidimensional passando uma lista de lista para função array()
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8 ,9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(arr)
#Desta forma criamos um array Numpy bidimensional 4x5 com os valores:


# In[8]:


#Acessar elementos de um array
#Podemos acessar os elementosde um array Numpy usando seus números de índice, que iniciam em 0:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[3])


# In[11]:


#Também podemos acessar elementos de um array bidimensional usando índices de linha e coluna

import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr[0, 0])
print(arr[0, 2])
print(arr[1, 0])


# In[14]:


#Operações em arrays
#O NumPy permite realizar operações em arrays de forma rápida e eficiente. Por exemplo, podemos adicionar dois arrays NumPy da seguinte maneira:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6,])
arr3 = arr1 + arr2
print(arr3)



# In[15]:


#Funções matemáticas
#O Numpy tanbém oferece muitas funções matemáticas...
import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.sqrt(arr)) #Raiz quadrada
print(np.exp(arr)) #Exponencial
print(np.sin(arr)) #Seno


# In[16]:


#Reshape de arrays
#Podemos alterar a forma de um array usando a função reshape()

import numpy as np
#Array de uma dimensão
arr = np.array ([1, 2, 3, 4, 5, 6])
#Aplicar reshape e riar array bidimensional com os valores:
novo_arr = arr.reshape(2, 3)
#Mostrar o novo array criado
print(novo_arr)
#Esse código irá criar um novo array bidimensional de formato 2x3, a partir de um array unidimensional, com


# In[17]:


#Indexação Booleana 
# Podemos usar indexação booleana para selecionar elementos de um array com base em uma condição:

arr = np.array([1, 2, 3, 4, 5])
bool_arr = arr > 2
print(bool_arr)

novo_arr = arr [bool_arr]
print(novo_arr)


# In[ ]:


#Ordernar uma Array
#O NumPy também oferece funções para ordenação de arrays:

arr = np.array([3, 2, 1, 5, 4])
novo_arr = np.sort(arr)
print(novo_arr)

#Operações de matrizes
#O Numpy é usado para álgebra linear e pode realizar operações de matriz, como multriplicação de matriz e inversão de matriz:

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
novo_arr = np.dot(arr1, arr2)
print(novo_arr)

#Neste exemplo é efetuado a multiplicação de matriz entre arr1 e arr2 e criado um novo array:

