import csv

# O leitor irá salvar os dados no escopo da função caso houver cabeçalho dentro do arquivo.csv
def leitor_dados_em_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, mode="r") as file:
        leitor = csv.reader(file, delimiter=';')
        cabecalho = next(leitor, None) 
        if cabecalho is not None:
            for i in leitor:           
                dados.append(i)
    return dados

def salvar_dados_em_csv(nomes, ids, senhas, dtsNascimento, emails, cargos, nome_arquivo):
    with open(nome_arquivo, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Nome', 'ID', 'Senha', 'Data de Nascimento', 'Email', 'Cargo'])
        for i in range(5):
            writer.writerow([nomes[i], ids[i], senhas[i], dtsNascimento[i], emails[i], cargos[i]])
        print("Os dados foram gravados com sucesso!")

def verificadorsenha(senha):
    while not senha.isalnum():
        print("Senha inválida")
        senha = input("Caracteres especiais não permitidos, digite novamente: ")
    return senha

def cifra_de_cesar(texto, chave):
    resultado = ''
    for letra in texto:
        if letra.isalpha():  
            if letra.islower():  
                resultado += chr(((ord(letra) - ord('a') + chave) % 26) + ord('a'))
            else: 
                resultado += chr(((ord(letra) - ord('A') + chave) % 26) + ord('A'))
        else:
            resultado += letra  
    return resultado

def criptografar_senha(senha, chave):
    senha_cifrada = cifra_de_cesar(senha, chave)
    return senha_cifrada

def descriptografar_senha(senha_cifrada, chave):
    senha_original = cifra_de_cesar(senha_cifrada, -chave)  
    return senha_original

nome_de_usuario = [""]
id_do_usuario = [""]
senha_do_usuario = [""]
dt_de_nascimento = [""]
email_usuario = [""]
cargo_usuario = [""]
caracteresespeciais = (';', ',', '!', '?', '%', '#', '&', '¨', '*', '()', '[]', '/', '|', '-', '+', '=', '_', '$', '<', '>', '^', '~', '`')
i = False
contador = 0
nome_repetido = str
final = 's'

pergunta = input("Deseja cadastrar um novo usuário? (S) (N): ")
if pergunta.lower() == 's':
    while final.lower() == 's' and contador <= 5 and i == False:
        # Nome do usuário
        nome_usuario = input("Digite nome de usuário: ")
        if not nome_usuario.isalpha() or nome_usuario.isspace():
            print('Nome inserido incorretamente. Por favor, escreva novamente.')
        elif nome_usuario in nome_de_usuario:
            nome_repetido = input("Esse nome de usuário já está cadastrado. Deseja continuar? (S) (N): ")
            if nome_repetido.lower() == 's':
                continue
            elif nome_repetido.lower() == 'n':
                print("Digite o novo nome de usuário:")
                continue
        else:
            # ID do Usuário:
            while True:
                id_usuario = input('Digite o seu ID (7 DÍGITOS): ')
                id_usuario = id_usuario.strip()
                if len(id_usuario) !=7 or not id_usuario.isdigit():
                    print('Dados inseridos incorretamente, por favor, digite novamente!')
                    continue
                elif id_usuario in id_do_usuario:
                    print('\nO ID informado foi cadastrado anteriormente.')
                    print('O programa irá ser encerrado.\n')
                    exit()
                else:
                    break
            nome_de_usuario[i] = nome_usuario
            id_do_usuario [i] = id_usuario
            
            # Senha:
            senha = input('Digite a senha de usuário: ')
            senha = verificadorsenha(senha)
            senha_cifrada = criptografar_senha(senha, 9)
            senha_do_usuario[i] = senha_cifrada
    
            # Data de Nascimento:
            ano_atual = 2023
            while True:
                dt_nascimento = input("Digite a data de nascimento:DD-MM-AAAA: ")
                dma = dt_nascimento.split('-') 
                if len(dma) == 3:
                    dia = int(dma[0])
                    mes = int(dma[1])
                    ano = int(dma[2])
                    if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano >= 1953 and ano <= 2003:
                        break
                else: 
                    print('Data de nascimento inválida, verifique data inserida e digite uma data válida: ')
                    continue 
            dt_de_nascimento[i] = dt_nascimento
            
            # E-mail:
            while True:
                email = input("Digite o seu e-mail: ")
                if any(char in email for char in caracteresespeciais):   
                    print('Endereço de e-mail inválido. Por favor, digite outro e-mail.')
                    continue
                elif email in email_usuario:
                    print('Endereço de e-mail já cadastrado. Por favor, digite outro e-mail.')
                    continue
                else:
                    break
            email_usuario[i] = email
            
            # Cargo:
            while True:
                cargo = input("Digite o seu cargo na empresa: ")
                if all(f.isalpha() or f.isspace() for f in cargo):
                    break
                else:
                    print("Digite um cargo válido: ")
                continue
            cargo_usuario[i] = cargo
            
            print("Usuário cadastrado :)")
            print("-"*46)
            
            nome_de_usuario.append(nome_usuario)
            id_do_usuario.append(id_usuario)
            senha_do_usuario.append(senha)
            dt_de_nascimento.append(dt_nascimento)
            email_usuario.append(email)
            cargo_usuario.append(cargo)

        contador += 1 

        if(contador == 5):
            escolha = input("Deseja continuar s/n?: ")
            salvar_dados_em_csv(nome_de_usuario, id_do_usuario, senha_do_usuario, dt_de_nascimento, email_usuario, cargo_usuario, 'usuarios.csv')
            leitor_dados_em_csv('usuarios.csv')
            if(escolha.lower == 's'):
                nome_usuario.clear()
                id_usuario.clear()
                senha.clear()
                dt_nascimento.clear()
                email.clear()
                cargo.clear()
                contador = 0
            else:
                i = True

else:
    print()
    print ("Finalizando programa...")
    exit()