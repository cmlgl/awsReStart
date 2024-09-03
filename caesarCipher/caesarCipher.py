alphabet = 'ABC'

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input('Por favor, insira uma mensagem para criptografar:')
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input('Por favor, insira uma chave (número inteiro de 1 a 25):')
    return shiftAmount
        
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)

        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
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
    print(f'Mensagem criptografada: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabetTwo)
    print(f'Mensagem descriptografada: {myDecryptedMessage}')
    
runCaesarCipherProgram()