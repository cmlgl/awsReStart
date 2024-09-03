number = 250

while number <= 251:
    print('Vamos verificar se o número escolhido é primo e seu resultado.')

    primeNumber = int(input('Escolha um número entre 1 e 250:'))
    mult = 0
    
    for count in range(2,primeNumber):
        if (primeNumber % count == 0):
            print(primeNumber,'é múltiplo de',count)
            mult += 1

    if (mult == 0):
         print(primeNumber,'é um número primo.')

         # Quando esta atividade foi realizada seu caminho absoluto era:
         print('Caminho absoluto do arquivo: /home/ec2-user/environment')
    else:
         print('Tem',mult,'múltiplos acima de 2 e abaixo de',primeNumber)
         print('Caminho absoluto do arquivo: /home/ec2-user/environment')