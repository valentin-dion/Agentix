from agentix import tool
import subprocess

@tool
def shell(command: str) -> str:
    """
    Executes a shell command and returns the result.

    Args:
        command (str): The command to execute in the shell.

    Returns:
        str: The output from the shell command.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout
