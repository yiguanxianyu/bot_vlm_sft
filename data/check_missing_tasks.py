import os
import subprocess
from pathlib import Path

from all_files import files

video_path = Path("/mnt/nvme/sft_data/observations")

missing_tasks = set()

for i in files:
    if not (i.startswith("observations") and i.endswith(".tar")):
        continue
    task, file_name = i.split("/")[1:3]
    path = video_path / task
    if not path.exists():
        missing_tasks.add(task)

print(sorted(list(missing_tasks)), len(missing_tasks))
