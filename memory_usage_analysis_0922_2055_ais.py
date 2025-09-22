# 代码生成时间: 2025-09-22 20:55:08
import psutil
import pandas as pd

"""
This program analyzes the memory usage of the system and outputs it in a Pandas DataFrame.
It provides a clear structure, includes error handling, and is well-documented.

The program follows Python best practices, ensuring maintainability and scalability."""


def get_memory_usage():
    """
    Retrieves the system's memory usage and returns it as a Pandas DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing memory usage information.
    """
    try:
        # Get the current memory usage
        memory = psutil.virtual_memory()
        
        # Create a dictionary to hold the memory usage data
        memory_data = {
            'Total Memory (MB)': memory.total / (1024 * 1024),
            'Available Memory (MB)': memory.available / (1024 * 1024),
            'Used Memory (MB)': memory.used / (1024 * 1024),
            'Memory Usage (%)': memory.percent,
            'Free Memory (MB)': memory.free / (1024 * 1024),
            'Active Memory (MB)': memory.active / (1024 * 1024),
            'Inactive Memory (MB)': memory.inactive / (1024 * 1024),
            'Wired Memory (MB)': memory. wired / (1024 * 1024)
        }
        
        # Convert the dictionary to a Pandas DataFrame
        memory_df = pd.DataFrame(memory_data, index=[0])
        
        return memory_df
    
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == '__main__':
    memory_df = get_memory_usage()
    if memory_df is not None:
        print(memory_df)