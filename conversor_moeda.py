#CONVERSOR DE MOEDAS

saldo_reais = 0
saldo_dolar = 0
saldo_iene = 0

#Função para mostrar saldo após a conversão
def mostrar_moedas(r, d, i):
    print('\n**** CONVERSÕES *****\n')
    print(f'Saldo em Reais: R${r}')
    print(f'Saldo em Dólares: US${d}')
    print(f'Saldo em Ienes: ¥{i}\n')

#Função para fazer a conversão de uma moeda para outra (Real/Dólar/Iene)
def calcular():
    while True:
        #Pedindo para o usuário escolher a moeda que quer fazer a conversão
        moeda = input('Qual moeda? (iene/dolar/real e "sair" para Sair:  ').lower().strip()
        
        if moeda == 'sair':
            print('Encerrando programa...')
            break
        if moeda in ['iene', 'dolar', 'real']:
            try:
                #Conversão origem -> Iene
                if moeda == 'iene':
                    saldo_iene = int(input('Quantos ienes? '))
                    saldo_dolar = int(saldo_iene / 159.74)
                    saldo_reais = int(saldo_iene / 31.08)
                #Conversão origem -> Dólar
                elif moeda == 'dolar':
                    saldo_dolar = int(input('Quantos dolares? '))
                    saldo_reais = int(saldo_dolar * 5.14)
                    saldo_iene = int(saldo_dolar * 159.74)
                #Conversão origem -> Real
                else:
                    saldo_reais = int(input('Quantos reias? '))
                    saldo_dolar = int(saldo_reais / 5.14)
                    saldo_iene = int(saldo_reais * 31.08)

                mostrar_moedas(saldo_reais, saldo_dolar, saldo_iene)

            except ValueError:
                print('Valor inválido. Tente novamente.')
        else:
            print('Moeda inválida. Tente novamente.')

calcular()

#Fazer uma funcão para cada moeda e trocar o IF pelo CASE para o resultado ficar mais específico e melhor