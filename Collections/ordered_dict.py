from collections import OrderedDict

# Funções importantes: popitem() e move_to_end()

ord_dict = OrderedDict()

ord_dict["bairro"] = "Gusmão"
ord_dict["número"] = 7878
ord_dict["rua"] = "São Japão"

for elemento in reversed(ord_dict):
    print(elemento)