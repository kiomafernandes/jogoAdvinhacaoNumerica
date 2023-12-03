import random

print('Seja bem vindo(a) ao jogo de advinha numerico')
choice_number = input('Digite o numero teto do desafio: ').strip()

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: Valor informado não é um numero ou inseriu espaço. Favor execute novamente e informe um numero!")
    quit()


random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input('Advinhe o numero: ').strip()


    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print('Erro: valor informado não é numerico ou inseriu espaço. Favor informe um numero!')
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print('Acertou!')
        break
    elif answer_user > random_number:
        print('Chutou alto, o numero randomico é menor que isso!')
    elif answer_user < random_number:
        print('Chutou baixo, o numero randomico é meior que isso!')

print('Nº de tentativas:' + str(n_choices))
