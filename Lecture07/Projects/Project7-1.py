import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_weather_data(file_path):
    weather_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weather_data.append({
                'date': datetime.strptime(row['Date'], '%Y-%m-%d'),
                'temperature': float(row['Temperature']),
                'weather': row['Weather'],
                'precipitation': float(row['Precipitation'])
            })
    return weather_data

def calculate_statistics(weather_data):
    total_temp = sum([data['temperature'] for data in weather_data])
    avg_temp = total_temp / len(weather_data)
    max_temp = max(weather_data, key=lambda x: x['temperature'])['temperature']
    min_temp = min(weather_data, key=lambda x: x['temperature'])['temperature']
    rainy_days = sum(1 for data in weather_data if data['weather'] == 'Rainy')
    
    return avg_temp, max_temp, min_temp, rainy_days

def plot_temperature_over_time(weather_data):
    dates = [data['date'] for data in weather_data]
    temps = [data['temperature'] for data in weather_data]
    plt.plot(dates, temps)
    plt.title('Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

def main():
    weather_data = read_weather_data('weather_data.csv')
    avg_temp, max_temp, min_temp, rainy_days = calculate_statistics(weather_data)
    
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Maximum Temperature: {max_temp:.2f}°C")
    print(f"Minimum Temperature: {min_temp:.2f}°C")
    print(f"Number of Rainy Days: {rainy_days}")
    
    plot_temperature_over_time(weather_data)

if __name__ == '__main__':
    main()
