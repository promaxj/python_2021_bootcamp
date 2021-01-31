from day8.art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        while new_position > len(alphabet):
            new_position %= len(alphabet)
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encodeed text is: \n{cipher_text}")
def decrypt(cipher_text, shift_amount):
    decipher_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        while new_position < 0:
            new_position += len(alphabet)
        new_letter = alphabet[new_position]
        decipher_text += new_letter
    print(f"The encodeed text is: \n{decipher_text}")



print(logo)
type_again = True
while type_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        type_again = False
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        type_again = False
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(cipher_text=text, shift_amount=shift)
