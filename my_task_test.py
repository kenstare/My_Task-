from pathlib import Path

participant_pkg = Path("participant_pkg")
participant_pkg.mkdir(exist_ok=True)
file_path1 = participant_pkg / "__init__.py"
file_path2 = participant_pkg / "file_ops.py"
file_path3 = participant_pkg / "main.py"
file_path4 = participant_pkg / "contact.py"
f = open(file_path1, "w", encoding="utf-8")
f.close()

f = open(file_path2, "w", encoding="utf-8")
f.close()

f = open(file_path3, "w", encoding="utf-8")
f.close()

f = open(file_path4, "w", encoding="utf-8")
f.close()
print("All files created successfully.")

