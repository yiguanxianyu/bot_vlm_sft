import os
import subprocess
from pathlib import Path

from all_files import missing_data

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_TOKEN"] = ""

from huggingface_hub import hf_hub_download

for file in missing_data:
    hf_hub_download(
        repo_id="agibot-world/AgiBotWorld-Beta",
        filename=file,
        repo_type="dataset",  # 数据集类型必须设置为 "dataset"
        token=os.environ["HF_TOKEN"],
    endpoint="https://hf-mirror.com",  # 设置镜像端点
    local_dir="/data1/",
)
