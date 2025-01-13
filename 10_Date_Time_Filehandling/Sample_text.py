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

file_path =r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\data\mytext.txt'  # Ensure the file path is correct
n = 10
print(find_most_common_words(file_path, n))
file_path =r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\data\mytext.txt'  # Ensure the file path is correct
n = 5
print(find_most_common_words(file_path, n))