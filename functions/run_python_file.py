import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_work_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(abs_work_dir, file_path))

    if not abs_full_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ["python", abs_full_path] + args
        completed_process = subprocess.run(cmd, timeout=30, capture_output = True, text = True, cwd = abs_work_dir)

        output_lines = []

        if completed_process.stdout:
            output_lines.append(f"STDOUT:\n{completed_process.stdout}")

        if completed_process.stderr:
            output_lines.append(f"STDERR:\n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output_lines.append(f"Process exited with code {completed_process.returncode}")

        return "\n".join(output_lines) if output_lines else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"