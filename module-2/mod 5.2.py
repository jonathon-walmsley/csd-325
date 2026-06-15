# Name: Jonathon Walmsley
# Date: 04/19/2026
# Assignment: 5.2
# Purpose: Collect user information and store it in a file, then read and display the contents of the file.

def main():
    # Do While fileName does not contain any illegal characters
    while True:
        fileName = input("Enter the file name (e.g., user_data.txt): ")
        if fileName and not any(char in fileName for char in '<>:"/\\|?*'):
            fileName += " data.txt"
            break
        else:
            print("Invalid file name! Please avoid using characters like <>:\"/\\|?* and ensure the name is not empty.")
    
    userName = input("Enter your name: ")
    streetAddress = input("Enter your street address: ")
    phoneNumber = input("Enter your phone number: ")

    # Write the user information to the specified file
    with open(fileName, 'w') as file:
        file.write(f"{userName},{streetAddress},{phoneNumber}\n")

    # Read the contents of the file and display it
    print(f'\nContents of the file "{fileName}":')
    with open(fileName, 'r') as file:
        contents = file.read()
        print(contents)

if __name__ == "__main__":
    main()