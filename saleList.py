sale = ["temaki de salmão ", "sashimi de atum ", "yakisoba de frango "]

price = [15.90, 22.80, 19.99]

def processar_pedido(validate_sales):
    for cont in range (len(sale)):
        if(validate_sales == sale[cont]):
            return "true"


teste = ["yakisoba de frango ", "temaki de salmão ", "sashimi de atum "]

for cont in range (len(teste)):
    for cont2 in range (len(sale)):
        if(teste[cont] == sale[cont2]):
            print(str(sale[cont2]) + " - R$ " + str(price[cont2]))


def processar_valor(prato):
    for cont in range(len(sale)):
        if(prato == sale[cont]):
            preco = price[cont]
            return preco