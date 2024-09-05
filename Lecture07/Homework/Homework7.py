import re

# Define game world data
rooms = {
    "start": {
        "description": "You are in a small room with a wooden door to the north.",
        "items": [],
        "north": "hallway"
    },
    "hallway": {
        "description": "You are in a long hallway with doors to the east and west.",
        "items": ["key"],
        "east": "library",
        "west": "kitchen"
    },
    "library": {
        "description": "You are in a dusty library filled with old books.",
        "items": ["book"],
        "west": "hallway"
    },
    "kitchen": {
        "description": "You are in a kitchen with a strange smell.",
        "items": ["knife"],
        "east": "hallway"
    }
}

# Initialize game state
current_room = "start"
inventory = []

# Function to print room description
def describe_room(room):
    print(rooms[room]["description"])
    if rooms[room]["items"]:
        print("You see the following items:", ", ".join(rooms[room]["items"]))

# Function to process user commands
def process_command(command):
    global current_room
    command = command.lower().strip()
    
    # Move between rooms
    match = re.match(r"go (north|south|east|west)", command)
    if match:
        direction = match.group(1)
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            describe_room(current_room)
        else:
            print("You can't go that way.")
        return
    
    # Pick up items
    match = re.match(r"take (.+)", command)
    if match:
        item = match.group(1)
        if item in rooms[current_room]["items"]:
            inventory.append(item)
            rooms[current_room]["items"].remove(item)
            print(f"You picked up the {item}.")
        else:
            print("There is no such item here.")
        return
    
    # List inventory
    if command == "inventory":
        print("You have:", ", ".join(inventory))
        return
    
    # Default case
    print("I don't understand that command.")

# Main game loop
print("Welcome to the Text Adventure Game!")
describe_room(current_room)

while True:
    command = input("> ")
    process_command(command)
