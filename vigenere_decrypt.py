import string

def vigenere_decrypt(vigeneretext: str, key: str) -> str:
    """
    Decrypts vigenere
    """
    key = key.upper()
    key_length = len(key)
    decrypted_plaintext = []
    key_index = 0  # Tracks which key character to use for letters

    for char in vigeneretext:
        if char.isalpha():
            cipher_val = ord(char.upper()) - ord('A')
            key_val = ord(key[key_index % key_length]) - ord('A')

            decrypted_val = ((cipher_val - key_val) + 26) % 26
            decrypted_char = chr(decrypted_val + ord('A'))

            decrypted_plaintext.append(decrypted_char)
            key_index += 1  # Advance key only for letters
        elif char.isspace():
            decrypted_plaintext.append(' ')
        # else: skip (remove) punctuation, numbers, etc.

    return ''.join(decrypted_plaintext)


if __name__ == "__main__":
    # Read plaintext from file
    try:
        with open("vigenere.txt", "r", encoding="utf-8") as f:
            vigeneretext = f.read()
    except FileNotFoundError:
        print("Error: vigenere.txt not found.")
        exit(1)

    # Example key (must be at least length 5)
    key = "TZFTPMC"

    decrypted  = vigenere_decrypt(vigeneretext, key)

    print("Vigenere ciphertext from file:\n", vigeneretext)
    print("\nKey       :", key)
    print("Decrypted: ", decrypted)

