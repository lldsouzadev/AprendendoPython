def calcula_preco(preco_normal, forma_pagamento):
    if forma_pagamento == "dinheiro":
        return preco_normal * 0.9
    elif forma_pagamento == "debito":
        return preco_normal * 0.95
    elif forma_pagamento == "credito":
        return preco_normal
    elif forma_pagamento in "credito3x credito4x credito5x credito6x credito7x credito8x credito9x credito10x":
        return preco_normal * 1.2
    else:
        return "Forma de Pagamento Inválida"

preco = calcula_preco(100, "dinheiro")
print("Preço a ser pago: ", preco)
