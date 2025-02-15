def main():
    path_to_file = 'books/frankenstein.txt'

    file_contents = read_file(path_to_file)

    word_count = count_words(file_contents)
    characters = create_characters_dict(file_contents)

    print_report(path_to_file, word_count, characters)

    
def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def count_words(file_contents):
    return len(file_contents.split())


def create_characters_dict(file_contents):
    characters = {}

    for i in range (0, len(file_contents)):
        character = file_contents[i].lower()

        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1

    return characters  

            
def print_report(file_path, word_count, characters):
    print(f'--- Begin report of {file_path} ---')
    print(f'{word_count} words found in the document')
    print('')

    for key in characters:
        if key.isalpha():
            print(f"The '{key}' character was found {characters[key]} times")

    print('--- End report ---')


main()