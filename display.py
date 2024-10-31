item=input("Enter item name:")
price=input("Enter price:")

line=item.ljust(22,'.')+price
print(line)

#or
totallen=len(item)+len(price)
dot='.'*(25-totallen)
print(item+dot+price)