from collections import defaultdict

frase = "Minha faculdade é incrível"

dict_contador = defaultdict(int)

for letra in frase:
    dict_contador[letra] +=1

print(sorted(dict_contador.items()))