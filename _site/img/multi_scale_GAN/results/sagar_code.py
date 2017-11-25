import moviepy.editor as mpy
def reduce_fps(filename, new_fps):
    fast_clip = mpy.VideoFileClip(filename)
    duration = fast_clip.duration
    old_fps = fast_clip.fps
    new_duration = (duration * old_fps) / (1.0 * new_fps)
    new_clip = fast_clip.set_fps(new_fps)
    new_clip = new_clip.set_duration(new_duration)
    new_clip.write_gif(filename)
    
output_video_save_file_path = ''
for root, _ , files in os.walk(output_video_save_file_path):
    for file_name in files:
        file_name = os.path.join(root, file_name)
        reduce_fps(file_name, 10)
