items = ['sandwiches', 'chips', 'juice', 'cookies']
width = 20
print("Picnic Items".center(width, '-'))
for item in items:
    print(item.ljust(width//2) + item.rjust(width//2))
