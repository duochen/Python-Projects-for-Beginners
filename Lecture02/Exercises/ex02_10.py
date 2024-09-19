import csv

items = ['sandwiches', 'chips', 'juice', 'cookies']
with open('picnic_items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item'])
    for item in items:
        writer.writerow([item])
