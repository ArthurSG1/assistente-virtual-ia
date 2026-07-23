import json

# Abre a base de conhecimento
import json
import os

# Obtém a pasta onde está o app.py
pasta_atual = os.path.dirname(__file__)

# Monta o caminho até o arquivo JSON
caminho_json = os.path.join(pasta_atual, "..", "data", "base_conhecimento.json")

# Abre a base de conhecimento
with open(caminho_json, "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

print("=" * 50)
print("🛡️ CyberHelper AI")
print("=" * 50)

while True:

    pergunta = input("\nDigite sua pergunta (ou 'sair'): ").lower()

    if pergunta == "sair":
        print("\nAté logo!")
        break

    resposta_encontrada = False

    for palavra, resposta in base.items():

        if palavra in pergunta:

            print("\nResposta:\n")
            print(resposta)

            resposta_encontrada = True
            break

    if not resposta_encontrada:

        print("\nDesculpe.")
        print("Ainda não possuo informações sobre esse assunto.")