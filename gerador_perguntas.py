# gerador_perguntas.py
"""
Ponto de entrada principal e orquestrador da aplicação de geração de perguntas.

Este script é responsável por coordenar o fluxo de execução da aplicação,
seguindo três etapas principais:
1.  **Inicialização:** Carrega as configurações (variáveis de ambiente) e os dados
    de entrada (arquivo de texto).
2.  **Execução:** Instancia e utiliza os serviços da camada `core` (AIGenerator)
    para executar a lógica de negócio principal.
3.  **Apresentação:** Formata e exibe os resultados para o usuário, além de
    salvá-los em um arquivo de saída utilizando funções da camada `utils`.

A estrutura com a função `run()` e a verificação `if __name__ == "__main__"`
é uma prática padrão em Python para criar scripts executáveis e reutilizáveis.
"""

import os
from dotenv import load_dotenv
from core.ai_generator import AIGenerator
from utils.file_handler import ler_arquivo_texto, salvar_saida_texto

def formatar_saida_para_exibicao(perguntas: list) -> str:
    """
    Converte a lista de dicionários de perguntas em uma string formatada.

    Este método atua como uma camada de "apresentação" (view), sendo responsável
    apenas pela formatação estética dos dados para exibição ao usuário final,
    sem alterar os dados em si.

    Args:
        perguntas (list): A lista de dicionários, onde cada dicionário
                          representa uma pergunta gerada pela IA.

    Returns:
        str: Uma string única, formatada para ser impressa no console ou salva em arquivo.
    """
    output_string = "--- Perguntas de Revisão Geradas Automaticamente ---\n\n"
    # `enumerate(perguntas, 1)` inicia a contagem a partir do 1 para a numeração.
    for i, p in enumerate(perguntas, 1):
        output_string += f"{i}. {p['pergunta']}\n"
        for key, value in p['opcoes'].items():
            output_string += f"   {key}) {value}\n"
        output_string += f"   => Resposta Correta: {p['resposta_correta']}\n\n"
    return output_string

def run():
    """
    Função principal que orquestra todo o fluxo da aplicação.
    """
    # Carrega as variáveis de ambiente do arquivo .env para a sessão atual.
    load_dotenv()
    
    # Define as constantes para os nomes dos arquivos, facilitando a manutenção.
    ARQUIVO_INPUT = "texto_aula.txt"
    ARQUIVO_OUTPUT = "saida_perguntas.txt"
    
    # --- ETAPA 1: INICIALIZAÇÃO E CONFIGURAÇÃO ---
    print("Iniciando o processo de geração de perguntas...")
    api_key = os.getenv("GOOGLE_API_KEY")
    texto_base = ler_arquivo_texto(ARQUIVO_INPUT)
    
    # Validação de guarda (Guard Clause): Interrompe a execução cedo se as
    # condições essenciais (chave de API e texto) não forem atendidas.
    if not api_key or not texto_base:
        print("Execução interrompida. Verifique o arquivo .env e o arquivo de texto de entrada.")
        return

    # --- ETAPA 2: EXECUÇÃO DA LÓGICA PRINCIPAL ---
    try:
        # Instancia o serviço de IA, injetando a dependência da chave de API.
        ai_service = AIGenerator(api_key=api_key)
        # Chama o método principal para obter o resultado.
        lista_de_perguntas = ai_service.gerar_perguntas_from_text(texto_base)
        
        # --- ETAPA 3: APRESENTAÇÃO DOS RESULTADOS ---
        if lista_de_perguntas:
            # Passa os dados brutos para a função de formatação.
            saida_formatada = formatar_saida_para_exibicao(lista_de_perguntas)
            
            print("\n" + "="*50)
            print(saida_formatada)
            print("="*50)

            # Utiliza o serviço de arquivos para persistir o resultado.
            salvar_saida_texto(saida_formatada, ARQUIVO_OUTPUT)
        else:
            print("Nenhuma pergunta foi gerada devido a um erro anterior.")
            
    except Exception as e:
        # Um bloco de captura de exceção de último recurso para qualquer erro
        # não tratado nas camadas inferiores, garantindo que o programa termine de forma controlada.
        print(f"\n[ERRO] Uma falha crítica no fluxo principal ocorreu: {repr(e)}\n")

# A verificação `if __name__ == "__main__"` é o padrão ouro em Python.
# Ela garante que a função `run()` só seja executada quando o script é chamado
# diretamente, e não quando é importado por outro módulo.
if __name__ == "__main__":
    run()