text = "GOOD MORNING"
n = 1

def encrypt(text,n):
    ans = ""
    for i in range(len(text)):
        ch = text[i]
        if ch==" ":
            ans+=" " 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

print("Normal Text : " + text)
print("Cipher Text : " + encrypt(text,n))