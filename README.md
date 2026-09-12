<h1 align="center">🐍 Gerenciador de Conteúdos</h1>
<p align="center">Uma aplicação de terminal para organizar o que assistir.</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3-2563EB?style=flat-square" alt="Python: 3">
  <img src="https://img.shields.io/badge/Persist%C3%AAncia-JSON-0F766E?style=flat-square" alt="Persistência: JSON">
  <img src="https://img.shields.io/badge/Tipo-Projeto%20acad%C3%AAmico-475569?style=flat-square" alt="Tipo: Projeto acadêmico">
</p>

<p align="center"><a href="#visão-geral">Visão geral</a> · <a href="#como-executar">Execução</a> · <a href="#próximos-passos">Próximos passos</a></p>

---

## Visão geral

Aplicação acadêmica em Python para registrar conteúdos já assistidos e conteúdos para ver depois. A interação acontece no terminal, e as listas são salvas em `portfolio.json`.

O projeto exercita funções, listas, dicionários, tratamento de exceções e leitura/escrita de JSON usando apenas a biblioteca padrão.

## Funcionalidades

- Carregar as listas salvas ou iniciar um portfólio vazio.
- Adicionar conteúdos às listas de vistos e para assistir.
- Consultar as duas listas por comandos de terminal.
- Salvar os dados ao encerrar pelo comando `QUIT`.
- Tratar arquivo ausente ou JSON inválido durante o carregamento.

## Como executar

Com **Python 3** instalado:

```bash
git clone https://github.com/vineog23-boop/Trabalho-Python-Academico.git
cd Trabalho-Python-Academico
python3 projeto_python.py
```

No Windows, use `py projeto_python.py` ou `python projeto_python.py`, conforme a instalação. Não é necessário instalar pacotes.

## Comandos disponíveis

| Comando | Ação |
| --- | --- |
| `ABOUT` | Exibe informações sobre o sistema. |
| `ADD VISTOS` | Adiciona um conteúdo já assistido. |
| `ADD VER DEPOIS` | Adiciona um conteúdo para assistir depois. |
| `LISTA VISTOS` | Mostra a lista de conteúdos assistidos. |
| `LISTA PARA ASSISTIR` | Mostra a lista para assistir. |
| `QUIT` | Salva os dados e encerra. |

Execute o programa dentro da pasta do projeto. O arquivo `portfolio.json` é lido e gravado no diretório de execução.

## Organização

| Arquivo | Responsabilidade |
| --- | --- |
| `projeto_python.py` | Carregamento, interação pelo terminal e persistência. |
| `portfolio.json` | Dados locais criados durante o uso. |
| `LICENSE` | Licença do projeto. |

## Verificação e limites

Não há testes automatizados. Para verificar o fluxo manualmente, adicione um item em cada lista, consulte-os, encerre com `QUIT` e abra novamente para confirmar a persistência.

O projeto é uma aplicação local de terminal; não possui interface gráfica, banco de dados externo ou múltiplos usuários.

## Próximos passos

- Separar a interação do terminal das funções de domínio.
- Adicionar testes de carregamento e persistência.
- Melhorar validação de entrada e edição dos conteúdos.

## Autor

**Vinícius Oliveira** · [GitHub](https://github.com/vineog23-boop) · [LinkedIn](https://www.linkedin.com/in/vinícius-oliveira-1770b7306)

## Licença

Consulte [LICENSE](LICENSE).
