
# Formando um dicionário com a função zip

campos = ["nome", "cpf", "idade", "matricula"]
valores = ["Fernando", 1111, 25, "a-7777"]
zip_dados = zip(campos,valores)
dict_dados = dict(zip_dados)
print(dict_dados)

# Atualizando o valor de um dicionário
campo = ["idade"]
valor = [29]
dict_dados.update(zip(campo,valor))
print(f"Dicionário atualizado: {dict_dados}")

# Percorrendo listas em paralelo

nomes = ["Joana", "Michelle", "Rafael"]
numeros = [70,14,89]

for nome,numero in zip(nomes,numeros):
    print(nome)
    print(numero)

# Percorrendo dicionários em paralelo
dict_one = {"name": "John", "last_name": "Doe", "job": "Python Consultant"}
dict_two = {"name": "Jane", "last_name": "Doe", "job": "Community Manager"}
for (k1,v1), (k2,v2) in zip(dict_one.items(),dict_two.items()):
    print(f"{k1}->{v1}")
    print(f"{k2}->{v2}")

# Deszipando elementos
pairs = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
numbers, letters = zip(*pairs) # gera duas tuplas
print(numbers)
print(letters)