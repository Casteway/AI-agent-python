import sys
import os

def get_files_info(working_directory, directory="."):
    abs_work_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(abs_work_dir, directory))

    if not abs_full_path.startswith(abs_work_dir):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(abs_full_path):
        return(f'Error: "{directory}" is not a directory')
    
    try:
        result = []
        listing = os.listdir(abs_full_path)

        for list in listing:
            item_path = os.path.join(abs_full_path,list)
            size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)
            result.append(f' - {list}: file_size = {size} bytes, is_dir={is_directory}')
        return "\n".join(result)
    except Exception as e:
        return(f'Error: something went bad {e}')