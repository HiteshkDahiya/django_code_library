def modify(x):
    x = x * 2
    print("inside", x)

x = 10
modify(x)
print('outside', x)