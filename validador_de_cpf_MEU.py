while True:
    cpf = input("digite seu cpf sem pontuacao: ")
    
    if cpf.isdigit() == False or not len(cpf) == 11  :
        print('digite um valor válido')
        break 
    
    sequencia = cpf[0] * len(cpf)
    
    if sequencia == cpf:
        print('digite um valor válido')
        break
    
    contador = 10
    soma1 = []

    for v1 in cpf:
        v1 = int(v1)
        soma1.append(v1 * contador)
    
        contador -= 1
    

        if contador <= 1:
            contador = 0
        

    digito1 = 11 - (sum(soma1) % 11)

    if digito1 > 9:
        digito1 = 0

    contador = 11
    soma2 = []

    for v2 in cpf:
        v2 = int(v2)
        soma2.append(v2 * contador)

        contador -= 1
    
        if contador <= 1:
            contador = 0            
    
    digito2 = 11 - (sum(soma2) % 11)

    digito1 = str(digito1)
    digito2 = str(digito2)

    if digito1 == cpf[-2] and digito2 == cpf[-1]:
        print("seu cpf é válido")
    else:
        print("seu cpf é inválido")

