import paramiko
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ssh_run_command(host, username, password, command, port=22):
    """
    Connects to a remote host via SSH and runs a command. Returns the command output or None on error.
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password, port=port, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        client.close()
        if error:
            logger.error(f"Error running command on {host}: {error}")
            return None
        return output
    except Exception as e:
        logger.error(f"SSH error while connecting to {host}: {e}")
        return None

def run_command_on_linux(ip, username, key_path, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Clean up inputs
        key_path = key_path.strip() if key_path else ""
        password = password.strip() if password else ""
        
        if password:
            # Use password authentication
            ssh.connect(hostname=ip, username=username, password=password, timeout=10)
        elif key_path:
            # Use key file authentication
            if not os.path.exists(key_path):
                return "", f"Error: Key file not found at {key_path}"
            try:
                key = paramiko.RSAKey.from_private_key_file(key_path)
            except paramiko.SSHException:
                try:
                    key = paramiko.Ed25519Key.from_private_key_file(key_path)
                except Exception as e:
                    return "", f"Error: Invalid key file format: {str(e)}"
            ssh.connect(hostname=ip, username=username, pkey=key, timeout=10)
        else:
            return "", "Error: Either password or key file must be provided"

        stdin, stdout, stderr = ssh.exec_command(command)
        out = stdout.read().decode()
        err = stderr.read().decode()
        ssh.close()

        return out, err

    except Exception as e:
        return "", f"Error: {str(e)}"

def run_multiple_commands_on_linux(ip, username, key_path, password, commands):
    """
    Executes up to 50 commands on a remote Linux server via SSH.
    Returns a list of (command, output, error) tuples.
    """
    if not isinstance(commands, list):
        return [(None, '', 'Error: commands must be a list')]
    if len(commands) > 50:
        return [(None, '', 'Error: Too many commands (max 50 allowed)')]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    results = []

    try:
        # Clean up inputs
        key_path = key_path.strip() if key_path else ""
        password = password.strip() if password else ""
        
        if password:
            # Use password authentication
            ssh.connect(hostname=ip, username=username, password=password, timeout=10)
        elif key_path:
            # Use key file authentication
            if not os.path.exists(key_path):
                return [(None, '', f"Error: Key file not found at {key_path}")]
            try:
                key = paramiko.RSAKey.from_private_key_file(key_path)
            except paramiko.SSHException:
                try:
                    key = paramiko.Ed25519Key.from_private_key_file(key_path)
                except Exception as e:
                    return [(None, '', f"Error: Invalid key file format: {str(e)}")]
            ssh.connect(hostname=ip, username=username, pkey=key, timeout=10)
        else:
            return [(None, '', "Error: Either password or key file must be provided")]

        for cmd in commands:
            try:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                out = stdout.read().decode()
                err = stderr.read().decode()
                results.append((cmd, out, err))
            except Exception as e:
                results.append((cmd, '', f'Error: {str(e)}'))
        ssh.close()
        return results
    except Exception as e:
        return [(None, '', f'Error: {str(e)}')] 