from pathlib import Path

input_file = Path("/data/input.txt")
output_file = Path("/data/result.txt")

print("SWE40006 Task 4.4 - File Statistics Tool")
print("Starting file processing...")

if not input_file.exists():
    print("ERROR: input.txt was not found.")
    raise SystemExit(1)

text = input_file.read_text(encoding="utf-8")

lines = len(text.splitlines())
words = len(text.split())
characters = len(text)

result = f"""File Statistics Report
======================
Lines: {lines}
Words: {words}
Characters: {characters}
"""

print(result)

output_file.write_text(result, encoding="utf-8")

print("Result saved successfully to /data/result.txt")
print("Processing complete.")