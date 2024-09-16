# Quiz 003


## Paper Solution
![IMG_8534](https://github.com/user-attachments/assets/2ed445fd-4b9d-4485-a5ec-e729e442ea49)


## Code
```.py
dna_chain = input("Enter a DNA chain (using 'a', 'g', 't', 'c'): ").lower()

new_chain = ""

for protein in dna_chain:
    if protein == 'a':
        new_chain += 't'
    elif protein == 'g':
        new_chain += 'c'
    elif protein == 't':
        new_chain += 'a'
    elif protein == 'c':
        new_chain += 'g'
    else:
        print("Error: Invalid DNA character found")
        new_chain = ""
        break #used when a certain condition is met and you no longer want the loop to continue

if new_chain:
    print(new_chain)

```

## Proof of work
<img width="1470" alt="Screenshot 2024-09-16 at 19 44 46" src="https://github.com/user-attachments/assets/e111de0b-972a-4807-a6ba-d3436401baa3">
