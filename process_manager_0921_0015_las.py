# 代码生成时间: 2025-09-21 00:15:46
import pandas as pd
import psutil
import subprocess
from tabulate import tabulate

"""
Process Manager
=============

A simple Python script to manage system processes using the psutil library.

Features:
- List all running processes
- Kill a specific process
- Provide detailed information about a process

Usage:
- Run the script and follow the menu-driven interface
"""


class ProcessManager:
    def __init__(self):
        self.processes = self.get_all_processes()

    def get_all_processes(self):
        """Retrieve a list of all running processes."""
        return {proc.pid: proc for proc in psutil.process_iter(['pid', 'name', 'username'])}

    def list_processes(self):
        """Display a list of all running processes."""
        print(tabulate(self.processes.items(), headers=['PID', 'Name', 'Username'], tablefmt='psql'))

    def kill_process(self, pid):
        """Kill a process by its PID."""
        if pid in self.processes:
            try:
                self.processes[pid].kill()
                print(f"Process {pid} killed successfully.")
            except psutil.NoSuchProcess:
                print(f"Process {pid} not found.")
            except psutil.AccessDenied:
                print(f"Permission denied to kill process {pid}.")
            finally:
                self.processes = self.get_all_processes()
        else:
            print(f"No process found with PID {pid}.")

    def get_process_info(self, pid):
        """Retrieve detailed information about a process."""
        if pid in self.processes:
            process = self.processes[pid]
            info = {
                'PID': process.pid,
                'Name': process.name(),
                'Username': process.username(),
                'Status': process.status(),
                'Created': process.create_time(),
                'Memory Usage': process.memory_info().rss / (1024 * 1024),  # Convert to MB
                'CPU Usage': process.cpu_percent(interval=1),
            }
            print(tabulate([info], headers='keys', tablefmt='psql'))
        else:
            print(f"No process found with PID {pid}.")

    def run(self):
        """Main menu-driven interface."""
        while True:
            self.list_processes()
            choice = input("Choose an option: 1) Kill a process 2) Get process info 3) Exit: ")
            if choice == '1':
                pid = int(input("Enter the PID of the process to kill: "))
                self.kill_process(pid)
            elif choice == '2':
                pid = int(input("Enter the PID of the process to get info: "))
                self.get_process_info(pid)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    manager = ProcessManager()
    manager.run()