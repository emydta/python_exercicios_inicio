import random

print('Bem-vindo(a) ao jogo da adivinhação!')
print('Tente adivinhar um número entre 1 e 50. Você tem 5 tentativas!')

nmr_escolhido = random.randint(1, 50)
tentativas = 0

while True:
        try:
            palpite = (int(input('Seu palpite: ')))
            tentativas +=1

            if palpite == nmr_escolhido:
                print(f'Parabéns! Você acertou com {tentativas} tentativas!')
                break
            
            elif palpite < nmr_escolhido:
                print('Muito baixo! Tente um número maior.')
            else:
                print('Muito alto! Tente um número menor.')

        except ValueError:
            print("Por favor, insira um número válido.")

