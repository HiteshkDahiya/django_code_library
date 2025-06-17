a = 'PaBanI'
# print((''.join([x.lower() if x.isupper() else x.upper() for x in reversed(a)])))
b = a[::-1]
print(b.swapcase())

