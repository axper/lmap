import os
import stat

from base_scanner import BaseScanner
from scan_status import ScanStatus


class Umask(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        """
        Checks whether current user's umask value is secure.
        Only the last digit of the umask is checked (the Others digit).
        If the Others digit's write bit is set, the check fails.
        Otherwise the check succeeds.
        :returns: a tuple of (ScanStatus, message).
        """
        umask = self.get_umask_without_change()
        if umask & stat.S_IWOTH:
            return ScanStatus.success, ''
        else:
            return ScanStatus.fail, 'Current user\'s umask gives write permissions OTHERS group by default'

    def get_umask_without_change(self):
        """
        Gets current user's umask value without changing it.
        :returns: an integer of current user's umask.
        """
        current_umask = os.umask(0o0777)
        os.umask(current_umask)
        return current_umask
