import os
import whisper
import requests


class Main:

    def __init__(self):
        self.arquivo_audio = "teste-whisper.mp3"
        self.modelo_whisper = whisper.load_model("base")
        self.modelo_ollama = "llama3.2:latest"
        self.api_ollama = "http://localhost:11434/api/generate"

    def transcrever_audio(self):
        print("\n[1/2] Transcrevendo áudio com Whisper...\n")

        resultado = self.modelo_whisper.transcribe(
            self.arquivo_audio,
            language="pt",
            fp16=False
        )

        return resultado["text"]

    def gerar_resumo(self, texto):
        print("\n[2/2] Extraindo pontos-chave com Ollama...\n")

        prompt = f"""
Analise o texto abaixo e produza um resumo em português.

Destaque os principais pontos-chave utilizando tópicos
objetivos e organizados.

Texto:
{texto}
"""

        resposta = requests.post(
            self.api_ollama,
            json={
                "model": self.modelo_ollama,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        resposta.raise_for_status()

        return resposta.json()["response"]

    def executar(self):
        print("=" * 50)
        print("       TRANSCRICAO DE AUDIO COM IA")
        print("=" * 50)

        if not os.path.isfile(self.arquivo_audio):
            print(
                f"\nErro: arquivo {self.arquivo_audio} não encontrado."
            )
            return

        try:
            # Etapa 1: Transcrição do áudio
            transcricao = self.transcrever_audio()

            print("\n" + "=" * 50)
            print("TRANSCRICAO DO AUDIO")
            print("=" * 50)
            print(transcricao)

            # Etapa 2: Resumo e extração dos pontos-chave
            resumo = self.gerar_resumo(transcricao)

            print("\n" + "=" * 50)
            print("RESUMO E PONTOS-CHAVE")
            print("=" * 50)
            print(resumo)

            print("\n" + "=" * 50)
            print("PROCESSAMENTO CONCLUIDO!")
            print("=" * 50)

        except requests.exceptions.RequestException as erro:
            print(f"\nErro ao conectar com o Ollama: {erro}")

        except Exception as erro:
            print(f"\nErro durante o processamento: {erro}")


if __name__ == "__main__":
    aplicacao = Main()
    aplicacao.executar()
