import subprocess
from pathlib import Path

from all_files import missing_data

sft_data_path = Path("/mnt/nvme/sft_data/observations")
not_fully_downloaded = set()

for i in missing_data:
    task, file_name = i.split("/")[1:3]
    not_fully_downloaded.add(task)

for i in sft_data_path.glob("*"):
    if not i.is_dir():
        continue

    num_of_episodes = len(list(i.iterdir()))
    if num_of_episodes != 10:
        print(i, num_of_episodes)
        subprocess.run(["rm", "-rf", i])
