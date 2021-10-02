from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...

# print(sha256(f'{x*y}'.encode()).hexdigest())
# print(sha256(f'{x*y}'.encode()).hexdigest()[:3])

while sha256(f'{x*y}'.encode()).hexdigest()[:3] != "000":
    y += 1
    print(sha256(f'{x*y}'.encode()).hexdigest())


print(f'The solution is y = {y}')
