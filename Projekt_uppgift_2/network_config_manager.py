from netmiko import ConnectHandler

class NetworkConfigManager:
    """
    Hanterar nätverkskonfigurationer via SSH på en Linux-server i Docker.
    """
    def __init__(self, host="localhost", port=2222, username="admin", password="password"):
        """
        Initierar SSH-anslutningen till servern.
        """
        self.device = {
            "device_type": "linux",
            "host": host,
            "port": port,
            "username": username,
            "password": password
        }
        self.ssh = None

    def connect(self):
        """ Upprättar en SSH-anslutning till servern. """
        self.ssh = ConnectHandler(**self.device)

    def disconnect(self):
        """ Stänger SSH-anslutningen. """
        if self.ssh:
            self.ssh.disconnect()

    def update_hostname(self, hostname):
        """ Uppdaterar värdet för hostname på servern. """
        cmd = f'echo "hostname: {hostname}" > /etc/config/hostname/config.txt'
        self.ssh.send_command(cmd)

    def update_interface_state(self, state):
        """ Uppdaterar interfacets status (endast 'up' eller 'down' är tillåtna). """
        if state not in ["up", "down"]:
            raise ValueError("Endast 'up' eller 'down' är tillåtna värden.")
        cmd = f'echo "interface_state: {state}" > /etc/config/interface/config.txt'
        self.ssh.send_command(cmd)

    def update_response_prefix(self, prefix):
        """ Uppdaterar response_prefix på servern. """
        cmd = f'echo "response_prefix: {prefix}" > /etc/config/response/config.txt'
        self.ssh.send_command(cmd)

    def show_host_name(self):
        """ Hämtar nuvarande hostname. """
        return self.ssh.send_command("cat /etc/config/hostname/config.txt").strip()

    def show_interface_state(self):
        """ Hämtar nuvarande interface_state. """
        return self.ssh.send_command("cat /etc/config/interface/config.txt").strip()

    def show_response_prefix(self):
        """ Hämtar nuvarande response_prefix. """
        return self.ssh.send_command("cat /etc/config/response/config.txt").strip()
