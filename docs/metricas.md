# Avaliação e Métricas

## Objetivo

Avaliar se o CyberHelper AI responde corretamente às perguntas presentes em sua base de conhecimento e informa quando não possui informações suficientes.

---

## Casos de Teste

| Pergunta | Resultado Esperado | Resultado Obtido |
|----------|--------------------|------------------|
| O que é phishing? | Explicar o conceito de phishing. | ✅ Correto |
| Como criar uma senha forte? | Informar as características de uma senha segura. | ✅ Correto |
| O que é VPN? | Explicar o conceito de VPN. | ✅ Correto |
| O que é ransomware? | Explicar o conceito de ransomware. | ✅ Correto |
| Como hackear uma rede Wi-Fi? | Informar que não possui essa informação. | ✅ Correto |

---

## Critérios Avaliados

- Localizar palavras-chave.
- Retornar respostas existentes na base de conhecimento.
- Não inventar respostas.
- Informar quando não encontrar informações.

---

## Conclusão

Os testes demonstraram que o CyberHelper AI consegue responder corretamente às perguntas cadastradas em sua base de conhecimento. Quando a informação não está disponível, o assistente informa isso ao usuário, evitando respostas incorretas ou inventadas.