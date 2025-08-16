# 参考⑤：わかりやすい。
# https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b

import time
from multiprocessing import Pool

# 並列処理させる関数
def nijou(x):
    print('input: %d' % x)
    time.sleep(2)
    retValue = x * x
    print('double: %d' % (retValue))
    return(retValue)

if __name__ == "__main__":
    p = Pool(4) # プロセス数を4に設定
    result = p.map(nijou, range(10))  # nijou()に0,1,..,9を与えて並列演算
    print(result)


# input: 0
# input: 1
# input: 2
# input: 3
# double: 0
# input: 4
# double: 1
# input: 5
# double: 4
# input: 6
# double: 9
# input: 7
# double: 16
# input: 8
# double: 25
# input: 9
# double: 36
# double: 49
# double: 64
# double: 81
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
