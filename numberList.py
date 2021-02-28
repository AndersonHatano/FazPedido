extensive_number = ["zero ", "um ", "dois ", "tres ","quatro ", "cinco ", "seis ", "sete ", "nove ", "dez ",
"onze ", "doze ", "treze ", "quatorze ", "quinze ", "dezesseis ", "dezessete ", "dezoito ", "dezenove ", "vinte ",
"trinta ", "quarenta ", "cinquenta ", "sessenta ", "setenta ", "oitenta ", "noventa ", "cem ", "cento ",
"duzentos ", "trezentos ", "quatrocentos ", "quinhentos ", "seiscentos ", "setecentos ", "oitocentos ", "novecentos ","mil "]

interger_number = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100,
200, 300, 400, 500, 600, 700, 800, 900, 1000]

def processar_numero(quantidade):
    for cont in range (len(extensive_number)):

        if(extensive_number[cont] == quantidade):
            quantidade_numero = interger_number[cont]
            return quantidade_numero

        elif(cont == (len(extensive_number)-1)):
            quantidade_numero = 0
            return quantidade_numero 


def comparar_numero(teste0):

    for cont in range(len(extensive_number)):
        if(extensive_number[cont] == teste0):
            return "true"