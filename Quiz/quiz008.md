# Quiz 008


## Paper Solution
![IMG_8539](https://github.com/user-attachments/assets/71c0240f-b824-4997-9602-a7a965ab5895)

## Code
```.py
def print_hotel_rooms():

    room_number = 1

    for floor in range(1, 11):
        for room in range(1, 11):
            room_name = f"{floor}F{room:02d}"
            print(f"{room_number}-Room {room_name}")
            room_number += 1

print_hotel_rooms()

```

## Proof of work
<img width="1470" alt="Screenshot 2024-09-16 at 21 12 54" src="https://github.com/user-attachments/assets/0fd14fd9-e3c2-4e3b-808c-8008104be5c3">
