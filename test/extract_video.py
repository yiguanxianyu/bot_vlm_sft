import av

filename = r"C:\Users\yigua\Downloads\head_color.mp4"

av.logging.set_level(av.logging.VERBOSE)

with av.open(filename) as container:
    video_stream = container.streams.video[0]

    print(f"Stream index: {video_stream.index}")
    print(f"Type: {video_stream.type}")
    print(f"Codec: {video_stream.codec.name}")
    print(
        f"Resolution: {video_stream.codec_context.width}x{video_stream.codec_context.height}"
    )
    print(f"Frame rate: {video_stream.average_rate}")
    print(f"Duration (seconds): {(video_stream.duration * video_stream.time_base)}")
    print(f"Total frames: {video_stream.frames}")
    print(f"Time base: {video_stream.time_base}")

    # for index, frame in enumerate(container.decode(video=0)):
    #     frame.to_image()

    frames_to_extract = 30
    num_frames = video_stream.frames

    video_seconds = float(video_stream.time_base * video_stream.duration)
    sample_interval = av.time_base * video_seconds / (frames_to_extract - 1)

    for index in range(frames_to_extract):
        timestamp_us = int(index * sample_interval)
        container.seek(timestamp_us)
        frame = container.decode(video=0)
        image = next(iter(frame)).to_image()
        image.save(f"temp/frame-{index:04d}.jpg")
