import csv

with open('picnic_items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item', 'Quantity'])
    writer.writerow(['Sandwiches', 4])
    writer.writerow(['Juice', 2])
