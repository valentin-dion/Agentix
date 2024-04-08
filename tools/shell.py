import subprocess

def shell(command: str) -> str:
    """
    Executes a shell command and returns the output as a string.

    Args:
        command (str): The command to execute.

    Returns:
        str: The output from the command.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output, _ = process.communicate()
    if process.returncode == 0:
        return output
    else:
        return f"Error executing command. Return code: {process.returncode}\n{output}"
