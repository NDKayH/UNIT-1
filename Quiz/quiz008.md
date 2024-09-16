# Quiz 008


## Paper Solution


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
![Uploading IMG_8539.JPG…]()
