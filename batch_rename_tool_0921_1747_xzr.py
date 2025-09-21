# 代码生成时间: 2025-09-21 17:47:37
import os
import pandas as pd
from pathlib import Path

"""
批量文件重命名工具
该程序可以读取包含原始文件列表和新文件名的Excel文件，并在指定目录下执行批量重命名。
"""


# 定义重命名函数
def rename_files(excel_path, directory_path):
    # 读取Excel文件
    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # 检查文件是否存在
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    # 遍历DataFrame中的文件名
    for index, row in df.iterrows():
        old_name = row['old_name']
        new_name = row['new_name']
        old_path = Path(directory_path) / old_name
        new_path = Path(directory_path) / new_name

        # 检查旧文件是否存在
        if not old_path.exists():
            print(f"File not found: {old_path}")
            continue

        # 重命名文件
        try:
            old_path.rename(new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
        except Exception as e:
            print(f"Error renaming file: {e}")


def main():
    # Excel文件路径
    excel_path = 'file_rename_list.xlsx'
    # 文件所在目录
    directory_path = '/path/to/directory'

    # 执行重命名操作
    rename_files(excel_path, directory_path)

if __name__ == '__main__':
    main()