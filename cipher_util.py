def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    msg = "Secure Transmission"
    shift = 4
    enc = caesar_encrypt(msg, shift)
    dec = caesar_decrypt(enc, shift)
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
