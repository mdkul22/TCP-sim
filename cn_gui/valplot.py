import math
import numpy as np
import matplotlib.pyplot as plt
list1 = []
list2 = []
for x in range(100000):
    t = math.ceil(np.random.normal(50, 5))
    list1.append(t)

for x in range(0,99):
    list2.append(0)

for x in list1:
    for y in range(100):
        if x == y:
            list2[y-1]+=1

plt.plot(list2)
plt.show()
