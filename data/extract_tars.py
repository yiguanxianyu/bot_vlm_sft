import subprocess
from pathlib import Path

tars_path = Path("/mnt/nvme/agi_add/observations")
agi_beta_path = Path("/mnt/nvme/AgiBotWorldBeta/observations")
trash_path = Path("/mnt/nvme/AgiBotWorldBeta/trash")

# template
# tar -xvf 760308-760375.tar --wildcards '*/hand_left_color.mp4' '*/hand_right_color.mp4' '*/head_color.mp4'

for i in tars_path.glob("*.tar"):
    begin, end = i.name[:-4].split("-")
    task = i.parent.name
    output_path = agi_beta_path / task
    output_path.mkdir(parents=True, exist_ok=True)

    obs_1 = output_path / begin
    obs_2 = output_path / end
    if not (obs_1.exists() and obs_2.exists()):
        print(i)
        subprocess.run(
            [
                "tar",
                "-xf",
                i,
                "-C",
                output_path,
                "--wildcards",
                "*/hand_left_color.mp4",
                "*/hand_right_color.mp4",
                "*/head_color.mp4",
            ]
        )
