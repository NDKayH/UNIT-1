# Quiz 001


## Paper Solution
![IMG_7118](https://github.com/user-attachments/assets/1bc17d7e-cd14-40a5-971f-34b9ea113a3d)

## Code
```.py
word = input("Enter a word: ")

numbers_in_between = 0
for i in range(1, len(word) - 1):
    numbers_in_between += 1

print(f"{word} - {word[0]}{numbers_in_between}{word[-1]}")
```

## Proof of work
<img width="1470" alt="Screenshot 2024-09-16 at 19 48 08" src="https://github.com/user-attachments/assets/bb621488-291b-476b-819d-bded09eb4dd2">
