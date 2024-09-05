import csv
import random
from datetime import datetime, timedelta

# List of weather types
weather_types = ['Sunny', 'Rainy', 'Cloudy', 'Snowy']

# Function to generate random weather data
def generate_weather_data(num_days=365):
    data = []
    start_date = datetime.now() - timedelta(days=num_days)

    for i in range(num_days):
        date = start_date + timedelta(days=i)
        temperature = round(random.uniform(-10, 35), 1)  # Random temperature between -10°C and 35°C
        weather = random.choice(weather_types)
        precipitation = round(random.uniform(0, 20), 1) if weather == 'Rainy' else 0.0
        data.append([date.strftime('%Y-%m-%d'), temperature, weather, precipitation])

    return data

# Write data to CSV file
def write_to_csv(file_path, data):
    header = ['Date', 'Temperature', 'Weather', 'Precipitation']
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

# Generate and save the data
weather_data = generate_weather_data(num_days=365)
write_to_csv('weather_data.csv', weather_data)

print("weather_data.csv generated successfully!")
