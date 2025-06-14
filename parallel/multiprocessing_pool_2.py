# 参考⑤：わかりやすい。
# https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b


import time
from multiprocessing import Pool

def nijou(inputs):
    x, y = inputs
    print('input: %d, %d' % (x, y))
    time.sleep(2)
    retValue = [x * x, y * y]
    print('double: %d, %d' % (retValue[0], retValue[1]))
    return(retValue)

if __name__ == "__main__":
    p = Pool(4)
    values = [(x, y) for x in range(4) for y in range(4)]
    print(values)
    result = p.map(nijou, values)
    print(result)


# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
# input: 0, 0
# input: 0, 1
# input: 0, 2
# input: 0, 3
# double: 0, 0
# input: 1, 0
# double: 0, 1
# input: 1, 1
# double: 0, 4
# input: 1, 2
# double: 0, 9
# input: 1, 3
# double: 1, 0
# (略)
# double: 9, 4
# double: 9, 9
# [[0, 0], [0, 1], [0, 4], [0, 9], [1, 0], [1, 1], [1, 4], [1, 9], [4, 0], [4, 1], [4, 4], [4, 9], [9, 0], [9, 1], [9, 4], [9, 9]]
