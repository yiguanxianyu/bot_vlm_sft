import av
filename = "/mnt/nvme/sft_data/observations/327/649755/videos/head_color.mp4"

av.logging.set_level(av.logging.VERBOSE)
container = av.open(filename)

for index, frame in enumerate(container.decode(video=0)):
    frame.to_image().save(f"temp/frame-{index:04d}.jpg")