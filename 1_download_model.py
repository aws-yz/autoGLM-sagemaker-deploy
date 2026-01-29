#!/usr/bin/env python3
"""下载 AutoGLM-Phone-9B 模型到本地"""
import os
import json
from huggingface_hub import snapshot_download
from datetime import datetime

MODELS = {
    "1": ("zai-org/AutoGLM-Phone-9B", "中文版 - 针对中文手机应用优化"),
    "2": ("zai-org/AutoGLM-Phone-9B-Multilingual", "多语言版 - 支持英文等多语言场景"),
}
LOCAL_DIR = "model"

def main():
    print("请选择要下载的模型:")
    for k, (mid, desc) in MODELS.items():
        print(f"  {k}. {desc}\n     {mid}")
    print("  3. 退出")
    
    choice = input("\n请输入选项 (1/2/3): ").strip()
    if choice == "3":
        print("已退出")
        return
    if choice not in MODELS:
        print("无效选项")
        return
    
    model_id, desc = MODELS[choice]
    print(f"\n下载模型: {model_id}")
    print(f"目标目录: {LOCAL_DIR}")
    
    snapshot_download(
        repo_id=model_id,
        local_dir=LOCAL_DIR,
        local_dir_use_symlinks=False
    )
    
    # 计算大小
    total_size = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, files in os.walk(LOCAL_DIR)
        for f in files
    )
    
    info = {
        "status": "completed",
        "model_id": model_id,
        "model_size_gb": total_size / 1024**3,
        "download_time": datetime.now().isoformat()
    }
    
    with open("model_download_info.json", "w") as f:
        json.dump(info, f, indent=2)
    
    print(f"\n✅ 下载完成: {info['model_size_gb']:.1f} GB")

if __name__ == "__main__":
    main()
