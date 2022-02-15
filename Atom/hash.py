from hashlib import sha256
h = sha256()
h.update(b'Dawson')
hash = h.hexdigest()
print(hash)
