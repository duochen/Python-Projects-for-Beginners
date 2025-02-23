### Steps to Complete the Project: **Weather Data Parser**

#### **Step 1: Set Up the Project**
1. Create a new folder for the project (e.g., `weather_data_parser`).
2. Inside the folder, create a Python file (`weather_parser.py`) to write your code.
3. Download or create a CSV file (`weather_data.csv`) containing weather data with the following format:

   ```
   Date,Temperature,Weather,Precipitation
   2024-02-01,10,Sunny,0
   2024-02-02,8,Rainy,5
   2024-02-03,12,Cloudy,0
   2024-02-04,7,Rainy,8
   ```

4. Install `matplotlib` if not already installed:
   ```bash
   pip install matplotlib
   ```

---

#### **Step 2: Read the CSV File**
1. Open `weather_parser.py` and import necessary modules:
   ```python
   import csv
   import matplotlib.pyplot as plt
   ```
2. Write a function to read the weather data from the CSV file:
   ```python
   def read_weather_data(filename):
       weather_data = []
       with open(filename, mode='r') as file:
           reader = csv.DictReader(file)
           for row in reader:
               row["Temperature"] = float(row["Temperature"])
               row["Precipitation"] = float(row["Precipitation"])
               weather_data.append(row)
       return weather_data
   ```

---

#### **Step 3: Calculate Weather Statistics**
1. Create a function to calculate average, maximum, and minimum temperatures:
   ```python
   def calculate_temperature_stats(weather_data):
       temperatures = [day["Temperature"] for day in weather_data]
       avg_temp = sum(temperatures) / len(temperatures)
       max_temp = max(temperatures)
       min_temp = min(temperatures)
       return avg_temp, max_temp, min_temp
   ```
2. Create a function to count the number of rainy days:
   ```python
   def count_rainy_days(weather_data):
       return sum(1 for day in weather_data if day["Weather"] == "Rainy")
   ```

---

#### **Step 4: Plot Temperature Changes Over Time**
1. Write a function to plot the temperature changes:
   ```python
   def plot_temperature(weather_data):
       dates = [day["Date"] for day in weather_data]
       temperatures = [day["Temperature"] for day in weather_data]

       plt.figure(figsize=(10, 5))
       plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label="Temperature (°C)")
       plt.xlabel("Date")
       plt.ylabel("Temperature (°C)")
       plt.title("Temperature Changes Over Time")
       plt.xticks(rotation=45)
       plt.legend()
       plt.grid()
       plt.show()
   ```

---

#### **Step 5: Run the Program and Display Results**
1. In the `weather_parser.py` file, write the main execution logic:
   ```python
   if __name__ == "__main__":
       filename = "weather_data.csv"
       weather_data = read_weather_data(filename)

       avg_temp, max_temp, min_temp = calculate_temperature_stats(weather_data)
       rainy_days = count_rainy_days(weather_data)

       print(f"Average Temperature: {avg_temp:.2f}°C")
       print(f"Maximum Temperature: {max_temp}°C")
       print(f"Minimum Temperature: {min_temp}°C")
       print(f"Number of Rainy Days: {rainy_days}")

       plot_temperature(weather_data)
   ```
2. Save the file and run the script:
   ```bash
   python weather_parser.py
   ```

---

### **Bonus: Enhance the Project**
- **User Input**: Let users enter the filename instead of hardcoding it.
- **Error Handling**: Add try-except blocks to handle missing or incorrect data.
- **More Insights**: Calculate and display the most common weather condition.

---

### **What Students Learn**
✅ Reading and parsing CSV files using `csv.DictReader`  
✅ Performing basic statistical calculations in Python  
✅ Using list comprehensions for concise data processing  
✅ Visualizing data with `matplotlib`  
✅ Writing modular functions for better code organization  