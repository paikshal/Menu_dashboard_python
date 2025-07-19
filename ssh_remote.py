"""
SSH remote execution using Paramiko.
"""

import paramiko

def ssh_execute_command(host: str, username: str, command: str, password=None, key_file=None) -> str:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if key_file:
            key = paramiko.RSAKey.from_private_key_file(key_file)
            ssh.connect(hostname=host, username=username, pkey=key)
        else:
            ssh.connect(hostname=host, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        errors = stderr.read().decode()
        ssh.close()

        if errors:
            return f"Command executed with errors: {errors}"
        return output
    except Exception as e:
        return f"SSH connection failed: {str(e)}"