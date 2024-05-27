import re
import os

def strip_commands(text):
    text = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', text)  # Removes commands like \command{arg}
    text = re.sub(r'\\[a-zA-Z]+\[.*?\]', '', text)  # Removes commands like \command[arg]
    text = re.sub(r'\\[a-zA-Z]+\*?\b', '', text)    # Removes commands like \command or \command*
    text = re.sub(r'\\[a-zA-Z]+\d?', '', text)      # Removes commands like \command1
    return text

def extract_content(text):
    commands_to_extract = ['chapter', 'section', 'subsection', 'subsubsection']
    for command in commands_to_extract:
        text = re.sub(r'\\' + command + r'\{(.*?)\}', r'\1', text)
    return text

def strip_captions(text):
    """
    Remove LaTeX captions from the text.
    """
    # Pattern to remove \caption{} commands
    text = re.sub(r'\\caption\{.*?\}', '', text, flags=re.DOTALL)
    return text

def strip_comments(text):
    """
    Remove LaTeX comments from the text.
    """
    # Pattern to remove comments
    text = re.sub(r'%.*', '', text)
    return text

def characters_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    text = strip_comments(text)
    text = strip_captions(text)
    text = extract_content(text)
    text = strip_commands(text)
    # Replace \\ with \n and \n with a space
    text = text.replace('\\\\', '\n').replace('\n', ' ')
    text = re.sub(r'\n(?!\n)', '', text)
    return text

def count_characters(file_path):
    text = characters_in_file(file_path)    
    # Count characters
    char_count = len(text)
    return char_count

def count_characters_with_no_whitespaces(file_path):
    text = characters_in_file(file_path) 
    text = re.sub(r'\s', '', text)
    char_count = len(text)
    return char_count


if __name__ == "__main__":
    folder_path = 'files'
    print(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.tex')]
    total_char_count = 0

    for file_path in file_paths:
        char_count = count_characters(file_path)
        print(f"Total characters in {file_path} (excluding captions and commands): {char_count}")
        total_char_count += char_count


    print(f"Total characters in all files: {total_char_count}")


    total_char_count = 0
    for file_path in file_paths:
        char_count = count_characters_with_no_whitespaces(file_path)
        print(f"Total characters in {file_path} (excluding captions and commands), without whitespaces: {char_count}")
        total_char_count += char_count

    print(f"Total characters in all files: {total_char_count}... without whitespaces.")
