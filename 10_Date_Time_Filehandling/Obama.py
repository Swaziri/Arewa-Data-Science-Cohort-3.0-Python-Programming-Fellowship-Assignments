
file_path = r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\data\obama_speech.txt'
def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        return num_lines, num_words
    except FileNotFoundError:
        return "File not found!", None
result = count_lines_and_words(file_path)
if result[1] is not None:
    print(f"The file contains Obama Speech:")
    print(f"Number of lines: {result[0]}")
    print(f"Number of words: {result[1]}")
else:
    print(result[0])

import re
from collections import Counter
def find_most_common_words(file_path, n):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Normalize and tokenize the text
        words = re.findall(r'\b\w+\b', text.lower())  # Extract words, converting to lowercase

        # Count word frequencies
        word_counts = Counter(words)

        # Get the n most common words
        most_common = word_counts.most_common(n)

        return most_common

    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."

    except Exception as e:
        return f"An error occurred: {e}"
file_path = r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\data\obama_speech.txt'
n = 10
print(find_most_common_words(file_path, n))