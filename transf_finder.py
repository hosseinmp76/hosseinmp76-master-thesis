import os
import re
from collections import defaultdict

# Get the current working directory
current_folder_path = os.getcwd()

# Regular expression pattern to match \transf{token1}{token2} allowing for whitespaces
pattern = re.compile(r'\\transf\s*\{\s*(.*?)\s*\}\s*\{\s*(.*?)\s*\}')

# Dictionary to store the categorized commands
categorized_commands = defaultdict(list)

# Function to find and add matches to the categorized dictionary
def add_transf_commands(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            matches = pattern.findall(contents)
            for token1, token2 in matches:
                if token1:  # Ensure there is a first token
                    first_char = token1[0].lower()  # Use lower case for consistency
                    categorized_commands[first_char].append((token1, token2))
    except IOError as e:
        print(f"Could not read file: {file_path} - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Recursively walk through the file system
for dirpath, dirnames, filenames in os.walk(current_folder_path):
    for filename in filenames:
        if filename.lower().endswith('.tex'):
            file_path = os.path.join(dirpath, filename)
            add_transf_commands(file_path)

# Sort each category by the first token
for first_char in categorized_commands:
    categorized_commands[first_char].sort(key=lambda x: x[0].lower())  # Sort ignoring case

# Now you can print the categorized and sorted results
for first_char, commands in sorted(categorized_commands.items()):
    print(f"\\dicalphabet{{{first_char}}}")
    for token1, token2 in commands:
        print(f'\\dicf{{{token1}}}{{{token2}}}')
