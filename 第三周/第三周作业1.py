import numpy as np
import pandas as pd

# 手动下载并加载数据集

def load_wine_data():
    url = "winequality-red.csv"
    # 读取后加 .values，直接变成 numpy 数组
    data = pd.read_csv(url, sep=';').values

    X = data[:, :-1]  # 特征
    y = data[:, -1]  # 质量分数
    return X, y


# 二分类标签：>6 为好酒
def binary_label(y):
    return (y > 6).astype(int)



# 手动划分训练集/测试集
def train_test_split(X, y, test_ratio=0.3, seed=42):
    np.random.seed(seed)
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    test_size = int(len(X) * test_ratio)

    test_idx = indices[:test_size]
    train_idx = indices[test_size:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


# 手动标准化（Z-score）

def standardize(X_train, X_test):
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    std[std == 0] = 1  # 避免除0
    return (X_train - mean) / std, (X_test - mean) / std


# 线性回归（最小二乘法 解析解）
class LinearRegression:
    def fit(self, X, y):
        X = np.c_[np.ones(len(X)), X]  # 加截距
        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X):
        X = np.c_[np.ones(len(X)), X]
        return X @ self.beta


# 评估指标
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


# 逻辑回归（梯度下降）
class LogisticRegression:
    def __init__(self, lr=0.5, epochs=30000):
        self.lr = lr
        self.epochs = epochs

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        X = np.c_[np.ones(len(X)), X]
        self.beta = np.zeros(X.shape[1])

        for _ in range(self.epochs):
            y_pred = self.sigmoid(X @ self.beta)
            grad = X.T @ (y_pred - y) / len(y)
            self.beta -= self.lr * grad

    def predict_proba(self, X):
        X = np.c_[np.ones(len(X)), X]
        return self.sigmoid(X @ self.beta)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


# 分类评估
def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)


def classification_metrics(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    return precision, recall, f1

# 主程序运行
if __name__ == "__main__":
    X, y = load_wine_data()
    y_cls = binary_label(y)

    # 回归任务
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    X_train, X_test = standardize(X_train, X_test)

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)

    print("===== 线性回归结果 =====")
    print(f"MSE: {mse(y_test, y_pred):.4f}")
    print(f"RMSE: {np.sqrt(mse(y_test, y_pred)):.4f}")
    print(f"R²: {r2(y_test, y_pred):.4f}\n")

    # 分类任务
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_cls)
    X_train_c, X_test_c = standardize(X_train_c, X_test_c)

    log_reg = LogisticRegression()
    log_reg.fit(X_train_c, y_train_c)
    y_pred_c = log_reg.predict(X_test_c)

    precision, recall, f1 = classification_metrics(y_test_c, y_pred_c)

    print("===== 逻辑回归结果 =====")
    print(f"准确率: {accuracy(y_test_c, y_pred_c):.4f}")
    print(f"精确率: {precision:.4f}")
    print(f"召回率: {recall:.4f}")
    print(f"F1分数: {f1:.4f}")