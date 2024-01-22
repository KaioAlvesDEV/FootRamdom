import pygame
from random import randint
from time import sleep
five = 0
golA = 0
golV = 0
penalA = 0
penalV = 0
acrescimos = randint(0, 8)
# Inicia a bliblioteca pygame e mostra o cabeçalho do jogo
pygame.init()
print('\33[92;1mFootRamdom\33[93m by \33[91;1mTtgames')

# Pede para que o jogador insira os nomes dos times
nome_Do_Time_Azul = str(input('\33[93;1mQual o nome do time da casa?')).capitalize()
nome_Do_Time_Vermelho = str(input('Qual o nome do time visitante?')).capitalize()

# Pede para que o jogador insira a chance de cada time fazer um gol
print('\33[92mDica: As chances devem estar entre 0 e 100, o recomendado é 30/100')
chance_Time_Azul = float(input(f'\33[93;1mQual a chance do time {nome_Do_Time_Azul} fazer um gol?'))
chance_Time_Vermelho = float(input(f'Qual a chance do time {nome_Do_Time_Vermelho} fazer um gol?'))
print(f'\33[97;1mEntão a chance do time {nome_Do_Time_Azul} fazer um gol é de {chance_Time_Azul}/100', end=' ')
print(f'E a chance do time {nome_Do_Time_Vermelho} de fazer um gol é de {chance_Time_Vermelho}/100')
tempo = float(input('Insira o tempo por minuto da simulação, o recomendado é de 5s'))
# Guarda as chances dos times fazerem gol na variável randintRed e randintBlue e inicia o loop principal
for time in range(0, 90 + acrescimos):
    randintBlue = randint(0, 100)
    randintRed = randint(0, 100)
    tentarA = randint(1, 14)
    tentarV = randint(1, 15)
    lesaoA = randint(1, 120)
    lesaoV = randint(1, 110)
    # desgaste dos jogadores
    chance_Time_Azul -= 0.05
    chance_Time_Vermelho -= 0.075
    five += 1
    sleep(tempo)
    print(f'\33[97;1m{five} minutos de jogo')
    if lesaoA == 1:
        pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
        pygame.mixer.music.play()
        sleep(17)
        pygame.mixer.music.stop()
        print(f'\33[93mInfelizmente um jogador do time {nome_Do_Time_Azul} foi lesionado, isso diminui em 5 a chance do time fazer gol')
        sleep(4)
        chance_Time_Azul = max(0, chance_Time_Azul - 5)
    if lesaoV == 1:
        pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
        pygame.mixer.music.play()
        sleep(17)
        pygame.mixer.music.stop()
        print(f'\33[93mInfelizmente um jogador do time {nome_Do_Time_Vermelho} foi lesionado, isso diminui em 5 a chance do time fazer gol')
        sleep(4)
        chance_Time_Vermelho = max(0, chance_Time_Vermelho - 5)
    if tentarA == 2:
        chance_Time_Azul -= 1
        print(f'\33[96mO time {nome_Do_Time_Azul} vai tentar o gol')
        if randintBlue <= chance_Time_Azul:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Azul}')
            golA += 1
            print(f'O placar está \33[96m{golA} - \33[91m{golV}')
        else:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print('\33[91mErraram o gol')
            sleep(1)
    if tentarV == 2:
        chance_Time_Vermelho -= 1.25
        print(f'\33[91mO time {nome_Do_Time_Vermelho} vai tentar o gol')
        if randintRed < chance_Time_Vermelho:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Vermelho}')
            golV += 1
            print(f'O placar está \33[96m{golA} - \33[91m{golV}')
        else:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print('\33[91mErraram feio o gol')
            print(f'\33[97mO placar continua \33[96m{golA} - \33[91m{golV}')
    if five == 45:
        chance_Time_Azul += 5
        chance_Time_Vermelho += 4
        sleep(2)
        print('\33[93mFIM DO PRIMEIRO TEMPO')
        print(f'{golA} - {golV}')
        sleep(4)
        print('INTERVALO COMERCIAL...')
        pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
        pygame.mixer.music.play()
        sleep(271)
        pygame.mixer.music.stop()
        print('\33[93mInicia o segundo tempo')
