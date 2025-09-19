# 代码生成时间: 2025-09-19 14:39:42
import os
import shutil
import pandas as pd
from datetime import datetime

"""
文件备份和同步工具
"""

# 定义全局变量
source_folder = "source/"  # 源文件夹路径
backup_folder = "backup/"  # 备份文件夹路径


def create_folder(folder_path):
    """创建文件夹，如果不存在的话"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")


def backup_files():
    """备份源文件夹中的文件到备份文件夹"""
    try:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            backup_path = os.path.join(backup_folder, filename)
            # 创建备份文件夹
            create_folder(backup_folder)
            # 复制文件
            shutil.copy2(file_path, backup_path)
            print(f"Backup: {file_path} -> {backup_path}")
    except Exception as e:
        print(f"Error during backup: {e}")


def sync_files():
    """同步备份文件夹中的文件到源文件夹"""
    try:
        for filename in os.listdir(backup_folder):
            file_path = os.path.join(backup_folder, filename)
            source_path = os.path.join(source_folder, filename)
            # 复制文件
            shutil.copy2(file_path, source_path)
            print(f"Sync: {file_path} -> {source_path}")
    except Exception as e:
        print(f"Error during sync: {e}")


def list_files(folder_path):
    """列出文件夹中的文件"""
    try:
        files = os.listdir(folder_path)
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []


def get_file_sizes(folder_path):
    """获取文件夹中文件的大小"""
    file_sizes = []
    for filename in list_files(folder_path):
        file_path = os.path.join(folder_path, filename)
        file_size = os.path.getsize(file_path)
        file_sizes.append((filename, file_size))
    return file_sizes


def save_file_sizes_to_csv(folder_path, csv_file):
    """将文件夹中文件的大小保存到CSV文件"""
    file_sizes = pd.DataFrame(get_file_sizes(folder_path), columns=["Filename", "Size"])
    file_sizes.to_csv(csv_file, index=False)
    print(f"Saved file sizes to CSV: {csv_file}")


def main():
    """主函数"""
    # 创建源文件夹和备份文件夹
    create_folder(source_folder)
    create_folder(backup_folder)

    # 备份文件
    backup_files()

    # 同步文件
    sync_files()

    # 将源文件夹和备份文件夹的文件大小保存到CSV文件
    save_file_sizes_to_csv(source_folder, "source_file_sizes.csv")
    save_file_sizes_to_csv(backup_folder, "backup_file_sizes.csv")

if __name__ == "__main__":
    main()