import subprocess
from pathlib import Path

sft_data_path = Path("/data1/zc_data/sft_data/observations")
tar_path = Path("/data1/zc_data/sft_data/tars")

for i in sft_data_path.glob("*"):
    tar_name = tar_path / (i.name + ".tar")
    if tar_name.exists():
        continue
    print(tar_name)
    subprocess.run(["tar", "-cvf", tar_name, i.name], cwd=sft_data_path)
