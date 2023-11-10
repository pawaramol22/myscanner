import csv
import os

start_directory = "/Users/amol/Documents/GitHub/algorithms/src"
keywords = ["int", "Array"]
context_lines = 5
matches = []

csv_path = "/Users/amol/Documents/scan_results.csv"

for root, dirs, files in os.walk(start_directory):
    for file in files:
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, start=1):
                    for keyword in keywords:
                        if keyword in line:
                            start = max(0, line_num - context_lines)
                            end = min(len(lines), line_num + context_lines + 1)
                            context = lines[start:end]
                            matches.append((filepath, line_num, context))
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

for match in matches:
    print(f"{match[0]}, Line Number: {match[1]}, Context: {match[2]}")
    #for line in match[2]:
    #    print(line.strip())
    print()

header = ["File", "Line Number", "Match Context"]

with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)

    for match in matches:
        csv_writer.writerow([match[0], match[1], match[2]])