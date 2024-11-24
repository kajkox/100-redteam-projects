import socket

# main menu prompt
MAIN_MENU: str = """
---Welcome to my UDP chat server---
Please select an option from the menu below:
    [0] - exit
    [1] - add a friend by name
    [2] - add a friend by ip:port 
Your choice: """


# function that adds friend by name to the contact book
def name_add(friend_name: str) -> None | SyntaxError:
    print(f"name works: {friend_name}")


# funtction that adds friend by ip, port pair to contact book
def ip_add(friend_ip: str, friend_port: int) -> None | SyntaxError:
    print(f"IP works: {friend_ip}, {friend_port}")

# main menu loop
def main() -> int:
    while True:
        print(f"{MAIN_MENU}")
        try:
            choice = int(input())
        except ValueError:
            print("Please input a number.")
        match choice:
            case 0:
                return 0
            case 1:
                print(f"Please input the name of the friend you want to add: ")
                name = input()
                try:
                    name_add(name)
                except SyntaxError:
                    print("[ERROR] Friend not found, make sure you typed the name correctly.")
            case 2:
                print(f"Please input your friend's ip: ")
                ip = input()
                print(f"Please input the port: ")
                try:
                    port = int(input)
                except ValueError:
                    print("[ERROR] Please input the port as a number.")
                try:
                    ip_add(ip, port)
                except SyntaxError:
                    print(f"[ERROR] Friend not found, make sure you typed the ip and port correctly.")
            case _:
                print(f"Option not found, make sure you typed the option correctly")

if __name__ == "__main__":
    main()