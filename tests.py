from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_content

'''
print(f"Result for current directory:")
print(get_files_info("calculator", "."))

print(f"Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print(f"Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print(f"Result for '../' directory:")
print(get_files_info("calculator", "../"))
'''


print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))