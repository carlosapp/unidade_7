
# unidade_7
# Transcrição de Áudio e Resumo com Inteligência Artificial

O sistema utiliza:

- **Whisper:** realiza a transcrição do áudio para texto.
- **Ollama:** utiliza o modelo `llama3.2:latest` para gerar um resumo e destacar os principais pontos do conteúdo.

Todo o resultado é exibido diretamente no terminal, sem gerar arquivos adicionais.

## Estrutura do Projeto

```text
unidade_7/
├── main.py
├── teste-whisper.mp3
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3 instalado.
- Ollama instalado.
- Modelo `llama3.2:latest` disponível no Ollama.
- FFmpeg instalado.

## Instalação

### 1. Instalar as dependências

Com o terminal aberto na pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

### 2. Instalar o FFmpeg

O Whisper utiliza o FFmpeg para processar arquivos de áudio.

No Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

No Windows, instale o FFmpeg e adicione a pasta `bin` à variável de ambiente `PATH`.

### 3. Preparar o Ollama

Certifique-se de que o Ollama esteja em execução e que o modelo esteja disponível:

```bash
ollama pull llama3.2
```

Caso o Ollama não esteja iniciado automaticamente, execute:

```bash
ollama serve
```

## Execução

Coloque o arquivo de áudio na pasta raiz do projeto com o nome:

```text
teste-whisper.mp3
```

Em seguida, execute:

```bash
python main.py
```

## Funcionamento

O processamento ocorre em duas etapas:

1. **Transcrição:** o Whisper analisa o áudio e converte a fala em texto, considerando o idioma português.
2. **Resumo:** o Ollama recebe o texto transcrito e utiliza inteligência artificial para elaborar um resumo com os principais pontos-chave.

## Resultado Esperado

O terminal apresenta:

- A transcrição completa do áudio.
- O resumo do conteúdo.
- Os principais pontos-chave organizados em tópicos.
- Uma mensagem indicando a conclusão do processamento.

## Tecnologias Utilizadas

- Python
- OpenAI Whisper
- Ollama
- Modelo Llama 3.2
- Biblioteca Requests
