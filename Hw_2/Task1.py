import platform
import sys

os_name = platform.system()
py_version = sys.version.replace('\n', '')

with open('os_info.txt', 'w', encoding='utf-8') as file:
    file.write(f"OS info is {os_name} Python version is {py_version}")


print(f"OS info is {os_name} Python version is {py_version}")