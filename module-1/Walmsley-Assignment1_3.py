# Jonathon Walmsley
# 6/7/2026
# Module 1.3 Assignment
# Purpose: Play the "100 Bottles of Beer on the Wall" song with user input.

def countDown(n):
    for i in range(n, 0, -1):
        print(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall, {i} bottle{'s' if i != 1 else ''} of beer.")
        if i - 1 > 0:
            print(f"Take one down and pass it around, {i - 1} bottle{'s' if i - 1 != 1 else ''} of beer on the wall.\n")
        else:
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

def main():
    while True:
        try:
            numBottles = int(input("Enter the number of bottles of beer on the wall (1-100): "))
            print("\n")
            if 1 <= numBottles <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    countDown(numBottles)
    print("Time to buy more bottles of beer.")

if __name__ == "__main__":
    main()