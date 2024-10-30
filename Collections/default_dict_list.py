from collections import defaultdict

palavras = ['gato','carro','bicicleta','casa']

dict_agrupador = defaultdict(list)

for palavra in palavras:
    dict_agrupador[len(palavra)].append(palavra)

print(dict_agrupador) 