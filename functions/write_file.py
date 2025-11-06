import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_work_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(abs_work_dir, file_path))

    if not abs_full_path.startswith(abs_work_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_full_path):
        try:
            os.makedirs(os.path.dirname(abs_full_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
        
    if os.path.exists(abs_full_path) and os.path.isdir(abs_full_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_full_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)