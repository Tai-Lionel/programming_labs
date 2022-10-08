import math
n = int(input(""))
# corner case
if n == 1:
    print(2)
else:
    print(math.ceil(n/3))
