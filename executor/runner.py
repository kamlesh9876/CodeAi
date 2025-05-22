# executor/runner.py

import subprocess

def run_code(file_path="main_output.py"):
    """
    Executes the specified Python file and returns output or errors.

    Parameters:
        file_path (str): Path to the Python file to execute.

    Returns:
        str: Standard output or error message from execution.
    """
    try:
        result = subprocess.run(
            ["python3", file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout or "[Run] Completed with no output."
        else:
            return f"[Run Error] {result.stderr}"
    except subprocess.TimeoutExpired:
        return "[Run Error] Execution timed out."
    except Exception as e:
        return f"[Run Error] {e}"
