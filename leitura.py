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
                    
        # Ordena alfabeticamente pela primeira posição da tupla (pergunta)
        base_dados.sort()
                    
        if base_dados:
            print("O que eu já sei:")
            for pergunta, resposta in base_dados:
                print(f"{pergunta} - {resposta}")
        else:
            print("Bot: Ainda não aprendi nada.")
            
    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! Me ensine algo primeiro.")






















