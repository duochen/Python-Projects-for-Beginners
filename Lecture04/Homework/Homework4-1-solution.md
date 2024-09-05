#### Explanation of the Code
1. **`roll_die(num_rolls, num_sides)`**: This function simulates rolling a die `num_rolls` times. It creates a list `results` to keep track of how many times each side of the die comes up. It then simulates each roll and updates the counts accordingly.

2. **`plot_results(results)`**: This function takes the list of results and uses `matplotlib` to create a bar chart showing the frequency of each die face. The x-axis represents the die faces, and the y-axis represents the frequency.

3. **`main()`**: This function gets input from the user for the number of rolls and the number of sides on the die. It then calls `roll_die()` to perform the simulation and `plot_results()` to display the results.

This project introduces students to basic concepts of randomness and data visualization in a fun and engaging way.