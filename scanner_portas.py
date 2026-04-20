import socket

ip_alvo = input('Qual IP deseja verificar? ')
porta = int(input('Qual porta deseja verificar? '))

print(f'\nCOMEÇANDO O SCANNER DA PORTA SOLICITADA....\n')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(0.5)

resultado = cliente.connect_ex((ip_alvo, porta))

if resultado == 0:
    print(f'A porta {porta} está ABERTA!')
else:
    print(f'A porta {porta} está fechada ou filtrada.')

cliente.close()