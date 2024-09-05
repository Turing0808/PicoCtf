from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_decrypt(plain_text: str, key: bytes, iv: bytes, mode: str) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    if mode == 'encrypt':
        return cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    elif mode == 'decrypt':
        return unpad(cipher.decrypt(plain_text), AES.block_size).decode()

if __name__ == "__main__":
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    text = "Good Morning!"
    encrypted_text = encrypt_decrypt(text, key, iv, 'encrypt')
    decrypted_text = encrypt_decrypt(encrypted_text, key, iv, 'decrypt')

    print(f"Text: {text}")
    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")