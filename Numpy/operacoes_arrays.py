import numpy as np

a = np.sin(np.pi / 2)
print(a)  # operação com seno e pi
print(type(np.pi))  # pi em float
print(type(np.nan))  # similar a none
a_1 = np.array([[1, 2, 3]])
a_2 = np.array([4, 5, 6])
print(a_1 - 5)  # operação matematica
print(a_1 * a_2)  # multiplicação de arrays
print(a_1.dot(a_2))  # multiplicação matricial
