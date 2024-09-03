# Armazenando a sequência da pré-pró-insulina humana em uma variável

preproInsulin = 'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr' \
'reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn'

# Armazenando os elementos restantes da sequência da insulina humana em variáveis

aInsulin = 'giveqcctsicslyqlenycn' 
bInsulin = 'fvnqhlcgshlvealylvcgergffytpkt'
cInsulin = 'rreaedlqvgqvelgggpgagslqplalegslqkr'  
dInsulin = 'malwmrllpllallalwgpdpaaa'  
insulin = aInsulin + bInsulin

pKR = {
    'Y': 10.07,
    'C': 8.18,
    'K': 10.53,
    'H': 6.00,
    'R': 12.48,
    'D': 3.65,
    'E': 4.25
}

insulin.count('Y')
float(insulin.count('Y'))

seqCount = ({
    x: float(insulin.count(x)) for x in
        ['Y', 'C', 'K', 'H', 'R', 'D', 'E']
})

pH = 0

while (pH <= 14):
    netLoad = 
        (+(sum({
            x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \
                for x in 
                    ['K', 'H', 'R']
        }.values()))

        -(sum({
            x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \
                for x in 
                    ['Y', 'C', 'D', 'E']
        }.values())))
    
    print('{0:.2f}'.format(pH), netLoad)
    pH += 1