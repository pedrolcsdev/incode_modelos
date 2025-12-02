import os
from groq import Groq
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do Cliente
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# --- Definição dos Prompts (Estratégia Tree of Thoughts) ---
prompt_sistema = """
Voce e uma pessoa amigável e breve.
"""
while True:
    prompt_usuario = input('Você: ')
    if prompt_usuario.lower() == 'sair':
        break

    # Função auxiliar para enviar o prompt
    def consultar_groq(prompt_sistema, prompt_usuario):
        print(f"\n--- Enviando: {prompt_usuario} ---")
        
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0, # Baixa temperatura para ser mais analítico
        )
        
        resposta = completion.choices[0].message.content
        print(f"RESPOSTA DA IA:\n{resposta}")

    # Execução do código
    if __name__ == "__main__":
        consultar_groq(prompt_sistema, prompt_usuario)
        print()
    