import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)

    except IOError:
        print('Não foi possível ler o arquivo.')

    return data