import random
import matplotlib.pyplot as plt

def roll_die(num_rolls, num_sides=6):
    results = [0] * num_sides
    for _ in range(num_rolls):
        roll = random.randint(1, num_sides)
        results[roll - 1] += 1
    return results

def plot_results(results):
    num_sides = len(results)
    sides = range(1, num_sides + 1)
    plt.bar(sides, results, tick_label=sides)
    plt.xlabel('Die Face')
    plt.ylabel('Frequency')
    plt.title('Dice Rolling Simulation Results')
    plt.show()

def main():
    num_rolls = int(input("Enter the number of rolls: "))
    num_sides = int(input("Enter the number of sides on the die (default is 6): ") or 6)
    
    results = roll_die(num_rolls, num_sides)
    print(f"Results: {results}")
    
    plot_results(results)

if __name__ == "__main__":
    main()
