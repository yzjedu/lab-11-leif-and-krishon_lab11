# Algorithm Document

* Purpose:  reads the morse code and puts it into a dictionary
* Name: make_dictionary
* Parameters: filename (morsecode.txt in most cases)
* Return: the completed dictionary for conversions
* Algorithm:
1. Open the given file to be read and set its data equal to a variable like "morse_data"
2. Create an empty dictionary with a name like "morse_dict"
3. For each line in the aforementioned "morse_data":
    1. Append the conversion to "morse_dict", the morse code as the key and the latin letter as the value
4. Close the given file
5. Return the completed dictionary "morse_dict"

* Purpose:  converts a given morse file into latin lettering via "morse_dict"
* Name: convert_morse
* Parameters: filename (morse1.txt, morse2.txt, or morse3.txt)
* Return: converted text represented in list form
* Algorithm:
1. Define an empty list with a name like "morse_text"
2. Define another empty list with a name like "latin_text"
3. Open the given file to be read and set its data equal to "morse_text"
4. For each line in "morse_text":
    1. Convert each morse letter into its corresponding latin letter via "morse_dict"
   2. Append the conversion to "latin_text"
5. Close the given file
6. Return the completed list "latin_text"

* Purpose:  writes each converted line to a new file with a name chosen by the user
* Name: imprint_latin
* Parameters: filename
* Return: the completed file
* Algorithm:
1. Create a new .txt file with the filename selected by the user
2. Open the new file to be written
3. For each line in list "latin_text":
    1. Write the line into the new .txt file
4. Close the new .txt file
5. Return the new file and/or output a completion message

* Purpose:  contains the main function
* Name: main
* Parameters: nilch
* Return: completed file
* Algorithm:
1. Output a welcome statement to the user
2. Create an error checking loop
3. While the error checking has not been passed:
    1. Request the user input the name of the file they wish to convert
4. While error checking has not been passed:
    1. Request the user input the name they wish to give their new converted file
5. run function make_dictionary with parameter '
6. run function convert_morse with the first input file name as a parameter
7. run function imprint_latin with the second input file name as a parameter
8. Prompt the user with a choice to convert another file
9. if the user responds "yes"
    1. Restart the program
10. otherwise if the user responds "no"
    1. print an exit message and exit the program