import random
contador = 1

while True:

    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    multiplicador = random.randint(1, 9)
    num2Div = random.randint(1, 9)
    num1Div = num2Div * multiplicador

    operador_aleatorio = random.choice(["+", "-", "*", "/"])

    if operador_aleatorio == "+":
        resposta_certa = num1 + num2
    elif operador_aleatorio == "-":
        resposta_certa = num1 - num2
    elif operador_aleatorio == "*":
        resposta_certa = num1 * num2
    else: 
        resposta_certa = (num1Div / num2Div)

    
    if operador_aleatorio != "/":
        pergunta = print(f"{num1} {operador_aleatorio} {num2}")
    else:
        pergunta = print(f"{num1Div} {operador_aleatorio} {num2Div}")
    resposta_usuario = int(input("qual a resposta certa?"))
    

    if resposta_usuario == resposta_certa:
        print("voce acertou!")
    elif resposta_usuario != resposta_certa:
        print("errou, resposta certa é {} ".format(resposta_certa))

    if resposta_usuario == 999:
        break

    





    