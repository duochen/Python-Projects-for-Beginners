import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # Scale: 0 (Not Hungry) - 100 (Very Hungry)
        self.happiness = 50  # Scale: 0 (Sad) - 100 (Happy)
        self.energy = 50  # Scale: 0 (Tired) - 100 (Energetic)

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        self.hunger = max(self.hunger, 0)
        print(f"{self.name} has been fed. Hunger level: {self.hunger}, Happiness level: {self.happiness}")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 10
            print(f"{self.name} is playing! Happiness level: {self.happiness}, Energy level: {self.energy}")
        else:
            print(f"{self.name} is too tired to play!")

    def sleep(self):
        self.energy += 20
        self.happiness += 5
        self.energy = min(self.energy, 100)
        print(f"{self.name} is sleeping. Energy level: {self.energy}, Happiness level: {self.happiness}")

    def status(self):
        print(f"{self.name}'s status: Hunger={self.hunger}, Happiness={self.happiness}, Energy={self.energy}")

def main():
    pet_name = input("What would you like to name your virtual pet? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nChoose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check Status")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.status()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
