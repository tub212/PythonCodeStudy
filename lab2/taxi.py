"""Taxi"""
import math
def taxi(num1, num2):
    """return price"""
    price = 0
    price2 = 0
    if num1 <= 1:
        price =  35
    elif num1 <= 12:
        price = 35+ (num1-1)*5
    elif num1 <= 20:
        price = 90+(num1-12)*5.5
    elif num1 <= 40:
        price = 134+(num1-20)*6
    elif num1 <= 60:
        price = 254+(num1-40)*6.5
    elif num1 <= 80:
        price = 384+(num1-60)*7.5
    else:
        price = 534+(num1-80)*8.5
    price = math.ceil(price)
    if price % 2 == 0:
        price = price + 1
    price2 = math.floor(num2 * 1.5)
    if price2 % 2 == 1:
        price2 = price2 - 1
    print int(price + price2)
taxi(input(), input())
