

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

def read_file():
    morse_name = input("Enter name of conversion file: ").lower().strip()
    while not os.path.isfile(morse_name):
        morse_name = input("File not exist. Enter file name: ")
    return morse_name

def convert_morse(key,morse_dict):
    new_file = read_file()
    for line in new_file:
        if key in morse_dict:
            print(line)





def main():
    file_name = read_conversion_file()
    morse_dict = read_conver_file_into_dictionary(file_name)


main()