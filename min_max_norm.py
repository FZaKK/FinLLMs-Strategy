import numpy as np

# 给定数据
data = [3960, 1813, 296808, 51451]

# 计算数据的最小值和最大值
min_value = np.min(data)
max_value = np.max(data)

# 应用min-max归一化
min_max_normalized_data = [(x - min_value) / (max_value - min_value) for x in data]
print('min-max norm: ', min_max_normalized_data)
