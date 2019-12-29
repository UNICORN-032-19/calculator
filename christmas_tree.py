from time import sleep
from random import randint

rnd2 = randint(1, 30)

def grentree():
    print('\033c')
    for x in range(1, 30, 2):
        rnd1 = randint(1, rnd2)
        if x == 1:
            ch = '$'
        elif rnd1 % 4 == 0:
            ch = '0'
        elif rnd1 % 3 == 0:
            ch = 'i'
        else:
            ch = '*'
        print('{:^33}'.format(ch * x))
    print('{:^33}'.format('|||'))
    print("{:^33}".format('|||'))
    sleep(.75)
    
    
while True:
    grentree()
