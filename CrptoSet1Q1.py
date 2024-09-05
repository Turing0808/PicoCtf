import base64
hex="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytearr = bytes.fromhex(hex)
base64str=base64.b64encode(bytearr).decode('utf-8')
print(base64str)