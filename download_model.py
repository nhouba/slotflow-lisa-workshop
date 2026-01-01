#!/usr/bin/env python3
"""
Download the pretrained SlotFlow model from GitHub releases.
"""

import os
import urllib.request
import sys

# GitHub release URLs
RELEASE_BASE = "https://github.com/nhouba/slotflow-inference/releases/download/v1.0.0"

MODEL_FILES = {
    "pretrained_model/test_clariden/model_config.pt": f"{RELEASE_BASE}/model_config.pt",
    "pretrained_model/test_clariden/checkpoints/best_model.ckpt": f"{RELEASE_BASE}/best_model.ckpt",
}

def download_file(url, dest_path):
    """Download a file with progress indicator."""
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    print(f"Downloading: {os.path.basename(dest_path)}")
    print(f"  From: {url}")
    print(f"  To: {dest_path}")

    try:
        urllib.request.urlretrieve(url, dest_path, reporthook=progress_hook)
        print("  Done!\n")
        return True
    except Exception as e:
        print(f"  Error: {e}\n")
        return False

def progress_hook(block_num, block_size, total_size):
    """Display download progress."""
    if total_size > 0:
        percent = min(100, block_num * block_size * 100 // total_size)
        bar = '=' * (percent // 2) + '-' * (50 - percent // 2)
        sys.stdout.write(f"\r  [{bar}] {percent}%")
        sys.stdout.flush()
        if percent >= 100:
            print()

def main():
    print("=" * 60)
    print("SlotFlow Pretrained Model Downloader")
    print("=" * 60)
    print()

    # Check if model already exists
    all_exist = all(os.path.exists(path) for path in MODEL_FILES.keys())
    if all_exist:
        print("Pretrained model already exists!")
        response = input("Re-download? [y/N]: ").strip().lower()
        if response != 'y':
            print("Skipping download.")
            return

    print("Downloading pretrained model files...\n")

    success = True
    for dest_path, url in MODEL_FILES.items():
        if not download_file(url, dest_path):
            success = False

    if success:
        print("=" * 60)
        print("Download complete!")
        print("You can now run the tutorials in notebooks/")
        print("=" * 60)
    else:
        print("=" * 60)
        print("Some downloads failed.")
        print("Please download manually from:")
        print("  https://github.com/nhouba/slotflow-inference/releases/tag/v1.0.0")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
