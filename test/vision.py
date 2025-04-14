from torchvision import io, transforms

video_path = (
    r"file://C:\Users\yigua\Downloads\Bon Iver - Everything Is Peaceful Love (Official Video)-1.mp4"
)

video, audio, info = io.read_video(
    video_path,
    start_pts=0.0,
    end_pts=None,
    pts_unit="sec",
    output_format="TCHW",
)

print(video.shape)
print(info)
