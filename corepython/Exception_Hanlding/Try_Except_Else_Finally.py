try:
    a = 10
    b = 0
    c = a / b
    print("Division:", c)
except ZeroDivisionError as e:
    print("Exception:",e)
except Exception as e:
    print("General exception:",e)

else:
    print("Else executed")

finally:
    print("Always Executed")