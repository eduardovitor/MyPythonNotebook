from collections import deque

pessoas = ["João", "Fernando", "Maria Júlia", "Camila", "Millene", "Paulo"]
fila_pessoas = deque(pessoas)

# Atendendo pessoas da fila
fila_pessoas.popleft()
fila_pessoas.popleft()
# Novas pessoas chegaram
fila_pessoas.append("Caio")
fila_pessoas.append("Isabela")
# Atendendo mais pessoas da fila
fila_pessoas.popleft()
fila_pessoas.popleft()
fila_pessoas.popleft()
# Ver fila resultante
print(fila_pessoas)