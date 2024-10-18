import asyncio

# Dorme todas as tarefas pelo tempo de atraso e depois executa uma por uma
async def tarefa(nome, atraso):
    await asyncio.sleep(atraso)
    print(f"Tarefa {nome} concluída após {atraso} segundos")

async def main():
    await asyncio.gather(
        tarefa("A", 1),
        tarefa("B", 2),
        tarefa("C", 3)
    )

asyncio.run(main())