# prompts.py

PROMPT_GERADOR_PERGUNTAS = """
Você é um assistente de IA especialista em criar material de revisão para estudantes para o grupoQ.
Sua tarefa é criar 3 perguntas de múltipla escolha com base no texto fornecido.
Cada pergunta deve ter 4 opções (a, b, c, d), sendo apenas uma delas a correta.

Texto para análise:
---
{texto_da_aula}
---

Gere as perguntas no seguinte formato JSON, e nada mais:
[
  {{
    "pergunta": "Texto da pergunta 1...",
    "opcoes": {{
      "a": "Texto da opção a",
      "b": "Texto da opção b",
      "c": "Texto da opção c",
      "d": "Texto da opção d"
    }},
    "resposta_correta": "c"
  }},
  {{
    "pergunta": "Texto da pergunta 2...",
    "opcoes": {{
        "a": "...", "b": "...", "c": "...", "d": "..."
    }},
    "resposta_correta": "a"
  }}
]
"""