if golA == golV:
    print('EMPATE, É HORA DA PRORROGAÇÃO, DEBUFF DE DESGASTE PARA O TIME FORA DA CASA E BUFF DE TENTATIVAS DE GOL PARA O TIME DE CASA')
    sleep(4)
    for time in range(0, 15 + acrescimos):
        randintBlue = randint(0, 100)
        randintRed = randint(0, 100)
        tentarA = randint(1, 12)
        tentarV = randint(1, 16)
        lesaoA = randint(1, 120)
        lesaoV = randint(1, 110)
        # desgaste dos jogadores
        chance_Time_Azul -= 0.05
        chance_Time_Vermelho -= 0.25
        five += 1
        sleep(tempo)
        print(f'\33[97;1m{five} minutos de jogo')
        if lesaoA == 1:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(
                f'\33[93mInfelizmente um jogador do time {nome_Do_Time_Azul} foi lesionado, isso diminui em 5 a chance do time fazer gol')
            sleep(4)
            chance_Time_Azul = max(0, chance_Time_Azul - 5)
        if lesaoV == 1:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(
                f'\33[93mInfelizmente um jogador do time {nome_Do_Time_Vermelho} foi lesionado, isso diminui em 5 a chance do time fazer gol')
            sleep(4)
            chance_Time_Vermelho = max(0, chance_Time_Vermelho - 5)
        if tentarA == 2:
            chance_Time_Azul -= 1
            print(f'\33[96mO time {nome_Do_Time_Azul} vai tentar o gol')
            if randintBlue <= chance_Time_Azul:
                pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
                pygame.mixer.music.play()
                sleep(17)
                pygame.mixer.music.stop()
                print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Azul}')
                golA += 1
                print(f'O placar está \33[96m{golA} - \33[91m{golV}')
            else:
                pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
                pygame.mixer.music.play()
                sleep(17)
                pygame.mixer.music.stop()
                print('\33[91mErraram o gol')
                sleep(1)
        if tentarV == 2:
            chance_Time_Vermelho -= 1.25
            print(f'\33[91mO time {nome_Do_Time_Vermelho} vai tentar o gol')
            if randintRed < chance_Time_Vermelho:
                pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
                pygame.mixer.music.play()
                sleep(17)
                pygame.mixer.music.stop()
                print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Vermelho}')
                golV += 1
                print(f'O placar está \33[96m{golA} - \33[91m{golV}')
            else:
                pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
                pygame.mixer.music.play()
                sleep(17)
                pygame.mixer.music.stop()
                print('\33[91mErraram feio o gol')
                print(f'\33[97mO placar continua \33[96m{golA} - \33[91m{golV}')
if golA == golV:
    chance_Time_Azul += 8
    chance_Time_Vermelho += 7
    sleep(2)
    print('\33[93mAGUARDE OS PENALTIS')
    print(f'{golA} - {golV}')
    sleep(4)
    print('INTERVALO COMERCIAL...')
    pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
    pygame.mixer.music.play()
    sleep(271)
    pygame.mixer.music.stop()
    print('\33[93mHora dos penaltis')
    print('Quem fizer o máximo de gols em 5 chutes ganha, com o modificador em que a cada chute a chance de fazer gols aumenta em 4')
    for penaltis in range(1, 5):
        randintBlue = randint(0, 100)
        randintRed = randint(0, 100)
        chance_Time_Azul += 4
        chance_Time_Vermelho += 4
        print(f'\33[96mO time {nome_Do_Time_Azul} vai cobrar o penalti')
        if randintBlue <= chance_Time_Azul:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Azul}')
            penalA += 1
            print(f'O placar está \33[96m{penalA} - \33[91m{penalV}')
        else:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print('\33[91mErraram o gol')
            sleep(1)
        print(f'\33[91mO time {nome_Do_Time_Vermelho} vai tentar o penalti')
        if randintRed < chance_Time_Vermelho:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print(f'\33[92mGOOOOOOOOOOOOL! Gol do time {nome_Do_Time_Vermelho}')
            penalV += 1
            print(f'O placar está \33[96m{penalA} - \33[91m{penalV}')
        else:
            pygame.mixer.music.load('liveandlearnsonicadventure2.mp3')
            pygame.mixer.music.play()
            sleep(17)
            pygame.mixer.music.stop()
            print('\33[91mErraram feio o gol')
            print(f'\33[97mO placar continua \33[96m{penalA} - \33[91m{penalV}')
if golA > golV:
    print(f'\33[96mO jogo acabou em {golA} - {golV}, o time ganhador foi o {nome_Do_Time_Azul}')
if golV > golA:
    print(f'\33[91mO jogo acabou em {golA} - {golV}, o time ganhador foi o {nome_Do_Time_Vermelho}')
if golA == golV:
    print(f'\33[93mO jogo acabou nos penaltis em {penalA} - {penalV}')
