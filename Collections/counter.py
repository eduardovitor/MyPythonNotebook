import requests
from collections import Counter

conteudo = requests.get("https://www.gutenberg.org/cache/epub/11/pg11.txt") # Book - Alice’s Adventures in Wonderland
conteudo = conteudo.text
conteudo_split = conteudo.split(" ")

for i in range(len(conteudo_split)):
    if conteudo_split[i].find("\r"):
        conteudo_split[i] = conteudo_split[i].replace("\r","")
    if conteudo_split[i].find("\n"):
        conteudo_split[i] = conteudo_split[i].replace("\n","")
    if conteudo_split[i].find("\\"):
        conteudo_split[i] = conteudo_split[i].replace("\\","")

contador = Counter(conteudo_split)
print("Frequência das 50 palavras mais comuns no livro Alice’s Adventures in Wonderland")
for (chave,valor) in contador.most_common(50):
    print(f"{chave}: {valor}")

