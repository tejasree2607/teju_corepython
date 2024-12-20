def dict(cart):
    total=sum(cart.values())
    print (f'total: {total}')
    if total>=20000 and total<=50000:
        total*=0.9
        return f'total after discount of 10% {total}'
    elif total>50000:
        total*=0.85
        return f'total after discount of 15% {total}'
cart={'Laptop':50000,'Headsphones':2000,'mouse':35000,'keyboard':1500,'monitor':8000,'usb-drive':1000}
print(dict(cart))