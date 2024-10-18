import requests
import time

urls = [
        "https://viacep.com.br/ws/01001000/json/",
        "https://viacep.com.br/ws/57304400/json/",
        "https://viacep.com.br/ws/57304200/json/"
    ]

inicio = time.perf_counter()

for url in urls:
    resp =  requests.get(url).json()
    print(resp)

total = time.perf_counter() - inicio
print(f"{total:0.2f} segundos")