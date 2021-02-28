import numberList
import saleList

txt = "vinte e um temaki de salmão dois sashimi de atum sete yakisoba"

pedido = ""
cont2 = 0
cont_quantidade_pedido = 0
cont_pratos = 0
sprpedido = [] 
quantidade = []
pratos = []
quantidade = 0
quantidade_pedido = []
trava = 0

#Separa os Strings em um array
for cont in range (len(txt)):
    pedido += txt[cont]

    if(txt[cont] == " " or cont ==(len(txt)-1)):

        sprpedido.append(pedido)
        cont2 += 1 
        pedido = ""

pratos = sprpedido

#Separa a quantidade dos nomes dos pedidos
for cont3 in range (len(sprpedido)):

    quantidade = sprpedido[cont3]
    quantidade_numero = numberList.processar_numero(quantidade)

    if(quantidade_numero != 0):
        if(len(quantidade_pedido) != 0):
            quantidade_pedido[cont_quantidade_pedido] += quantidade_numero
            trava = 0
        if(len(quantidade_pedido) == 0):
            quantidade_pedido.append(quantidade_numero)
            trava = 0
        if(quantidade_numero == 1000):
            quantidade_pedido[cont_quantidade_pedido] = quantidade_numero[cont_quantidade_pedido] * quantidade_numero
            trava = 0

    if(sprpedido[cont3] == "e "):
        quantidade_numero = 0

    elif(quantidade_numero == 0 and trava == 0):
        cont_quantidade_pedido = cont_quantidade_pedido + 1
        trava = 1
        quantidade_numero = 0
        quantidade_pedido.append(0)

#Separa os nomes do pratos
for cont4 in range (len(sprpedido)):
    
    validate_number = sprpedido[cont4]

    if(validate_number != "e "):

        if(numberList.comparar_numero(validate_number) != "true"):
        
            if(sprpedido[cont_pratos] != sprpedido[cont4]):    
                pratos[cont_pratos] = pratos[cont_pratos] + sprpedido[cont4]

            validate_sales = pratos[cont_pratos]
            
            if(saleList.processar_pedido(validate_sales) == "true"):
                cont_pratos = cont_pratos + 1
                pratos[cont_pratos] = ""

        else:
            pratos[cont_pratos] = ""

#Calcular valor pedido
for 

#Apresentar em tela quantidade de pratos
for cont in range (cont_quantidade_pedido):
    print(str(quantidade_pedido[cont]) + " - " + pratos[cont])
