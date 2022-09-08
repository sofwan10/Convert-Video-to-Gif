from moviepy.editor import VideoFileClip
clip = VideoFileClip("merdeka.mp4")
clip.write_gif("Output.gif",fps=20)