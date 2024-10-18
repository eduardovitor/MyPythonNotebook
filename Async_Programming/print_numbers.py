import asyncio
import time

# Imprime números com intervalo de 1 segundo
async def imprimir_numeros():
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(i)

s = time.perf_counter()
asyncio.run(imprimir_numeros())
elapsed = time.perf_counter() - s
print(f"Tempo decorrido foi de {elapsed:0.2f}")
# sleep(1), 1, sleep(1), 2, 