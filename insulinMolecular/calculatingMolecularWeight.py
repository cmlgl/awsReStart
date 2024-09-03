import fileHandler

data = fileHandler.readJsonFile('files/insulin.json')

if data != "":
    aInsulin = data['molecules']['aInsulin']
    bInsulin = data['molecules']['bInsulin']
    insulin = aInsulin + bInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    print('aInsulin: ' + aInsulin)
    print('bInsulin: ' + bInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculando o peso molecular da insulina
    # Obtendo uma lista dos pesos de aminoácidos (AA)

    aaWeights = data['weights']

    # Contando o número de cada aminoácido (AA)

    aaCountInsulin = ({
        x: float(insulin.upper().count(x)) for x in
            ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    })

    # Multiplicando a contagem pelos pesos

    molecularWeightInsulin = sum({
        x: (aaCountInsulin[x] * aaWeights[x]) for x in
            ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    }.values())

    print('O peso molecular aproximado da insulina: ' + str(molecularWeightInsulin))
    print('Erro percentual: ' + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))

else:
    print('Erro. Saindo do programa...')