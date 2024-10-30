from collections import namedtuple

Produto = namedtuple("Produto", ["nome", "preco", "quantidade"])

produto1 = Produto(nome="Brinquedo Hello Kitty", preco=12.90, quantidade=4)
produto2 = Produto(nome="Camisa Social", preco=100, quantidade=2)
produto3 = Produto(nome="Tênis Adidas", preco=400, quantidade=1)

produtos = list()
produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

valor_produtos_estoque = 0
for p in produtos:
    valor_produto_unit = p.preco * p.quantidade
    valor_produtos_estoque += valor_produto_unit

print("A soma total dos valores de produtos no estoque é: {}".format(valor_produtos_estoque))
