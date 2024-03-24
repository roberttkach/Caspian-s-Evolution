import numpy.random as rd

def getCode(size: int = 64) -> int: return rd.randint(0, 10, size=size)

for i in range(10):
    print(str(getCode()))