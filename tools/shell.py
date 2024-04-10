import subprocess
from agentix import tool

@tool
def shell(command: str) -> str:
    """
    Executes a shell command, streams the output in real-time, and returns the output as a string.

    Args:
        command (str): The command to execute.

    Returns:
        str: The output from the command.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output_lines = []
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
        output_lines.append(line)
    process.stdout.close()
    return_code = process.wait()
    
    return ''.join(output_lines) if return_code == 0 else f"Error executing command. Return code: {return_code}\n{''.join(output_lines)}"
