from collections import defaultdict

times = ["Botafogo", "Botafogo", "Fluminense", 
         "Palmeiras", "Corinthians", "Palmeiras",
         "Flamengo", "Vasco", "Cuiabá", "Internacional",
         "Cruzeiro", "Juventude"]

dict_valores_unicos = defaultdict(set)

for time in times:
    dict_valores_unicos[len(time)].add(time)

print(dict_valores_unicos)
