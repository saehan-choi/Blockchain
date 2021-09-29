import hashlib

# you can change the x value
# than you can see the change of hashvalue
x = 2

x = repr(x).encode('utf-8')
print(x)
print(hashlib.sha256(x).hexdigest())