import whisper
import openai
from downloader import baixar_tiktok_sem_marcadagua
from editor import editar_video
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcrever(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    os.makedirs("transcricoes", exist_ok=True)
    with open("transcricoes/texto.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    return result["text"]

def identificar_trecho(texto):
    prompt = f"""
Abaixo está a transcrição de um vídeo de comédia. Encontre o trecho mais engraçado (20 a 60 segundos) e responda:
início: XX.X
fim: YY.Y

Transcrição:
{texto}
"""
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    conteudo = resposta['choices'][0]['message']['content']
    try:
        inicio = float(conteudo.split("início:")[1].split("fim:")[0].strip())
        fim = float(conteudo.split("fim:")[1].strip())
        return inicio, fim
    except:
        raise ValueError("Não foi possível extrair tempos.")

def executar():
    os.makedirs("videos", exist_ok=True)
    os.makedirs("cortes", exist_ok=True)
    link_tiktok = "https://www.tiktok.com/@humorbrasil360/video/7357583665981644037"
    baixar_tiktok_sem_marcadagua(link_tiktok)
    texto = transcrever("videos/original.mp4")
    inicio, fim = identificar_trecho(texto)
    legenda = texto[int(inicio*2):int(fim*2)]
    editar_video("videos/original.mp4", inicio, fim, legenda)
