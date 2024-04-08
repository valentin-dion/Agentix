from agentix import tool
import subprocess

@tool
def shell(command: str) -> str:
    """
    Executes a shell command and prints the output in real-time.

    Args:
        command (str): The command to execute in the shell.

    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout
