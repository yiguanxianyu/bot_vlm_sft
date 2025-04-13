"""
Extract all skills from all task_info files.
"""

import json
from pathlib import Path

task_info_home = Path("/mnt/nvme/sft_data/task_info")

skills = set()

for task_info_file in task_info_home.rglob("task_*.json"):
    with open(task_info_file, "r") as f:
        data = json.load(f)

    for episode in data:
        for action in episode["label_info"]["action_config"]:
            skill = action["skill"]
            skills.add(skill)

print(sorted(list(skills)))
