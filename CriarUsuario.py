def CriandoUsuarios():
    usuarios = {}
    while True:
        nome = input("Digite o nome do usuário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        try:
            idade = int(input("Digite a idade do usuário: "))
        except ValueError:
            print("Por favor, insira uma idade válida.")
            continue
        CNH = input("O usuário possui CNH? (S/N): ").strip().upper()
        if CNH == 'S':
            CNH = True
        else:
            CNH = False
        usuarios[nome] = {'idade': idade, 'CNH': CNH}
    
    return usuarios

# Executando a função para criar usuários
usuarios = CriandoUsuarios()

# Variáveis para armazenar contagens
MaiorDeIdade = 0
QtdCNH = 0

# Iterando pelos usuários e calculando as quantidades
for usuario, dados in usuarios.items():
    if dados['idade'] >= 18:
        MaiorDeIdade += 1
    if dados['CNH']:
        QtdCNH += 1

# Exibindo os resultados
print(f"A quantidade de usuários maiores de idade é: {MaiorDeIdade}")
print(f"A quantidade de usuários com CNH é: {QtdCNH}")
