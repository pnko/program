# 두번째 테스트 동기화 push puttl
import numpy as np

num_point = 2000
vectors_set = []
for i in range(num_point):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0, 0.9), np.random.normal(0.0, 0.9)])
    else:
        vectors_set.append([np.random.normal(3.5, 0.5), np.random.normal(1.0, 0.5)])

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.DataFrame({"x" : [v[0] for v in vectors_set],
                   "y" : [v[1] for v in vectors_set]})
sns.lmplot("x", "y", data=df, fit_reg=False, size=6)
plt.show()

a=2/3