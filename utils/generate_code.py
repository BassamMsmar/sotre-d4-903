import random

def genetate(lenth=8):
    date = '0123456789ABCDEFGHIGKLMOPQRCTUVWXYZ'
    code = ''.join(random.choice(date) for _ in lenth)
    return code


