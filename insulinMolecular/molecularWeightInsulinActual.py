# Armazenando a sequência da pré-pró-insulina humana em uma variável

preproInsulin = 'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr' \
'reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn'

# Armazenando os elementos restantes da sequência da insulina humana em variáveis

aInsulin = 'giveqcctsicslyqlenycn'
bInsulin = 'fvnqhlcgshlvealylvcgergffytpkt'
cInsulin = 'rreaedlqvgqvelgggpgagslqplalegslqkr'
dInsulin = 'malwmrllpllallalwgpdpaaa'
insulin = aInsulin + bInsulin

# Imprimindo "A sequência da insulina humana" no console usando comandos print() sucessivos

print('A sequência da pré-pró-insulina humana:')
print(preproInsulin)

# Imprimindo no console usando strings concatenadas dentro da função print (one-liner - única linha)

print('A sequência da insulina humana, cadeia a: ' + aInsulin)


# Calculando o peso molecular da insulina
# Criando uma lista de pesos de aminoácidos (AA)


aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

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


molecularWeightInsulinActual = 5807.63
print('Erro percentual: ' + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))