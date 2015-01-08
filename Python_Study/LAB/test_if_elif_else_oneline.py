def test(num):
    return num if num <= 5 and num >= 0 else (num*2 if num <= 10 and num > 5 \
            else (num*3 if num <= 15 and num > 10 else \
                  (num*4 if num<=20 and num>15 else num*5)))
print test(input())
