from zipfile import ZipFile
with open('Ashley-Madison.txt', 'r') as f:
    passwords = [line.strip() for line in f]

for i, password in enumerate(passwords):
    if i % 10000 == 0:
        print(f"Trying password no. {i}: {password}")
    try:
        with ZipFile('whitehouse_secrets.zip') as z:
            z.extractall(pwd=password.encode())

            print("Password =", password, f"(no. {i})")
            break
    except:
        continue
