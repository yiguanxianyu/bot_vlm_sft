import json
import os
import random
import subprocess
from pathlib import Path

from all_files import missing_data

not_fully_downloaded = set()

for i in missing_data:
    task, file_name = i.split("/")[1:3]
    not_fully_downloaded.add(task)

data_path = Path("/data1/AgiBotWorld-Beta-Output/observations")
dest_path = Path("/data1/zc_data/sft_data/observations")

dest_path.mkdir(parents=True, exist_ok=True)

for srcdir in data_path.iterdir():
    if not srcdir.is_dir():
        continue
    dest_dir = dest_path / srcdir.name
    dest_dir_subdirs = list(dest_dir.iterdir()) if dest_dir.exists() else []
    srcdir_subdirs = list(srcdir.iterdir())

    num_episodes_already_there = len(dest_dir_subdirs)
    num_episodes_downloaded = len(srcdir_subdirs)

    if num_episodes_already_there > 10:
        print("Exceeds 10 episodes", srcdir.name, num_episodes_already_there)
        continue
    elif num_episodes_already_there == 10:
        continue

    if num_episodes_downloaded >= 10:
        choices = random.sample(srcdir_subdirs, k=10)
        dest_dir.mkdir(parents=True, exist_ok=True)
        # print(dest_dir, len(choices), choices[0])
        subprocess.run(
            ["rsync", "-am", "--include='head_color.mp4'", *choices, dest_dir],
            check=True,
        )
