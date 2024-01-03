def separate_and_convert(input_string):
    # Separate into number and letter substrings
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    # Convert even numbers in the number string to ASCII code decimal values
    even_numbers_ascii = [str(ord(char)) for char in number_string if int(char) % 2 == 0]

    # Convert upper-case letters in the letter string to ASCII code decimal values
    upper_case_ascii = [str(ord(char)) for char in letter_string if char.isupper()]

    # Output the results
    print("Number String:", number_string)
    print("Letter String:", letter_string)
    print("Even Numbers (ASCII):", ', '.join(even_numbers_ascii))
    print("Upper-case Letters (ASCII):", ', '.join(upper_case_ascii))

# Example usage
input_string = '56aAWW1984sktr235270aYmn145ss785fsq31D0'
separate_and_convert(input_string)