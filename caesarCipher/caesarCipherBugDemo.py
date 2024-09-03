# Laboratório de módulo: Bug nº 1 do programa Caesar Cipher

# Em um laboratório anterior foi criado o programa Caesar Cipher (Cifra de César).
# Esta versão do programa está com bugs mas não será depurada, pois servirá como demonstração.


# Dobrando o alfabeto fornecido
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


# A variável "alphabet" está no lugar certo? O bug pode estar aqui
alphabet = 'ABC'


# Recebendo uma mensagem para criptografar
def getMessage():
    stringToEncrypt = input('Por favor, insira uma mensagem para criptografar:')
    return stringToEncrypt

# Obtendo uma chave de cifra
def getCipherKey():
    shiftAmount = input('Por favor, insira uma chave (números inteiros de 1 a 25):')
    return shiftAmount

# Criptografando mensagem
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        
        # A variável "newPosition" está completa? O bug pode estar aqui
        newPosition = position + (cipherKey)

        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


# Descriptografando mensagem
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Lógica do programa principal
def runCaesarCipherProgram():
    myAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Alfabeto: {myAlphabet}')

    myAlphabetTwo = getDoubleAlphabet(myAlphabet)
    print(f'Alfabeto dois: {myAlphabetTwo}')

    myMessage = getMessage()
    print(myMessage)

    myCipherKey = getCipherKey()
    print(myCipherKey)

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabetTwo)
    print(f'Criptografando mensagem: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabetTwo)
    print(f'Descriptografando mensagem: {myDecryptedMessage}')

# Rodando o programa
runCaesarCipherProgram()