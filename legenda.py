from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def adicionar_legenda(video_path, legenda_texto):
    clip = VideoFileClip(video_path)
    txt = TextClip(legenda_texto, fontsize=60, color='white', font='Arial-Bold')
    txt = txt.set_position(('center', 'bottom')).set_duration(clip.duration)
    video = CompositeVideoClip([clip, txt])
    legenda_path = video_path.replace(".mp4", "_legendado.mp4")
    video.write_videofile(legenda_path, codec="libx264", audio_codec="aac")
    print("Vídeo com legenda salvo em:", legenda_path)
