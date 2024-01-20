import pygame
from random import randint
from time import sleep
five = 0
golA = 0
golV = 0
# Inicia a bliblioteca pygame e mostra o cabeçalho do jogo
pygame.init()
print('\33[92;1mFootRamdom\33[93m by \33[91;1mTtgames')

# Pede para que o jogador insira os nomes dos times
nome_Do_Time_Azul = str(input('\33[93;1mQual o nome do time da casa?')).capitalize()
nome_Do_Time_Vermelho = str(input('Qual o nome do time visitante?')).capitalize()

# Pede para que o jogador insira a chance de cada time fazer um gol
print('\33[92mDica: As chances devem estar entre 0 e 100, o recomendado é 30/100')
chance_Time_Azul = int(input(f'\33[93;1mQual a chance do time {nome_Do_Time_Azul} fazer um gol?'))
chance_Time_Vermelho = int(input(f'Qual a chance do time {nome_Do_Time_Vermelho} fazer um gol?'))
print(f'\33[97;1mEntão a chance do time {nome_Do_Time_Azul} fazer um gol é de {chance_Time_Azul}/100', end=' ')
print(f'E a chance do time {nome_Do_Time_Vermelho} de fazer um gol é de {chance_Time_Vermelho}/100')

# Guarda as chances dos times fazerem gol na variável randintRed e randintBlue e inicia o loop principal
for time in range(0, 9):
    randintBlue = randint(0, 100)
    randintRed = randint(0, 100)
    tentarA = randint(1, 3)
    tentarV = randint(1, 3)
    five += 5
    sleep(2)
    print(f'\33[97;1m{five} minutos do primeiro tempo')
    sleep(5)
    if tentarA == 2:
        print(f'\33[96mO time {nome_Do_Time_Azul} vai tentar o gol')
        if randintBlue <= chance_Time_Azul:
            sleep(5)
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Azul}')
            golA += 1
            print(f'O placar está \33[96m{golA} - \33[91m{golV}')
        else:
            sleep(5)
            print('\33[91mErraram o gol')
    if tentarV == 2:
        print(f'\33[91mO time {nome_Do_Time_Vermelho} vai tentar o gol')
        if randintRed < chance_Time_Vermelho:
            sleep(5)
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Vermelho}')
            golV += 1
            print(f'O placar está \33[96m{golA} - \33[91m{golV}')
        else:
            sleep(5)
            print('\33[91mErraram feio o gol')
            print(f'\33[97mO placar continua \33[96m{golA} - \33[91m{golV}')
