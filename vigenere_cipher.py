import string

def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenère cipher.
    - Only letters are encrypted (A–Z).
    - All letters are converted to uppercase.
    - Punctuation and numbers are REMOVED.
    - Each letter is mapped: A=0, B=1, ..., Z=25.
    - Ciphertext letter = (plaintext_letter + key_letter) mod 26
    - The nth letter uses key[(n mod K)] where K = len(key).
    """
    key = key.upper()
    key_length = len(key)
    ciphertext = []
    key_index = 0  # Tracks which key character to use for letters

    for char in plaintext:
        if char.isalpha():
            plain_val = ord(char.upper()) - ord('A')
            key_val = ord(key[key_index % key_length]) - ord('A')

            cipher_val = (plain_val + key_val) % 26
            cipher_char = chr(cipher_val + ord('A'))

            ciphertext.append(cipher_char)
            key_index += 1  # Advance key only for letters
        elif char.isspace():
            ciphertext.append(' ')
        # else: skip (remove) punctuation, numbers, etc.

    return ''.join(ciphertext)


if __name__ == "__main__":
    # Read plaintext from file
    try:
        with open("plaintext.txt", "r", encoding="utf-8") as f:
            plaintext = f.read()
    except FileNotFoundError:
        print("Error: plaintext.txt not found.")
        exit(1)

    # Example key (must be at least length 5)
    key = "fake key"

    encrypted = vigenere_encrypt(plaintext, key)

    print("Plaintext from file:\n", plaintext)
    print("\nKey       :", key)
    print("Ciphertext:", encrypted)

