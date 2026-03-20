# Numpy库

​		NumPy(Numerical Python),是Python的一个科学计算库,主要用于处理大规模的数组和矩阵数据,以及对这些数据执行各种数学运算。它为Python提供了大量高效的数学函数库,可以用于数值计算和数据分析。

读取文件：

```python
# 对 txt, csv 的文本文件读写
np.savetxt('array.csv', arr, delimiter=',')
np.loadtxt('array.csv', delimiter=',')

# 对 npy 的二进制文件读写
np.save('array.npy', arr)
np.load('array.npy')
```



ndarray:

```python
import numpy as np
arr1 = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(arr1)
print("数组的 shape（形状）：", arr1.shape)
print("数组的 dtype（数据类型）：", arr1.dtype)
print("数组的 ndim（维度数）：", arr1.ndim)
arr_flat = arr1.flatten()
print("展平后的一维数组（flatten()）：", arr_flat)
arr2 = np.zeros((3, 4), dtype=int) #创建二维全0数组（3行4列），指定为整数类型
# 水平拼接（axis=1）垂直拼接 （axis=0）
result_h = np.concatenate((arr1, arr2), axis=1)
```



向量：

```
np.linalg.norm()    #计算向量的模
np.dot()				#计算向量点积
```

数值：

```		
np.random.random()	#生成（0,1）的随机浮点数
np.random.randint(low=1, high=20, size=(3, 4))	#生成[1,20)的随机整数
```







# Pandas库

​      Pandas(衍生自术语“panel data")，是一个高性能、易用的数据分析包,提供了易于使用的数据结构和数据分析工具,特别适合处理表格型数据(如Excel表格、数据库表等)。

## 一、一维数据结构Series

Series：具有索引的一维数组的结构，每个数据项都可以通过标签访问。

```python
import pandas as pd
#从列表中创建
s1 = pd.Series([1,2,3], index=['a','b','c'])
#从字典中创建
s2 = pd.Series({'a':1,'b':2,'c':3})
print(s1)
print(s2)
print("s1['a']:",s1['a'])
print("s2['b']:",s2['b'])
```





## 二、二维数据结构DataFrame


DataFrame:一个二维表格型的数据结构。可以将它理解为一个表格,每一行和每一列都有自己的标签(索引和列名)

①创建表格

```python
import pandas as pd

# 从列表（数组）创建
data1 = [
    [1, 'Alice', 24, 'New York'],
    [2, 'Bob', 27, 'Los Angeles'],
    [3, 'Charlie', 22, 'Chicago'],
    [4, 'David', 3, 'Houston']
]

# 从字典创建
data2 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 3],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df1 = pd.DataFrame(data1, columns=['ID', 'Name', 'Age', 'City'])
df2 = pd.DataFrame(data2)

print(df1)
```

②常用操作

文件读写:分为csv和Excel文件两种

```python
# csv
df = pd.read_csv('sample_data.csv', sep=',')
df.to_csv('output.csv', index=False)
# Excel
df = pd.read_excel('sample_data.xlsx')
df.to_excel('output.xlsx')
```

修改：inplace = True,替换；inplace = False,须一个承载

```python
df.drop('column1', axis=1, inplace=True)
```

查看DataFrame的数据信息:

```
# 多行/列索引
df.loc[2:4,'column1'] #假设行标签是2到4,选择column1
df.iloc[2:4,7] # 2到3行,选择第8列

# 条件索引
df[df['column1']> 10] #列值大于10的行
df[(df['age'] >30) & (df['score']>300)]
```

常用操作：

```python
df.apply(lambda x: x*2,axis=1)#axis=0按列处理,axis=1 按行处理
df.dropna()#删除有缺失值的行
df.drop(‘总成绩',axis=1)#删除一列
df.fillna(0)#将缺失值填充为0
df.sort_values(by='score',ascending:True)#按score升序排行
```



# JSON库

Json是一种文本数据格式，是轻量级的文本数据交换格式，来源于javascript的对象语法。Json可以简单灵活地表示树形结构的数据

Json标准库的作用：

​		1.使用json字符串生成python对象（load）

​		2.由python对象格式化成为json字符串（dump）

数据类型转换：

| JSON 类型     | Python 类型 |
| ------------- | ----------- |
| object        | dict        |
| array         | list，tuple |
| string        | str         |
| number (int)  | int         |
| number (real) | float       |
| true          | True        |
| false         | False       |
| null          | None        |

使用方法：

| 方法                 | 功能                                                 |
| -------------------- | ---------------------------------------------------- |
| `json.dump(obj, fp)` | 将 Python 数据类型转换并保存到 JSON 格式的文件内。   |
| `json.dumps(obj)`    | 将 Python 数据类型转换为 JSON 格式的字符串。         |
| `json.load(fp)`      | 从 JSON 格式的文件中读取数据并转换为 Python 的类型。 |
| `json.loads(s)`      | 将 JSON 格式的字符串转换为 Python 的类型。           |