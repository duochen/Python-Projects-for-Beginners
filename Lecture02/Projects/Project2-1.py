import os
from datetime import datetime

# Directory to store diary entries
DIARY_DIR = "diary_entries"

def create_diary_entry():
    if not os.path.exists(DIARY_DIR):
        os.makedirs(DIARY_DIR)
    
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{DIARY_DIR}/{date}.txt"
    
    entry = input("Write your diary entry: ")
    
    with open(filename, "a") as file:
        file.write(f"{datetime.now().strftime('%H:%M:%S')} - {entry}\n")
    
    print(f"Diary entry saved to {filename}")

def read_diary_entry(date):
    filename = f"{DIARY_DIR}/{date}.txt"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            print(f"\nDiary Entry for {date}:\n")
            print(content)
    else:
        print(f"No entry found for {date}")

def search_diary_entries(keyword):
    if not os.path.exists(DIARY_DIR):
        print("No diary entries found.")
        return
    
    found = False
    for entry_file in os.listdir(DIARY_DIR):
        with open(f"{DIARY_DIR}/{entry_file}", "r") as file:
            content = file.read()
            if keyword.lower() in content.lower():
                print(f"Keyword found in {entry_file}:\n")
                print(content)
                found = True
                
    if not found:
        print("No entries contain the keyword.")

def main():
    while True:
        print("\n--- Personal Diary Application ---")
        print("1. Create Diary Entry")
        print("2. Read Diary Entry")
        print("3. Search Diary Entries")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_diary_entry()
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            read_diary_entry(date)
        elif choice == "3":
            keyword = input("Enter a keyword to search for: ")
            search_diary_entries(keyword)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
