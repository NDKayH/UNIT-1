# Quiz 001


## Paper Solution
![IMG_8535](https://github.com/user-attachments/assets/b8beba88-a602-42b4-ae10-93a4f5508962)


## Code
```.py
number = int(input("Enter a number: "))

factors = []

for i in range(1, number):
    if number % i == 0:
        factors.append(i) #it modifies the list in place, meaning the original list is changed.

new_factors = ""
for i in range(len(factors)):
    if i == len(factors) - 1:
        new_factors += str(factors[i])
    else:
        new_factors += str(factors[i]) + ", "

print(new_factors)

```

## Proof of work
<img width="1470" alt="Screenshot 2024-09-16 at 20 39 52" src="https://github.com/user-attachments/assets/fb2bfce2-fff8-4f6e-9348-324eebe70395">
