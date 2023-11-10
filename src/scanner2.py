import os
import re

def find_keyword_in_files(folder_path, keyword, context_regex, lines_before=5, lines_after=5):
    result_list = []

    # Iterate through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is a text file (you may adjust this condition)
            if file_path.endswith(".txt") or file_path.endswith(".py"):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()

                pattern = re.compile(context_regex)

                for i, line in enumerate(lines, start=1):
                    match = re.search(pattern, line)
                    if match and keyword in line:
                        start = max(1, i - lines_before)
                        end = min(len(lines), i + lines_after + 1)
                        context = lines[start-1:end]
                        result_list.append({
                            'file_path': file_path,
                            'keyword': keyword,
                            'line_number': i,
                            'context': context
                        })

    return result_list

if __name__ == "__main__":
    folder_path = "your_folder_path"
    keyword = "your_keyword"
    context_regex = r"your_regex_pattern"

    results = find_keyword_in_files(folder_path, keyword, context_regex)

    if results:
        for result in results:
            print(f"File: {result['file_path']}")
            print(f"Keyword: {result['keyword']} | Line Number: {result['line_number']}")
            print("Context:")
            for i, line in enumerate(result['context'], start=result['line_number'] - len(result['context']) + 1):
                print(f"{i}: {line.strip()}")
            print("\n" + "=" * 50 + "\n")
    else:
        print(f"No matches found for '{keyword}' in the specified folder with the given regex context.")
