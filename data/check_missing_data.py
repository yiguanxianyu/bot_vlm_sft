import os
import subprocess
from pathlib import Path

from all_files import files

video_path = Path("/data1/AgiBotWorld-Beta-Output/observations")

missing_data = []

for i in files:
    if not (i.startswith("observations") and i.endswith(".tar")):
        continue
    task, file_name = i.split("/")[1:3]
    begin, end = file_name[:-4].split("-")

    obs_1 = video_path / task / begin
    obs_2 = video_path / task / end
    if not obs_1.exists() or not obs_2.exists():
        missing_data.append(i)

print(missing_data)
