Cyphers

This is a simple Python script that encodes a string using a Caesar cipher algorithm. The script takes an input string from the user, applies the encoding algorithm, and outputs the encoded string.

Table of Contents
Installation
Usage
Algorithm
Contributing
Contact

Installation:
Make sure you have Python installed on your system.
Clone or download the script to your local machine.
Open a terminal or command prompt and navigate to the directory where the script is located.
Run the script using the command python filename.py (replace filename.py with the actual name of the script).

Usage:
Once you have done istallation, run the script, You will be prompted to enter a string to encode. 
Type your desired string and press Enter.
The script will encode the string using a Caesar cipher and display the encoded string.

Algorithm:
The script uses a simple Caesar cipher algorithm to encode the input string. Here's how the algorithm works:
Iterate over each character in the input string.
If the character is an alphabet, get its ASCII value and add 15 to it.
If the character is lowercase and the resulting ASCII value is greater than the ASCII value of 'z', subtract 26 to wrap around.
If the character is uppercase and the resulting ASCII value is greater than the ASCII value of 'Z', subtract 26 to wrap around.
Append the encoded character to the replaced_string.
If the character is not an alphabet, append it as is to the replaced_string.
Finally, return the replaced_string as the encoded string.

Example:
![Screenshot (37)](https://github.com/Richa31182/Final-Capstone/assets/127997453/fb7f5e6e-0462-4869-84c7-9c068703d286)

Contributing:
Contributions to this project are welcome. If you find any issues or want to add new features, please submit a pull request.

Contact:
If you have any questions or suggestions regarding this project, please feel free to contact the author at [uplopwar.richa@gmail.com]
