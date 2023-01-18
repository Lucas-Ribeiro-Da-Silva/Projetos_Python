print("""
- Jogo da palavra secreta: a palavra secreta está no módulo resposta.
- Não há limite de tentativas mas há um contador.
- No arquivo de respostas existe uma lista com 10 palavras que de forma.
pseudoaleatória são inseridas no jogo, a cada partida a ordem de exibição muda.
- Vale destacar que você pode inserir suas palavra no jogo modificando a lista.
Bom jogo!!!
""")

import random
import os
from resposta_pseudoaleatoria import lista

while True:
    random.shuffle(lista)
    tamanho_lista = len(lista)
    indice_aleatorio = random.randint(0, tamanho_lista-1)
    dicionario_palavra = lista[indice_aleatorio][0]
    palavra_secreta = dicionario_palavra['palavra_secreta']
    dicas = lista[indice_aleatorio][1]

    letras_acertadas = ''
    numero_tentativas = 0
    while True:
        if numero_tentativas==0:
            print('\ndica: ' + dicas['dica1'], end='\n\n')
        elif numero_tentativas == 5:
            print('\ndica: ' + dicas['dica2'], end='\n\n')
        elif numero_tentativas == 10:
            print('\ndica: ' + dicas['dica3'], end='\n\n')

        letra_digitada = input('Digite uma letra: ').lower()
        numero_tentativas += 1

        if len(letra_digitada) > 1:
            print('Digite apenas uma letra.')
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print('Palavra formada:', palavra_formada)

        if palavra_formada == palavra_secreta:
            #caso seu sistema operacional seja o linux, 
            # troque o comando 'cls' pelo comando 'clear'
            os.system('cls') 
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            print('-'*40)
            break

