import os

from base_scanner import BaseScanner
from scan_status import ScanStatus


class Root(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        """
        Checks whether the user running this program is the root user with UID of 0.
        Takes into account the usage of the program sudo.
        :returns: a tuple of (ScanStatus, message).
        """
        if os.getuid() == 0:
            if os.environ.get('SUDO_UID'):
                return ScanStatus.success, ''
            else:
                return ScanStatus.fail, 'Do not use the root user account'
        else:
            return ScanStatus.success, ''
