import os
import sys
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "output"
LOG_FILE = "run.log"
SUMMARY_FILE = "summary.txt"


def log(message):
    """Write log with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(OUTPUT_DIR, LOG_FILE), "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def safe_exit(reason):
    """Exit safely with message"""
    print(f"ERROR: {reason}")
    log(f"FAILED: {reason}")
    sys.exit(1)


def validate_inputs():
    if not os.path.exists(INPUT_DIR):
        safe_exit("Input folder does not exist")

    files = os.listdir(INPUT_DIR)

    txt_files = [f for f in files if f.endswith(".txt")]
    images_path = os.path.join(INPUT_DIR, "images")

    if not txt_files:
        safe_exit("No .txt files found in input folder")

    if not os.path.exists(images_path):
        safe_exit("images folder is missing")

    return txt_files, images_path


def generate_summary(txt_files, images_path):
    total_lines = 0
    total_size = 0

    for file in txt_files:
        path = os.path.join(INPUT_DIR, file)
        size = os.path.getsize(path)
        total_size += size

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            total_lines += len(lines)

    image_count = len([p for p in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, p))])

    summary = [
        f"Text files count: {len(txt_files)}",
        f"Total text lines: {total_lines}",
        f"Total text size (bytes): {total_size}",
        f"Images count: {image_count}"
    ]

    return summary


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear old log
    open(os.path.join(OUTPUT_DIR, LOG_FILE), "w", encoding="utf-8").close()

    log("Automation started")

    txt_files, images_path = validate_inputs()
    log("Input validation successful")

    summary = generate_summary(txt_files, images_path)

    with open(os.path.join(OUTPUT_DIR, SUMMARY_FILE), "w", encoding="utf-8") as f:
        for line in summary:
            f.write(line + "\n")

    log("Summary generated successfully")
    log("Automation completed")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        safe_exit(str(e))
