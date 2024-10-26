# Importing the library
import matplotlib.pyplot as plt

# Simple line plot
days = [1, 2, 3, 4, 5]
temperatures = [22, 24, 26, 23, 25]

plt.plot(days, temperatures)  # Plotting the days against temperatures
plt.xlabel('Days')  # Label for X-axis
plt.ylabel('Temperature (°C)')  # Label for Y-axis
plt.title('Temperature over Days')  # Title of the plot
plt.show()  # Display the plot

# Bar chart example
subjects = ['Math', 'Science', 'History', 'Art', 'PE']
scores = [85, 92, 78, 90, 95]

plt.bar(subjects, scores, color='skyblue')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title('Student Scores by Subject')
plt.show()

# Scatter plot example
height = [150, 160, 165, 170, 175]
weight = [50, 60, 62, 65, 70]

plt.scatter(height, weight, color='purple')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs. Weight')
plt.show()

# Customizing a line plot
plt.plot(days, temperatures, color='green', marker='o', linestyle='--')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Customized Temperature Plot')
plt.show()
