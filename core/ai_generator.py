# core/ai_generator.py

import json
import google.generativeai as genai
from prompts import PROMPT_GERADOR_PERGUNTAS

class AIGenerator:
    """
    Encapsula toda a lógica de interação com a API do Google Generative AI.

    Esta classe atua como a camada de serviço de IA, abstraindo a complexidade
    da configuração do modelo e da geração de conteúdo. Ao centralizar a lógica aqui,
    facilitamos a manutenção, a testabilidade e futuras substituições do provedor de IA.
    """

    def __init__(self, api_key: str, model_name: str = 'models/gemini-1.5-flash-latest'):
        """
        Construtor da classe. Inicializa e configura o cliente do modelo de IA.

        Args:
            api_key (str): A chave de API necessária para autenticação no serviço.
            model_name (str): O identificador do modelo a ser utilizado. O padrão é um
                              modelo rápido e eficiente.

        Raises:
            ValueError: Lançado se a chave de API não for fornecida, evitando
                        que o objeto seja instanciado em um estado inválido.
        """
        # Validação de pré-condição: garante que a chave de API foi fornecida.
        if not api_key:
            raise ValueError("Chave de API não encontrada.")
        
        # Configura a biblioteca do Google com a chave fornecida.
        genai.configure(api_key=api_key)
        
        # Instancia o modelo generativo e o armazena como um atributo da classe.
        self.model = genai.GenerativeModel(model_name)
        
        print(f"Modelo de IA '{model_name}' configurado com sucesso.")

    def gerar_perguntas_from_text(self, texto_base: str) -> list | None:
        """
        Orquestra a geração de perguntas a partir de um texto base.

        Este método recebe o texto, formata-o dentro do prompt pré-definido,
        envia a requisição para a API e processa a resposta, garantindo que
        ela seja um JSON válido.

        Args:
            texto_base (str): O conteúdo educacional a ser analisado pela IA.

        Returns:
            list | None: Uma lista de dicionários contendo as perguntas geradas,
                         ou None em caso de falha na comunicação ou processamento.
        """
        # Injeta o texto do usuário no template do prompt, preparando a instrução final para a IA.
        prompt_final = PROMPT_GERADOR_PERGUNTAS.format(texto_da_aula=texto_base)
        
        print("Gerando perguntas com base no texto... Por favor, aguarde.")
        
        try:
            # Realiza a chamada síncrona para a API, enviando o prompt.
            response = self.model.generate_content(prompt_final)
            
            # Etapa de sanitização: remove marcações (como ```json) que a IA pode
            # adicionar à resposta, garantindo que tenhamos uma string JSON pura.
            cleaned_json_string = response.text.strip().replace("```json", "").replace("```", "").strip()
            
            # Desserializa a string JSON em uma estrutura de dados Python (lista de dicionários).
            # Este é um ponto crítico que valida se a IA seguiu o formato solicitado.
            return json.loads(cleaned_json_string)

        except Exception as e:
            # Tratamento genérico de exceções para capturar qualquer falha durante a chamada da API
            # ou o parsing do JSON, garantindo a resiliência da aplicação.
            print(f"\n[ERRO] A resposta da API não foi um JSON válido ou ocorreu outro erro: {repr(e)}")
            return None