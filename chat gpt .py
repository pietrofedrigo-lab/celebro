import requests
import sys

# 1. COLOCA A TUA CHAVE AQUI DENTRO DAS ASPAS
CHAVE_API = "SUA_CHAVE_AQUI"

if CHAVE_API == "SUA_CHAVE_AQUI":
    print("ERRO: Precisas de colocar a tua chave verdadeira na variável CHAVE_API.")
    sys.exit()

# Configuração da ligação à API
cabecalhos = {
    "Authorization": f"Bearer {CHAVE_API}",
    "Content-Type": "application/json"
}

# Memória do bot
historico = [
    {"role": "system", "content": "És um assistente inteligente e amigável."}
]

print("\n--- CHATGPT NO TERMINAL (Versão Direta) ---")
print("Escreve 'sair' para terminar.\n")

while True:
    mensagem = input("Tu: ").strip()
    
    if mensagem.lower() == 'sair':
        print("Até logo!")
        break
        
    historico.append({"role": "user", "content": mensagem})
    
    dados = {
        "model": "gpt-3.5-turbo",
        "messages": historico
    }
    
    try:
        # Faz o pedido diretamente ao site da OpenAI
        resposta = requests.post(
            "https://api.openai.com/v1/chat/completions", 
            headers=cabecalhos, 
            json=dados
        )
        
        resultado = resposta.json()
        
        # Verifica se a API devolveu algum erro (ex: falta de saldo, chave errada)
        if "error" in resultado:
            print(f"\nERRO DA OPENAI: {resultado['error']['message']}\n")
            historico.pop() # Remove a mensagem para não bloquear a conversa
            continue
            
        texto_resposta = resultado["choices"][0]["message"]["content"]
        print(f"\nChatGPT: {texto_resposta}\n")
        
        historico.append({"role": "assistant", "content": texto_resposta})
        
    except Exception as e:
        print(f"\nErro de ligação à internet: {e}\n")
        historico.pop()