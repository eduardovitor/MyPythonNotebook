
# O operador de atribuição passa a referência de lista para outra (uma modificação em uma afeta a outra)
lista = [1,2,3,4,5]
mesma_lista = lista
mesma_lista.append(19)
mesma_lista.append(20)
print(lista)
print("*"*20)

# O operador de atribuição não passa referência de tipos simples como o int
numero = 2
numero_espelho = numero
numero_espelho = 5
print(numero)
print("*"*20)

# Caso seja necessário apenas obter uma cópia da lista para modificação sem alterar a lista original

lista_shallow = [4,9,10,22,27,29]
shallow_copy = lista_shallow.copy()
shallow_copy.append(18)
shallow_copy.append(15)
print(lista_shallow)
print(shallow_copy)


