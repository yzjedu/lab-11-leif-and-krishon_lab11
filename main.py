

# Import os package into the code
import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_conversion_file():
    f_name = input("Enter name of conversion file: ").lower().strip()
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

def read_conver_file_into_dictionary(file_name):
    morse_dictionary = {}
    try:
        file = open(file_name, "r")
        for line in file:
            items = line.split('  ')
            key = items[1]
            value = items[0]
            morse_dictionary[key] = value
        print(morse_dictionary)
        return morse_dictionary
    except:
        if file_name != "morsecode.txt":
            print("File is not a conversion file. Please try again.")
        return

def convert_morse(morse_dict):
    passthru = False
    while not passthru:
        passthru2 = False
        while not passthru2:
            file_name = input('\nEnter file to convert: ').lower()
            if file_name == 'morse1.txt' or file_name == 'morse2.txt' or file_name == 'morse3.txt':
                passthru2 = True
            else:
                print("Invalid file selection. try again")
        file_data = open(file_name, 'r')
        all_conversions = []
        for line in file_data:
            characters = line.split()
            conversion = []
            for character in characters:
                character = character + '\n'
                to_append = morse_dict[character]
                conversion.append(to_append)
            all_conversions.append(conversion)
        file_data.close()
        new_file = input('Enter name of new file, EXCLUDE SUFFIX: ').lower()
        file_writing = open(f'{new_file}.txt', 'w')
        for word in all_conversions:
            for character in word:
                file_writing.write(character)
            file_writing.write('\n')
        file_writing.close()
        print('Conversion complete.')
        while passthru2:
            continue_query = input('\nConvert another file? Express answer as Y or N: ').lower()
            if continue_query == 'y':
                print('Resetting...')
                passthru2 = False
            elif continue_query == 'n':
                print('Thank you for using our converter')
                passthru2 = False
                passthru = True
            else:
                print('Invalid input. Express answer as Y or N')

def main():
    file_name = read_conversion_file()
    morse_dict = read_conver_file_into_dictionary(file_name)
    convert_morse(morse_dict)

main()