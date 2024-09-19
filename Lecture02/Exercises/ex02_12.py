import json

items = ['sandwiches', 'chips', 'juice', 'cookies']
data = {'items': items}
with open('picnic_items.json', 'w') as file:
    json.dump(data, file)
