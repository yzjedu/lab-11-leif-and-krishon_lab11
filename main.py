

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

# Purpose:  Creates conversion dictionary
# Parameters: file_name
# Return: the completed conversion dictionary
def read_conver_file_into_dictionary(file_name):
    # creates empty dictionary to mold later
    morse_dictionary = {}
    try:
        # opens conversion file from read_conversion_file
        file = open(file_name, "r")
        for line in file:
            # splits each line into its morse and latin characters
            items = line.split('  ')
            # sets morse character as key
            key = items[1]
            # sets latin character as value
            value = items[0]
            # assigns key and value to dictionary
            morse_dictionary[key] = value
        # prints dictionary to user
        print(morse_dictionary)
        return morse_dictionary
    except:
        # if the file name is not the assigned conversion file, it spits an error messages and retries
        if file_name != "morsecode.txt":
            print("File is not a conversion file. Please try again.")
        return

# Purpose:  Runs conversion on given document and creates new document
# Parameters: morse_dict
# Return: the completed conversion file
def convert_morse(morse_dict):
    # assigns passthru value for retry query
    passthru = False
    while not passthru:
        # assigns passthru2 value for error checking
        passthru2 = False
        while not passthru2:
            # requests user input file name
            file_name = input('\nEnter file to convert: ').lower()
            # if the given file is not one of the 3 presented, it provides an error message
            if file_name == 'morse1.txt' or file_name == 'morse2.txt' or file_name == 'morse3.txt':
                passthru2 = True
            else:
                print("Invalid file selection. try again")
        # opens file as directed by user
        file_data = open(file_name, 'r')
        # creates empty list to contain all conversions
        all_conversions = []
        for line in file_data:
            # splits each line (word) into individual characters
            characters = line.split()
            # creates empty list for every new word
            conversion = []
            for character in characters:
                character = character + '\n'
                # sets given character as the morse_dict key to look up
                to_append = morse_dict[character]
                # appends converted character to its given word list
                conversion.append(to_append)
            # converts completed word to full conversion list
            all_conversions.append(conversion)
        file_data.close()
        # requests user input name to give to converted file
        new_file = input('Enter name of new file, EXCLUDE SUFFIX: ').lower()
        file_writing = open(f'{new_file}.txt', 'w')
        for word in all_conversions:
            for character in word:
                # writes each character in a word onto a line
                file_writing.write(character)
            # separates words per line
            file_writing.write('\n')
        file_writing.close()
        print('Conversion complete.')
        while passthru2:
            # requests whether or not the user would like to convert another file
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

# Purpose:  Runs main function
# Parameters: none
# Return: the completed conversion file
def main():
    file_name = read_conversion_file()
    morse_dict = read_conver_file_into_dictionary(file_name)
    convert_morse(morse_dict)

main()