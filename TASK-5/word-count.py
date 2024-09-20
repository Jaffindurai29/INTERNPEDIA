import string
def count_words(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    
    words = clean_text.split()
    
    return len(words)

def get_text_from_user():
    print("\nEnter your text (or type 'done' to stop input):")
    lines = []
    while True:
        line = input("> ")
        if line.lower() == 'done':
            break
        lines.append(line)
    return ' '.join(lines)

def get_text_from_file():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def prompt_user_for_input_method():
    while True:
        choice = input("\nDo you want to input text manually or from a file? (manual/file): ").lower()
        if choice in ['manual', 'file']:
            return choice
        else:
            print("Invalid choice. Please enter 'manual' or 'file'.")

def word_counter():
    print("Welcome to the Word Counting Program!")
    
    while True:
        input_method = prompt_user_for_input_method()
        
        if input_method == 'manual':
            text = get_text_from_user()
        else:
            text = get_text_from_file()
            if text is None:
                continue 
        
        if not text.strip():
            print("Error: No text provided.")
            continue
        
        word_count = count_words(text)
        print(f"\nThe text contains {word_count} words.")
        
        another_text = input("\nDo you want to count words in another text? (y/n): ").lower()
        if another_text != 'y':
            print("Thank you for using the Word Counting Program!")
            break

if __name__ == "__main__":
    word_counter()
