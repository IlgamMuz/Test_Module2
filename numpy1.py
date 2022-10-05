import numpy as np
# a = np.int32(1000)
# b = a + 25
# print(b)
# print(type(b))
print(*sorted(map(str, set(np.sctypeDict.values()))), sep="\n")