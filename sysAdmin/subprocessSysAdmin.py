import subprocess

# Exibindo os arquivos do diretório em listagem longa. Exibindo o diretório "files"
subprocess.run(['ls','-l','files'])


# Usando o comando "uname -a" para exibir informações do sistema
command = 'uname'
commandArgument = '-a'

print(f'Coletando informações do sistema com o comando: {command} {commandArgument}')
subprocess.run([command,commandArgument])


# Usando o comando "ps -x" para exibir informações de disco (executando o comando "df")
command = 'ps'
commandArgument = '-x'

print(f'Coletando informações do processo ativo com o comando: {command} {commandArgument}')
subprocess.run([command,commandArgument])