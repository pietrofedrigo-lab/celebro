def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if " - " in linha:
                    pergunta, resposta = linha.strip().split(" - ", 1)
                    if fala == pergunta:
                        print(f"Bot: {resposta}")
                        encontrou = True
                        break
                        
    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! Me ensine algo primeiro.")
        return

    if not encontrou:
        print("Bot: Desculpe, não sei a resposta. Use a opção 2 para me ensinar.")

def ensinar():
    pergunta = input("Digite a pergunta que deseja me ensinar: ").strip().lower()
    resposta = input("Digite a resposta para essa pergunta: ").strip()
    
    # Abre o arquivo em modo "a" (append) para adicionar no final sem apagar o que já existe
    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta} - {resposta}\n")
        
    print("Bot: Obrigado por me ensinar!")

def listar_conhecimento():
    base_dados = []
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    # Cria tupla (pergunta, resposta) e adiciona na lista
                    base_dados.append((dados[0], dados[1]))
                    
        # Ordena alfabeticamente pela primeira posição da tupla
        base_dados.sort()
        
        print("\n--- MEMÓRIA DO PYBOT (ORDENADA) ---")
        if base_dados:
            for item in base_dados:
                print(f"Pergunta: {item[0]} -> Resposta: {item[1]}")
        else:
            print("Nenhum dado cadastrado ainda.")
            
    except FileNotFoundError:
        print("Nenhum dado cadastrado ainda.")

# O programa principal começa aqui
while True:
    print("\n--- MENU ---")
    print("1. Conversar com o bot")
    print("2. Ensinar nova resposta")
    print("3. Lista conhecimento (A-Z)")
    print("4. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar() 
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")






















