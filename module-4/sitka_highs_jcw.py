import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt # pyright: ignore[reportMissingModuleSource]

def read_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # Get dates, high and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
    return dates, highs, lows

def display_menu():
    print("Welcome to the Sitka Weather App!")
    print("Please select an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. View Both High and Low Temperatures")
    print("4. Exit")

def display_graph(fig):
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    # Read the weather data once from the CSV file
    filename = 'C:\\Users\\Jonat\\source\\repos\\csd\\csd-325\\module-4\\sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)
    
    while True:
        display_menu()
        fig, ax = plt.subplots()
        choice = input("Enter your choice (1-4): ")
        if choice == "1": # View High Temperatures
            plt.title("Daily high temperatures - 2018", fontsize=24)
            ax.plot(dates, highs, c='red')
            display_graph(fig)
        elif choice == "2": # View Low Temperatures
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.plot(dates, lows, c='blue')
            display_graph(fig)
        elif choice == "3":
            plt.title("Daily high and low temperatures - 2018", fontsize=22)
            plt.plot(dates, highs, c='red') 
            plt.plot(dates, lows, c='blue')
            display_graph(fig)
        elif choice == "4":
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()