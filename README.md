# Gerador de Perguntas Automáticas (Teste Técnico - AI Team) - Peterson Rafael Chiquetto de Camargo

Este projeto é uma solução de software desenvolvida como parte do teste técnico para a equipe de Inteligência Artificial do GrupoQ. A aplicação analisa um trecho de texto educacional e gera automaticamente perguntas de múltipla escolha para auxiliar na revisão de conteúdo por parte dos alunos.

---

## Arquitetura do Projeto

Para garantir a qualidade, manutenibilidade e escalabilidade, o projeto foi desenvolvido com uma arquitetura modular, seguindo o princípio da **Separação de Responsabilidades (SoC)**.

```
(Estrutura de Pastas do Projeto)
├── core/
│   └── ai_generator.py      # Módulo principal da IA.
├── utils/
│   └── file_handler.py      # Módulo utilitário para arquivos.
├── gerador_perguntas.py     # Ponto de entrada (orquestrador) da aplicação.
├── prompts.py               # Armazena os templates de prompts para a IA.
├── requirements.txt         # Lista de dependências do projeto.
└── .env.example             # Arquivo de exemplo para as variáveis de ambiente.
```

- **`gerador_perguntas.py`**: Orquestra o fluxo da aplicação.
- **`core/ai_generator.py`**: Camada de serviço que lida com toda a comunicação com a API do Google Generative AI.
- **`utils/file_handler.py`**: Camada de utilitários responsável por interações com o sistema de arquivos.
- **`prompts.py`**: Isola as instruções enviadas à IA, facilitando a manutenção e o ajuste fino (Prompt Engineering).

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **Google Generative AI API** (com o modelo `gemini-1.5-flash-latest`)
- **Bibliotecas**: `google-generativeai`, `python-dotenv`

---

## Como Configurar e Executar o Projeto

Siga os passos abaixo para executar a aplicação.

**1. Descompacte o Projeto**
   - Extraia o conteúdo do arquivo `.zip` para uma pasta de sua preferência no seu computador.

**2. Abra um Terminal na Pasta do Projeto**
   - Navegue através do seu terminal (PowerShell, CMD, etc.) até a pasta que você acabou de extrair.

**3. Crie e Ative um Ambiente Virtual**
   - É uma boa prática isolar as dependências do projeto.
   ```bash
   # Criar o ambiente virtual
   python -m venv venv

   # Ativar no Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

**4. Instale as Dependências**
   - Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

**5. Configure sua Chave de API (Passo Essencial)**
   - Este projeto necessita de uma chave de API do Google AI Studio para funcionar.
   - Na pasta do projeto, você encontrará um arquivo chamado **`.env.example`**.
   - **Copie este arquivo e renomeie a cópia para `.env`**.
   - Abra o novo arquivo `.env` e substitua o valor `SUA_CHAVE_DE_API_VEM_AQUI` pela sua chave de API pessoal e válida.

**6. Execute a Aplicação**
   - Agora, com tudo configurado, execute o script principal:
   ```bash
   python gerador_perguntas.py
   ```

O script irá ler o arquivo `texto_aula.txt`, gerar as perguntas, exibi-las no terminal e salvar o resultado final no arquivo `saida_perguntas.txt`, que será criado na mesma pasta.