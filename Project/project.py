import csv

MASTER_CODE = "lockup_92135467"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def calculator():
    while True:
        user_input = input(f"{YELLOW}Enter the first number: {RESET}").strip()

        if user_input == MASTER_CODE:
            print(f"{GREEN}Secret code recognized. Switching...{RESET}")
            password_manager()
            break

        try:
            num1 = float(user_input)
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")
            continue

        operation = input(f"{YELLOW}Choose an operation (+, -, *, /): {RESET}")

        try:
            num2 = float(input(f"{YELLOW}Enter the second number: {RESET}"))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")
            continue

        if operation == '+':
            result = num1 + num2
            print(f"{CYAN}The result of {num1} + {num2} is: {result}{RESET}")
        elif operation == '-':
            result = num1 - num2
            print(f"{CYAN}The result of {num1} - {num2} is: {result}{RESET}")
        elif operation == '*':
            result = num1 * num2
            print(f"{CYAN}The result of {num1} * {num2} is: {result}{RESET}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{CYAN}The result of {num1} / {num2} is: {result}{RESET}")
            else:
                print(f"{RED}Error: Division by zero is not allowed.{RESET}")
        else:
            print(f"{RED}Invalid operation selected. Please choose +, -, *, or /.{RESET}")

        repeat = input(f"{YELLOW}Would you like to perform another calculation? (yes/no): {RESET}").strip().lower()

        if repeat != 'yes':
            print(f"{GREEN}Thank you for using the calculator. Goodbye!{RESET}")
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
        print(f"\n{CYAN}--- Password Manager ---{RESET}")
        print(f"{CYAN}1. Add a new password{RESET}")
        print(f"{CYAN}2. Delete a password{RESET}")
        print(f"{CYAN}3. View all passwords{RESET}")
        print(f"{CYAN}4. Exit{RESET}")

        choice = input(f"{YELLOW}Choose an option (1-4): {RESET}")

        if choice == '1':
            room = input(f"{YELLOW}Enter the room name/number: {RESET}")
            password = input(f"{YELLOW}Enter the password for this room: {RESET}")
            encrypted_password = encrypt_password(password)

            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([room, encrypted_password])

            print(f"{GREEN}Password for room '{room}' added successfully.{RESET}")

        elif choice == '2':
            room_to_delete = input(f"{YELLOW}Enter the room name/number for the password you want to delete: {RESET}")

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
                print(f"{GREEN}Password for room '{room_to_delete}' deleted successfully.{RESET}")
            else:
                print(f"{RED}No password found for room '{room_to_delete}'.{RESET}")

        elif choice == '3':
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                print(f"\n{CYAN}--- Stored Room Passwords ---{RESET}")

                for index, row in enumerate(reader):
                    if index == 0:
                        continue
                    room, encrypted_password = row
                    decrypted_password = decrypt_password(encrypted_password)
                    print(f"{CYAN}Room: {room}, Password: {decrypted_password}{RESET}")

        elif choice == '4':
            print(f"{GREEN}Exiting the password manager.{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please select a valid option.{RESET}")

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
