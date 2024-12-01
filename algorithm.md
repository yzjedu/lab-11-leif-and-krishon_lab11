# Algorithm Document

* Import os package into program 


* Purpose: Processes user's file input and output's if user's input is invalid
* Name: read_conversion_file 
* Parameters: [NONE]
* Return: f_name
* Algorithm:
  1. Collect user input, assigns it to variable f_name, and strip and lower variable.
  2. While file name is not in program
  3. Ask user to re-input file name 

 
* Purpose: Reads the morse code and puts it into a dictionary
* Name: read_conver_file_into_dictionary
* Parameters: file_name
* Return: morse_dictionary; the completed dictionary for conversions
* Algorithm:
  1. Try to run:
     1. Create an empty dictionary and assign it to variable
     2. Open conversion file from read_conversion_file with reading permissions
     3. For each line in conversion file
     4. Split lines by tab and assign to variable
     5. Set morse character to variable "key"
     6. Set latin character to variable "value"
     7. Assign keys and values to dictionary
     8. Output dictionary
     3. For each line in the aforementioned "morse_data":
        1. Append the conversion to "morse_dict", the morse code as the key and the latin letter as the value
     4. Close the given file
     5. Return the completed dictionary "morse_dict"
  2. Except:
     1. While file name is not the conversion file:
        * Output an error messages and re-collects user's input


* Purpose: Converts a given morse file into latin lettering via "morse_dict"
* Name: convert_morse
* Parameters: morse_dict; morse dictionary
* Return: [NONE]
* Algorithm:
  1. Assign variable 'passthru' to value FALSE
  2. While not passthru:
     1. Assign variable 'passthru2' to value FALSE
     2. While not passthru2:
        1. Collect user input and assign it to variable
        2. If file name is equal to "morse1.txt" or "morse2.txt" or "morse3.txt":
           1. Assign variable 'passthru2' to value TRUE
        3. Otherwise:
           1. Output that file input was invalid
        4. Open user-selected file with reading permissions and store it in a variable "file_data"
        5. Create empty list and store it in variable "all_conversions"
        5. For each line in file_data:
           1. Split each line into individual characters and assign it to variable "characters"
           2. Create empty list for every new word
           3. For each character in characters
              1. Concatenate character with new line character
              2. Set given character as the morse_dict key to look up and assign it to variable "to_append"
              3. Append converted character to its given word list
              4. Convert completed word to full conversion list
           4. Close file
           5. Request user input name to give to new converted file and assign it to variable "new_file"
           6. Open "new_file" with writing permissions and assign it to variable "file_writing"
           7. For each word in all_conversions:
              1. For each character in word:
              2. Write each character in a word onto a line
              3. Separate words per line
           8. Close file
           9. Output that conversion was complete
           10. While passthru2:
               1. Asks user if they would like to continue and collect user input
               2. If user input is equal to yes:
                  1. Output resetting and assign "passthru2" to FALSE
               3. Otherwise if user input is equal to no:
                  1. Output thank you to the user
                  2. Assign variable "passthru2" equal to FALSE
                  3. Assign variable "passthru" equal to TRUE
               4. Otherwise:
                  1. Output invalid input


* Purpose: contains the main function
* Name: main
* Parameters: [NONE]
* Return: completed file
* Algorithm:
  1. Output a welcome statement to the user and code purpose to user
  2. Assign function "read_file_conversion" to variable "file_name"
  3. Assign function "read_conver_file_into_dictionary" to variable "morse_dict"
  4. Invoke function "convert_morse"
5. Invoke main function