# Lógica do programa:

# 1. Peça ao usuário um palpite.
# 2. O palpite é o número certo?
# 3. Se o palpite estiver certo, diga ao usuário que o palpite estava certo e saia do loop.
# 4. Se o palpite estiver errado, diga ao usuário que o palpite estava errado e mantenha o loop.


import random

print('Bem-vindo ao Adivinhe o Número!')
print('As regras são simples. Eu pensarei em um número e você tentará adivinhá-lo.')

number = random.randint(1,10)
rightNumber = False

while rightNumber != True:
    guess = input('Adivinhe um número entre 1 e 10:')

    if int(guess) == number:
        print('Você adivinhou {}. Está correto! Você venceu!'.format(guess))
        rightNumber = True
    else:
        print('Você adivinhou {}. Desculpe, não está correto. Tente novamente.'.format(guess))

print('Contar até 10!')

for x in range(0,11):
    print(x)