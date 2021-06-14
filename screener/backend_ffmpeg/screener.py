import ffmpeg
# """
# (
#     ffmpeg
#     .input('1', format='avfoundation', pix_fmt='uyvy422', framerate=30)
#     .output('out.mkv', pix_fmt='yuv420p', vframes=1000)
#     .run()
# )
# """

# video_format = "flv"
# server_url = "http://0.0.0.0:8080"

# process = (
#     ffmpeg.input('out.mkv').output(
#         server_url,
#         codec="copy",  # use same codecs of the original video
#         listen=1,  # enables HTTP server
#         f=video_format).global_args("-re")  # argument to act as a live stream
#     .run())
