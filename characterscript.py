import re
import os

def strip_commands(text):
    """
    Remove LaTeX commands from the text, excluding chapter, section, and subsection.
    """
    # Pattern to remove LaTeX commands
    commands_to_exclude = ['chapter', 'section', 'subsection']
    command_pattern = r'\\(?!' + '|'.join(commands_to_exclude) + r')[a-zA-Z]+\{.*?\}'
    text = re.sub(command_pattern, '', text)  # Removes commands like \command{arg}
    text = re.sub(r'\\[a-zA-Z]+\[.*?\]', '', text)  # Removes commands like \command[arg]
    text = re.sub(r'\\[a-zA-Z]+\*?\b', '', text)    # Removes commands like \command or \command*
    text = re.sub(r'\\[a-zA-Z]+\d?', '', text)      # Removes commands like \command1
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

def count_characters(file_path):
    """
    Count characters in a .tex file excluding captions and commands.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    text = strip_comments(text)
    text = strip_captions(text)
    text = strip_commands(text)
    
    # Count characters
    char_count = len(text)
    
    return char_count

if __name__ == "__main__":
    folder_path = 'C:\\Users\\Lukas\\source\\repos\\latexcharactercounterscript\\files'
    print(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.tex')]
    total_char_count = 0

    for file_path in file_paths:
        char_count = count_characters(file_path)
        print(f"Total characters in {file_path} (excluding captions and commands): {char_count}")
        total_char_count += char_count

    print(f"Total characters in all files: {total_char_count}")