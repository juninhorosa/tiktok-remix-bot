from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, vfx

def editar_video(input_path, inicio, fim, legenda_texto):
    print("🎬 Editando vídeo...")
    clip = VideoFileClip(input_path).subclip(inicio, fim)
    clip = clip.fx(vfx.crop, width=clip.w * 0.9, height=clip.h * 0.9, x_center=clip.w / 2, y_center=clip.h / 2)
    clip = clip.fx(vfx.resize, height=1920)

    legenda = TextClip(legenda_texto, fontsize=70, color='white', font='Arial-Bold', method='caption', size=(clip.w - 100, None))
    legenda = legenda.set_duration(clip.duration).set_position(('center', 'bottom'))

    final = CompositeVideoClip([clip.set_position("center"), legenda])
    final.write_videofile("cortes/remix_final.mp4", codec="libx264", audio_codec="aac")
    print("✅ Edição concluída.")
