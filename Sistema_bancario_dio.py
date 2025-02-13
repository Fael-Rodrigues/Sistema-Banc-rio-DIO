# Sistema bancario

print('=-'*20)
print('Banco do Fael')
print('=-'*20)
conta = 0
controle = 1
contador = 0
saques = []

while True: # Loop infinito para o menu
    print('''Operações: 
    [1] Deposito: 
    [2] Saque: 
    [3] Extrato: ''')

    op = int(input('Escolha uma operação: '))# escolha da opção
 
    if op == 1:# opcao deposito
        print('Voce escolheu a opção de deposito:')
        while controle == 1:
            v = int(input('informe o valor que deseja depositar: '))# inserindo o valor do deposito
            conta = conta + v # somando o valor ao saldo
            print('Deposito realizado!')
            controle = int(input('Deseja fazer outro deposito? [1 = Sim] / [0 = Não]: ')) # deseja fazer outro deposito
    elif op == 2:# opcao saque
        print('Voce escolheu a opção de saque:')
        while controle == 1 and contador <= 3:
            v = int(input('Quantos voce quer sacar? saque maximo R$500: '))
            if conta > 0 and v <= conta:
                conta = conta - v
                contador = contador + 1
                print('Saque ralizado!')
                t = f'saque {contador} realizado no valor de {v}'
                saques.append(t)
            else:
                print('Saldo insuficiente')
            controle = int(input('Deseja fazer outro saque? [1 = Sim] / [0 = Não]: '))
    r = str(input('Deseja fazer outra operacao? [s/n]: '))
    if r == 'n':
        break




print(f'O saldo da sua conta é de R${conta}')