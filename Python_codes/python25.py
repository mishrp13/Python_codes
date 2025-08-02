
## #Count word frequency in a file..


def count_word_frequency(file_path):
    word_count = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().strip('.,!?";:()[]{}')  # Normalize the word
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    
    return word_count