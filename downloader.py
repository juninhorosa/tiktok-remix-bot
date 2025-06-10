import requests

def baixar_tiktok_sem_marcadagua(url):
    print("⬇️ Baixando vídeo do TikTok...")
    api = "https://tikwm.com/api/"
    res = requests.post(api, data={"url": url})
    data = res.json()

    if data.get("data", {}).get("play"):
        video_url = data["data"]["play"]
        video_data = requests.get(video_url).content
        with open("videos/original.mp4", "wb") as f:
            f.write(video_data)
        print("✅ Vídeo baixado com sucesso!")
    else:
        print("❌ Erro ao baixar vídeo.")
