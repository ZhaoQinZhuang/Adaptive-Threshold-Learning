# 赵秦壮
# 开发时间：2022/11/19  17:05
import numpy as np
import pandas as pd
from causallearn.search.FCMBased import lingam

from tools import ShowTrueC

# np.set_printoptions(suppress=True)
# if __name__ == '__main__':
#     dn = 1
#     path = 'D:\\科研\\实验\\10-5\\'
#     dataPath = path + 'data' + str(dn) + '.csv'
#     X = pd.read_csv(dataPath, header=None, engine='python')
#     model = lingam.VARLiNGAM(lags=5)
#     model.fit(X)
#     results = model.adjacency_matrices_
#     print(results)

if __name__ == '__main__':
    a = 0.94535
    b = 1
    a =2* a * b / (a + b)
    print(round(a,5))