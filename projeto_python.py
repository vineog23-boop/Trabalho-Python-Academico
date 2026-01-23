import json  # Biblioteca para trabalhar com JSON


def carregar_dados():
    """
    Lê o arquivo JSON (portfolio.json) e transforma o conteúdo em um dicionário.
    Se o arquivo não existir ou estiver corrompido, devolve um dicionário novo.
    """
    try:
        with open("portfolio.json", "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)  # Lê o arquivo e converte de JSON para dicionário
            return conteudo
    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Criando novo portfólio.")
        return {"vistos": [], "ver_depois": []}
    except json.JSONDecodeError:
        print("Arquivo corrompido ou vazio. Criando novo portfólio.")
        return {"vistos": [], "ver_depois": []}


def salvar_dados(informacoes):
    """
    Recebe um dicionário e grava esse conteúdo dentro do arquivo JSON.
    """
    with open("portfolio.json", "w", encoding="utf-8") as arquivo:
        json.dump(informacoes, arquivo, indent=4, ensure_ascii=False)


# Mensagem inicial com os comandos disponíveis
print("""
Bem-vindo ao Meu Gerenciador de Conteúdos.

Comandos disponíveis:
ABOUT - sobre o sistema
ADD VISTOS - adicionar um conteúdo já assistido
ADD VER DEPOIS - adicionar algo para assistir depois
LISTA VISTOS - ver conteúdos já assistidos
LISTA PARA ASSISTIR - ver conteúdos salvos para assistir depois
QUIT - salvar e sair do programa
""")

# Carrega o que estava salvo no arquivo, se existir.
arquivo_memoria = carregar_dados()

# Loop principal da aplicação
while True:
    comando = input("Digite um comando: ")
    comando_padrao = comando.strip().upper()  # Normaliza o comando

    if comando_padrao == "ABOUT":
        print("""
Este é o Meu Gerenciador de Conteúdos.
Você pode salvar conteúdos que já assistiu e conteúdos para ver depois.
Os dados são salvos em arquivo para você não perder as informações.
""")

    elif comando_padrao == "ADD VISTOS":
        titulo = input("Digite o nome do conteúdo que você já assistiu: ").strip()
        if titulo == "":
            print("ERRO: o título não pode ser vazio.")
        else:
            arquivo_memoria["vistos"].append(titulo)
            print(f'"{titulo}" foi adicionado à lista de conteúdos já vistos.')

    elif comando_padrao == "ADD VER DEPOIS":
        titulo = input("Digite o nome do conteúdo para assistir depois: ").strip()
        if titulo == "":
            print("ERRO: o título não pode ser vazio.")
        else:
            arquivo_memoria["ver_depois"].append(titulo)
            print(f'"{titulo}" foi adicionado à lista de conteúdos para assistir depois.')

    elif comando_padrao == "LISTA VISTOS":
        if not arquivo_memoria["vistos"]:
            print("Nenhum conteúdo registrado como visto ainda.")
        else:
            print("Conteúdos já assistidos:")
            for i, conteudo in enumerate(arquivo_memoria["vistos"], start=1):
                print(f"{i}. {conteudo}")

    elif comando_padrao == "LISTA PARA ASSISTIR":
        if not arquivo_memoria["ver_depois"]:
            print("Nenhum conteúdo salvo para assistir depois.")
        else:
            print("Conteúdos para assistir depois:")
            for i, conteudo in enumerate(arquivo_memoria["ver_depois"], start=1):
                print(f"{i}. {conteudo}")

    elif comando_padrao == "QUIT":
        # Salva tudo o que está em memória no arquivo JSON antes de sair
        salvar_dados(arquivo_memoria)
        print("Dados salvos. Saindo do Gerenciador. Até logo!")
        break

    else:
        print("Erro. Comando inválido.")
