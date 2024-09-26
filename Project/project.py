import csv


MASTER_CODE = "lockup_92135467"

def calculator():
    while True:
        user_input = input("Enter the first number: ").strip()

        if user_input == MASTER_CODE:
            print("Secret code recognized. Switching...")
            password_manager()
            break

        try:
            num1 = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        operation = input("Choose an operation (+, -, *, /): ")

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation selected. Please choose +, -, *, or /.")

        repeat = input("Would you like to perform another calculation? (yes/no): ").strip().lower()

        if repeat != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break


def password_manager():
    filename = "passwords.csv"

    try:
        with open(filename, mode='r', newline='') as file:
            pass
    except FileNotFoundError:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Room", "Password"])

    while True:
        print("\n--- Password Manager ---")
        print("1. Add a new password")
        print("2. Delete a password")
        print("3. View all passwords")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            room = input("Enter the room name/number: ")
            password = input("Enter the password for this room: ")
            encrypted_password = encrypt_password(password)

            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([room, encrypted_password])

            print(f"Password for room '{room}' added successfully.")

        elif choice == '2':
            room_to_delete = input("Enter the room name/number for the password you want to delete: ")

            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            found = False
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)

                for row in rows:
                    if row[0] != room_to_delete:
                        writer.writerow(row)
                    else:
                        found = True

            if found:
                print(f"Password for room '{room_to_delete}' deleted successfully.")
            else:
                print(f"No password found for room '{room_to_delete}'.")

        elif choice == '3':
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                print("\n--- Stored Room Passwords ---")

                for index, row in enumerate(reader):
                    if index == 0:
                        continue
                    room, encrypted_password = row
                    decrypted_password = decrypt_password(encrypted_password)
                    print(f"Room: {room}, Password: {decrypted_password}")

        elif choice == '4':
            print("Exiting the password manager.")
            break
        else:
           print("Invalid choice. Please select a valid option.")


def encrypt_password(s):
    chars = "0123456789"
    trans = chars[5:] + chars[:5]
    encrypted = ''
    for c in s:
        if c in chars:
            encrypted += trans[chars.index(c)]
        elif c.lower() in chars:
            encrypted += trans[chars.index(c.lower())].upper()
        else:
            encrypted += c
    return encrypted


def decrypt_password(s):
    return encrypt_password(s)

if __name__ == "__main__":
    calculator()
