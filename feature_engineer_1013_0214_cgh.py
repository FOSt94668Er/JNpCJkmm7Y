# 代码生成时间: 2025-10-13 02:14:25
import pandas as pd

"""
特征工程工具，用于数据预处理和特征转换
"""

def load_data(file_path):
    """
    加载数据文件
    
    参数：
    file_path (str): 文件路径
    
    返回：
    pd.DataFrame: 包含数据的DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"加载数据失败：{e}")
        return None


def handle_missing_values(data):
    """
    处理缺失值
    
    参数：
    data (pd.DataFrame): 包含缺失值的DataFrame
    
    返回：
    pd.DataFrame: 处理缺失值后的DataFrame
    """
    if data is not None:
        # 填充缺失值
        data.fillna(data.mean(), inplace=True)
    return data


def encode_categorical_features(data):
    """
    对分类特征进行编码
    
    参数：
    data (pd.DataFrame): 包含分类特征的DataFrame
    
    返回：
    pd.DataFrame: 编码后的DataFrame
    """
    if data is not None:
        # 使用独热编码处理分类特征
        data = pd.get_dummies(data, drop_first=True)
    return data


def feature_scaling(data):
    """
    特征缩放
    
    参数：
    data (pd.DataFrame): 包含数值特征的DataFrame
    
    返回：
    pd.DataFrame: 缩放后的DataFrame
    """
    if data is not None:
        # 使用标准化处理数值特征
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        data = pd.DataFrame(data_scaled, columns=data.columns)
    return data


def main():
    """
    主函数，执行特征工程流程
    """
    # 加载数据
    file_path = 'data.csv'  # 假设数据文件名为data.csv
    data = load_data(file_path)
    
    # 处理缺失值
    data = handle_missing_values(data)
    
    # 对分类特征进行编码
    data = encode_categorical_features(data)
    
    # 特征缩放
    data = feature_scaling(data)
    
    # 保存处理后的数据
    data.to_csv('processed_data.csv', index=False)
    print('特征工程完成，处理后的数据已保存。')

if __name__ == '__main__':
    main()