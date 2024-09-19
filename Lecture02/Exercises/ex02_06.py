items = input("Enter items separated by commas: ").split(',')
with open('picnic_list.txt', 'w') as file:
    file.write(f"You are bringing {', '.join(items[:-1])}, and {items[-1]} to the picnic.")
