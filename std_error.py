import pandas as pd
import numpy as np

# 读取CSV文件
df1 = pd.read_csv('000001历史数据.csv', header=None, skiprows=1)
df2 = pd.read_csv('002594历史数据.csv', header=None, skiprows=1)
df3 = pd.read_csv('600519历史数据.csv', header=None, skiprows=1)

df1_last_column = df1.iloc[:, -1]
df2_last_column = df2.iloc[:, -1]
df3_last_column = df3.iloc[:, -1]
df = pd.concat([df1_last_column, df2_last_column, df3_last_column], axis=1,
               keys=['Return_A', 'Return_B', 'Return_C'])

df['Return_A'] = df['Return_A'].apply(lambda x: float(x.strip('%')) / 100)
df['Return_B'] = df['Return_B'].apply(lambda x: float(x.strip('%')) / 100)
df['Return_C'] = df['Return_C'].apply(lambda x: float(x.strip('%')) / 100)

# 计算投资组合的日收益率
df['Portfolio_Return'] = 0.45 * df['Return_A'] + 0.35 * df['Return_B'] + 0.20 * df['Return_C']

# 计算投资组合的收益率标准差
portfolio_std = np.std(df['Portfolio_Return'])
print('投资组合的收益率标准差为：{}'.format(portfolio_std))
