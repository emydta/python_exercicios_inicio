ano_nasc = (int(input('Insira seu ano de nascimento: ')))

idade = 2025 - ano_nasc

if idade >= 65:
    print(idade,'. Já pode se aposentar')
else:
    print(idade, '. Ainda não pode se aposentar')