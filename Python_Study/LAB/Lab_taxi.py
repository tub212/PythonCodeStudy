"""Lab_Taxi"""
import math
def taxi(distance, time):
    """return price"""
    price = 0
    price2 = 0
    if distance <= 1:
        price =  35
    elif distance <= 12:
        price = 35+ (distance-1)*5
    elif distance <= 20:
        price = 90+(distance-12)*5.5
    elif distance <= 40:
        price = 134+(distance-20)*6
    elif distance <= 60:
        price = 254+(distance-40)*6.5
    elif distance <= 80:
        price = 384+(distance-60)*7.5
    else:
        price = 534+(distance-80)*8.5
    price = math.ceil(price)
    if price % 2 == 0:
        price = price + 1
    price2 = math.floor(time * 1.5)
    if price2 % 2 == 1:
        price2 = price2 - 1
    print int(price + price2)
taxi(input(), input())
