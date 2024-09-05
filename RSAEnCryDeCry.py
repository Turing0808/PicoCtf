from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair(bits=2048):
    key = RSA.generate(bits)
    return key.export_key(), key.publickey().export_key()

def rsa_cipher(message: str, key: bytes, encrypt: bool) -> bytes:
    cipher = PKCS1_OAEP.new(RSA.import_key(key))
    return cipher.encrypt(message.encode()) if encrypt else cipher.decrypt(message).decode()

if __name__ == "__main__":
    private_key, public_key = generate_keypair()
    
    text = "RSA!"
    encrypted_text = rsa_cipher(text, public_key, True)
    decrypted_text = rsa_cipher(encrypted_text, private_key, False)

    print(f"Text: {text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")