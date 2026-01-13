
# Automation & Python Intern – Practical Assignment

## Overview
This project is a small, safe, and structured automation system built using Python.  
The goal is to demonstrate **clear thinking, defensive programming, and real-world automation practices**, not complex features.

The script:
- Reads an input folder
- Validates required inputs
- Fails safely with clear messages if inputs are incorrect
- Generates a summary and log file when inputs are valid

---

## Folder Structure Used
```
media_system_automation/
│
├── input/
│ ├── data.txt
│ ├── notes.txt
│ └── images/
│   ├── img1.jpg
│   └── img2.png
│
├── output/
│ ├── summary.txt
│ └── run.log
│
├── automation.py
└── README.md
```

---

## How to Run the Program

### Prerequisites
- Python 3.8 or above

### Steps
1. Place required files inside the `input/` folder
2. Run the script:
	```bash
	python automation.py
	```

If successful, results will be created inside the `output/` folder.

## What the Program Does

### Validates Inputs
- Checks if `input/` folder exists
- Ensures at least one `.txt` file is present
- Ensures `images/` folder exists

### Handles Errors Safely
- Does not crash
- Displays clear error messages
- Logs failure reason
- Exits gracefully

### On Successful Validation
Counts:
- Number of text files
- Total lines across text files
- Total size of text files
- Number of images

Creates:
- `summary.txt` (human-readable output)
- `run.log` (timestamped execution log)

### Failure Behavior
| Scenario | Behavior |
|---|---|
| Input folder missing | Clear error + safe exit |
| No .txt files found | Error logged + safe exit |
| `images/` folder missing | Error logged + safe exit |
| Empty files | Logged as warning, not fatal |
| Unexpected runtime error | Logged + graceful exit |

The program never crashes abruptly.

## Design Decisions & Reasoning

- Simple folder-based automation mirrors real production pipelines
- Explicit validation rules avoid hidden failures
- Logging every major step ensures traceability
- Minimal dependencies keep the system portable and reliable
- Errors are treated as expected states, not exceptions

### One Edge Case Considered

Text files with invalid encoding

Files are read using:

```
errors="ignore"
```

Prevents crashes when encountering malformed or mixed encodings

### One Improvement for Scale

- Replace custom logging with Python’s `logging` module
- Add configurable validation rules via a JSON/YAML config
- Parallelize file processing for large datasets
- Add CLI arguments for dynamic input/output paths

### Example Successful Output

`output/summary.txt`:

```
Text files count: 2
Total text lines: 45
Total text size (bytes): 1832
Images count: 2
```

`output/run.log`:

```
[2026-01-13 11:52:01] Automation started
[2026-01-13 11:52:01] Input validation successful
[2026-01-13 11:52:01] Summary generated successfully
[2026-01-13 11:52:01] Automation completed
```

## Conclusion

This project prioritizes clarity, reliability, and safe automation practices.
It reflects how real-world automation systems are designed to handle unexpected input gracefully while remaining easy to maintain and extend.

---
