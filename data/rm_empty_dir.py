import subprocess
from pathlib import Path

video_path = Path("/data1/AgiBotWorld-Beta-Output/observations")

for i in video_path.glob("*"):
    if i.is_dir() and not any(i.iterdir()):  # empty dir
        print(i, list(i.iterdir()))
        r = subprocess.run(f"du -sh {str(i)}", shell=True, capture_output=True, text=True)
        print(r.stdout)
        # subprocess.run(f"rm -rf {str(i)}", shell=True)
