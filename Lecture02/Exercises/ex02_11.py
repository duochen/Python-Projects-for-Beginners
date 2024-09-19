import json

data = {'items': ['sandwiches', 'chips', 'juice', 'cookies']}
with open('picnic_items.json', 'w') as file:
    json.dump(data, file)
