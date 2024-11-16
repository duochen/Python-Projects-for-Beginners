import csv

# Specify the path to your .csv file
file_path = 'sample.csv'

try:
    # Open the .csv file
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        # Create a DictReader object
        csv_reader = csv.DictReader(csv_file)

        # Print each row as a dictionary
        print("Reading .csv file using DictReader:")
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print(f"File '{file_path}' not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
