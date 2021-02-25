import numberList

txt = "um temaki de salmão e dois sashimi de atum"

pedido = ""
cont2 = 0
cont_quantidade_pedido = 0
sprpedido = [] 
quantidade = []
pratos = []
quantidade = 0
quantidade_pedido = []

#Separa os Strings em um array
for cont in range (len(txt)):
    pedido += txt[cont]

    if(txt[cont] == " " or cont ==(len(txt)-1)):

        sprpedido.append(pedido)
        cont2 += 1 
        pedido = ""

#Separa a quantidade
for cont3 in range (len(sprpedido)):

    quantidade = sprpedido[cont3]
    quantidade_numero = numberList.processar_numero(quantidade)

    if(quantidade_numero != 0):
        if(len(quantidade_pedido) == 0):
            quantidade_pedido[cont_quantidade_pedido] = 1
        if(quantidade_numero == 1000):
            quantidade_pedido[cont_quantidade_pedido] = quantidade_numero[cont_quantidade_pedido] * quantidade_numero
        else:
            quantidade_pedido[cont_quantidade_pedido] += quantidade_numero

    if(sprpedido[cont3] == "e "):
        quantidade_numero = 0

    if(quantidade_numero == 0):
        ++cont_quantidade_pedido
        quantidade_numero = 0

    print(quantidade_pedido[cont_quantidade_pedido])

#Separa os nomes do pratos
for cont4 in range (len(sprpedido)):

    if(sprpedido[cont4] == "temaki "):
        pratos.append(sprpedido[cont4])
        print(pratos)
    
