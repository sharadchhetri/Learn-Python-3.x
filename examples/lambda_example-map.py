# map(function, iterables)

list1 = [1,2,3,4,56,2,4,5,77,33,4]

print(list1)

def multiply(x, y):
    return x+y

q = map(multiply,'abc','def')
print(list(q))

