# Secret Code Generator

# Function to encode a message with a given shift
def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase for proper shifting
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character within the alphabet range using modulo
            encoded_message += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded_message += char  # Non-alphabet characters remain the same
    return encoded_message

# Function to decode a message with a given shift
def decode_message(message, shift):
    # Decoding is just encoding with the negative shift
    return encode_message(message, -shift)

# Function to handle user input and menu choices
def menu():
    while True:
        print("\nSecret Code Generator") 
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter the shift number: "))
                encoded = encode_message(message, shift)
                print(f"Encoded message: {encoded}")
            except ValueError:
                print("Invalid shift number. Please enter an integer.")
                
        elif choice == '2':
            message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter the shift number: "))
                decoded = decode_message(message, shift)
                print(f"Decoded message: {decoded}")
            except ValueError:
                print("Invalid shift number. Please enter an integer.")
                
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# Run the menu to start the program
if __name__ == "__main__":
    menu()
