import os
import stat
import re

from base_scanner import BaseScanner
from scan_status import ScanStatus


class Ssh(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        """
        Checks whether the system SSHd daemon configuration file is secure or not..
        :returns: a tuple of (ScanStatus, message).
        """
        if self.check_protocol('/etc/ssh/ssh_config'):
            return ScanStatus.success, ''
        else:
            return ScanStatus.fail, 'The vulnerable SSHv1 is enabled in /etc/ssh/ssh_config'

    def check_protocol(self, sshd_config_path):
        """
        Checks SSHd service's configuration file - whether the vulnerable v1 protocol is enabled.
        :param sshd_config_path: the SSHd service's configuration file location, usually /etc/ssh/ssh_config.
        :returns: True if no protocol is selected or the default protocol 2 is selected.
        :returns: False if protocol 1 is selected or is selected as fallback.
        """
        is_comment_line = re.compile('^\s*#')
        with open(sshd_config_path) as config_file:
            for line in config_file.readlines():
                if not is_comment_line.match(line):
                    if line.split() and line.split()[0] == 'Protocol' and '1' in ''.join(line.split()[1:]):
                        return False
        return True
