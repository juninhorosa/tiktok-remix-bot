import moviepy.editor as mp
import os

def cortar_video(input_path, inicio, fim):
    clip = mp.VideoFileClip(input_path).subclip(inicio, fim)
    clip = clip.resize(height=1920)  # 9:16 formato vertical
    clip = clip.set_position("center")
    output_path = f"cortes/corte_{int(inicio)}s_{int(fim)}s.mp4"
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
