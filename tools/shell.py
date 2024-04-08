import subprocess

def shell(command: str):
    """
    Executes a shell command and prints the output in real-time.

    Args:
        command (str): The command to execute.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    process.stdout.close()
    return_code = process.wait()
    return return_code
