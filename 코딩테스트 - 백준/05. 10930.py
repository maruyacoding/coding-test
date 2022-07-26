import hashlib

s = input()
encoded_data = s.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
