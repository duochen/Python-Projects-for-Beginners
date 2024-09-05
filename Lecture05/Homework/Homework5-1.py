import json
import random

class Game:
    def __init__(self):
        self.rooms = {
            'start': 'You are in the starting room.',
            'north': 'You are in the northern room.',
            'south': 'You are in the southern room.',
            'east': 'You are in the eastern room.',
            'west': 'You are in the western room.'
        }
        self.items = ['sword', 'shield', 'potion']
        self.enemies = ['goblin', 'dragon', 'orc']
        self.inventory = []
        self.enemies_encountered = []
        self.moves = 0
        self.current_room = 'start'
        
    def move(self, direction):
        if direction in self.rooms:
            self.current_room = direction
            self.moves += 1
            print(self.rooms[direction])
            self.interact()
        else:
            print("You can't go that way.")
        
    def interact(self):
        # Random chance to find an item or encounter an enemy
        if random.random() > 0.7:
            item = random.choice(self.items)
            self.inventory.append(item)
            print(f"You found a {item}!")
            
        if random.random() > 0.5:
            enemy = random.choice(self.enemies)
            self.enemies_encountered.append(enemy)
            print(f"You encountered a {enemy}!")
    
    def end_game(self):
        print("Game Over")
        print(f"Total Moves: {self.moves}")
        print(f"Items Collected: {self.inventory}")
        print(f"Enemies Encountered: {self.enemies_encountered}")
        
        # Save data to JSON
        data = {
            'moves': self.moves,
            'items': self.inventory,
            'enemies': self.enemies_encountered
        }
        with open('game_data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        # Analyze data
        self.analyze_data()
    
    def analyze_data(self):
        with open('game_data.json', 'r') as f:
            data = json.load(f)
            
        print("\n--- Data Analysis ---")
        print(f"Average Moves: {data['moves']}")
        
        item_counts = {item: data['items'].count(item) for item in set(data['items'])}
        print(f"Most Collected Items: {item_counts}")
        
        enemy_counts = {enemy: data['enemies'].count(enemy) for enemy in set(data['enemies'])}
        print(f"Most Common Enemies: {enemy_counts}")

# Game Execution
if __name__ == "__main__":
    game = Game()
    game.move('north')
    game.move('east')
    game.move('south')
    game.end_game()
