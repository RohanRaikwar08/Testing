number = 1549
rev = 0
r = 0
n = number

while n > 0:
    r = n % 10
    rev = (rev * 10) + r
    n = n // 10

print("reverse number is =", rev)

















