# Function to encode the string
def cypher(string):
    replaced_string = ""
    for char in string:
        if char.isalpha():
            ascii_value = ord(char) + 15
            if char.islower():
                if ascii_value > ord('z'):
                    ascii_value -= 26
            else:
                if ascii_value > ord('Z'):
                    ascii_value -= 26
            replaced_string += chr(ascii_value)
        else:
            replaced_string += char
    return replaced_string

# Get the input string from user
input_string = input("Enter a string to encode: ")
result = cypher(input_string)
print("Encoded string:", result)
