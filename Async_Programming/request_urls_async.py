import aiohttp
import asyncio
import time

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json() # Aguarda a execução da função para finalizar, mas enquanto isso não ocorre, passa o controle para a próxima função

async def main():
    urls = [
        "https://viacep.com.br/ws/01001000/json/",
        "https://viacep.com.br/ws/57304400/json/",
        "https://viacep.com.br/ws/57304200/json/"
    ]
    results = await asyncio.gather(*(fetch(url) for url in urls))
    for result in results:
        print(result)

inicio = time.perf_counter()
asyncio.run(main())
total = time.perf_counter() - inicio
print(f"{total:0.2f} segundos")