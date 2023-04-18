def abc():
    print('a')
    print('b')
    print('c')

def get_vat(price, vat_rate = 0.1):
    return price*vat_rate

total = get_vat(10000)

print('total', total)

total = get_vat(1000000, 0.3)

print('total', total)