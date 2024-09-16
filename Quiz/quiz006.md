# Quiz 006


## Paper Solution
![IMG_8538](https://github.com/user-attachments/assets/57707e03-52b1-4539-b49a-3628823352df)

## Code
```.py
import random
import string

def generate_passwords():
    passwords = []

    characters = string.ascii_letters + string.digits

    for _ in range(10):
        password = ''.join(random.choice(characters) for _ in range(20))  #taught by Aren
        passwords.append(password)

    return passwords

passwords = generate_passwords()
for i, password in enumerate(passwords, 1):
    print(f"Password {i}: {password}")
```

## Proof of work
<img width="1470" alt="Screenshot 2024-09-16 at 20 55 45" src="https://github.com/user-attachments/assets/67f5e815-07ee-456a-af5c-2d7acd78cc73">
