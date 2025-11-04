import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_work_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(abs_work_dir, file_path))

    if not abs_full_path.startswith(abs_work_dir):
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_full_path):
        return(f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        with open(abs_full_path, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                truncation_string = file_content_string[:MAX_CHARS]
                return f'{truncation_string}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            else:
                return file_content_string
    except Exception as e:
        return(f'Error: something went bad {e}')