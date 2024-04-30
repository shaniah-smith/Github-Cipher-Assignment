import sys

def unique_cipher(input_text, shift_amount):
    result_text = ""
    for char in input_text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
            result_text += encrypted_char
    return result_text

def display_blocks(text):
    for i in range(0, len(text), 5):
        print(text[i:i+5], end=' ')
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 unique_cipher.py <shift>")
        sys.exit(1)

    try:
        shift = int(sys.argv[1])
        shift = shift % 26
    except ValueError:
        print("Please provide a valid integer for the shift value.")
        sys.exit(1)

    for line in sys.stdin:
        line = line.upper()
        encrypted_message = unique_cipher(line, shift)
        display_blocks(encrypted_message)

if __name__ == "__main__":
    main()
