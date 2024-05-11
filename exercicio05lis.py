"""
Faça um programa que percorra duas listas e gere uma terceira com
elementos das duas primeiras.

"""

# Definindo duas listas iniciais
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

# Inicializando a terceira lista vazia
lista3 = []

# Percorrendo as duas listas e adicionando os elementos à terceira lista
for elemento in lista1:
    lista3.append(elemento)

for elemento in lista2:
    lista3.append(elemento)

# Exibindo a terceira lista resultante
print("A terceira lista combinada é:", lista3)
