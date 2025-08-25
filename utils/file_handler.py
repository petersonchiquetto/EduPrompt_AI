# utils/file_handler.py
"""
Módulo utilitário para centralizar as operações de entrada e saída (I/O) de arquivos.

Abstrair a manipulação de arquivos em funções dedicadas promove a reutilização de código
e a separação de responsabilidades (SoC), tornando o código principal mais limpo e focado
em sua lógica de negócio, sem se preocupar com os detalhes da manipulação de arquivos.
"""

def ler_arquivo_texto(caminho_arquivo: str) -> str | None:
    """
    Lê o conteúdo de um arquivo de texto de forma segura.

    Tenta abrir e ler um arquivo especificado, tratando exceções comuns como
    a não localização do arquivo ou outros erros de permissão de leitura.

    Args:
        caminho_arquivo (str): O caminho relativo ou absoluto para o arquivo de texto.

    Returns:
        str | None: O conteúdo do arquivo como uma string em caso de sucesso,
                     ou None se ocorrer qualquer erro durante a leitura.
    """
    try:
        # O gerenciador de contexto 'with' garante que o arquivo seja fechado
        # automaticamente, mesmo que ocorram erros. 'encoding="utf-8"' é
        # fundamental para garantir a compatibilidade com diferentes caracteres.
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    
    # Trata de forma específica o erro mais comum para esta operação.
    except FileNotFoundError:
        print(f"[ERRO] Arquivo de entrada não encontrado em '{caminho_arquivo}'")
        return None
    
    # Captura outras exceções de I/O (ex: permissões de leitura negadas)
    # para garantir que a aplicação não pare de forma inesperada.
    except Exception as e:
        print(f"[ERRO] Falha ao ler o arquivo: {repr(e)}")
        return None

def salvar_saida_texto(conteudo: str, caminho_arquivo: str):
    """
    Salva uma string de conteúdo em um arquivo de texto.

    Abre um arquivo em modo de escrita ('w'), o que cria um novo arquivo ou
    sobrescreve completamente um arquivo existente, e salva o texto fornecido.

    Args:
        conteudo (str): O texto a ser salvo no arquivo.
        caminho_arquivo (str): O caminho onde o arquivo será criado ou sobrescrito.
    """
    try:
        # O modo 'w' (write) é usado para escrever no arquivo. Se o arquivo
        # não existir, ele será criado. Se existir, seu conteúdo será apagado.
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"Resultados salvos com sucesso em '{caminho_arquivo}'")
        
    # Captura exceções de I/O (ex: caminho inválido, permissões de escrita negadas).
    except Exception as e:
        print(f"[ERRO] Falha ao salvar o arquivo de saída: {repr(e)}")