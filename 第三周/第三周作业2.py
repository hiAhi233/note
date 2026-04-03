import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ====================== 用 pandas 直接读取鸢尾花数据集（最简洁方式） ======================
# 直接从网络加载鸢尾花CSV
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, names=names)

# 提取特征（只取数值列）
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y_true = df['class']  # 真实标签

print("数据集大小：", X.shape)


# ====================== K-Means 聚类算法 ======================
class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4, random_state=42):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol                  # 收敛阈值：中心变化很小就停止
        self.random_state = random_state
        self.centers = None
        self.labels = None

    def fit(self, X):
        X = X.values
        np.random.seed(self.random_state)

        # 初始化聚类中心
        idx = np.random.choice(len(X), self.n_clusters, replace=False)
        self.centers = X[idx]

        for _ in range(self.max_iter):
            # 计算距离
            dists = np.sqrt(((X - self.centers[:, np.newaxis]) ** 2).sum(axis=2))
            self.labels = np.argmin(dists, axis=0)

            # 更新中心
            new_centers = np.array([X[self.labels == i].mean(axis=0) for i in range(self.n_clusters)])

            # 收敛判断
            if np.linalg.norm(new_centers - self.centers) < self.tol:
                break
            self.centers = new_centers

        return self


# ====================== 训练模型 ======================
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# ====================== 结果输出 ======================
print("\n聚类中心：")
print(pd.DataFrame(kmeans.centers, columns=X.columns))

print("\n前10个样本聚类标签：")
print(kmeans.labels[:10])

