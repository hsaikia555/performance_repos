# __Author__ : Indu Sharma
# __Date__ : 14/03/2019
# __About__ : Utility to copy files to remote nodes or run commands on remote nodes


from fabric import operations
import global_constants


def create_fabric_command(command, hosts, username, password, command_timeout=None,
                          connection_timeout=global_constants.DEFAULT_CONNECTION_TIMEOUT):
    command = command.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$')  # Escaping the quotes
    fabric_command = "fab -D "
    if command_timeout is not None:
        fabric_command += "-T %s " % command_timeout

    fabric_command += " -t %s --abort-on-prompts -H %s -u %s -p %s -- \"%s\"" % (
        connection_timeout, hosts, username, password, command)
    return fabric_command


def run_command_with_remote_prompts(ip, username, password, command, prompts):
    set_fabric_environment(ip, username, password)
    operations.env.prompts = prompts
    with operations.settings(abort_on_prompts=False):
        return operations.run(command)


def run_command_with_sudo(ip, username, password, command, sudo_password=None):
    set_fabric_environment(ip, username, password, sudo_password=sudo_password)
    return operations.sudo(command)


def copy_file_to_remote(ip, username, password, local_path, remote_path, use_sudo=True, mirror_local_mode=True):
    set_fabric_environment(ip, username, password)
    return operations.put(local_path, remote_path, use_sudo, mirror_local_mode)


def set_fabric_environment(ip, username, password, sudo_password=None):
    operations.env.host_string = ip
    operations.env.user = username
    operations.env.password = password
    operations.env.sudo_password = sudo_password
    operations.env.warn_only = True
    operations.env.abort_on_prompts = True
    operations.env.disable_known_hosts = True
    operations.env.timeout = global_constants.DEFAULT_CONNECTION_TIMEOUT

