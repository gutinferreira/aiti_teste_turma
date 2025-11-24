def calcula_total(preco,perc_desconto,perc_imposto):
    desconto = preco * perc_desconto
    imposto = (preco - desconto) * perc_imposto
    total = preco - desconto + imposto
    return round (total,2)
