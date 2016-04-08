import os
import platform
import re
from datetime import datetime, timedelta

from src.scanner.base_scanner import BaseScanner
from src.scanner.scan_status import ScanStatus


class Update(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        distribution_name = platform.linux_distribution()[0]
        if distribution_name == 'arch':
            return self.scan_arch()
        elif distribution_name == 'debian':
            return self.scan_debian()
        elif distribution_name == 'redhat':
            return self.scan_redhat()
        else:
            return ScanStatus.unknown, ''

    def scan_arch(self):
        # Scans the pacman log file, and checks whether the last system update date is older than required
        # Returns a tuple: (ScanStatus, message)
        config_update_interval_days = int(self.config['update']['warn_last_update_interval_days'])
        with open('/var/log/pacman.log') as f:
            last_update_date = self.get_pacman_last_update_date(f.readlines())
            if last_update_date is None:
                return ScanStatus.unknown, ''
            elif datetime.today() - last_update_date < timedelta(days=config_update_interval_days):
                return ScanStatus.success, ''
            else:
                return ScanStatus.fail, ''

    def get_pacman_last_update_date(self, contents):
        # contents: list of lines of pacman.log
        # Returns the datetime instance of last update date or None if last update date is not found
        for line in reversed(contents):
            if 'starting full system upgrade' in line:
                match_date = re.search('\[(.*?)\]', line)
                if match_date:
                    last_update_date_string = match_date.group(1)
                    return datetime.strptime(last_update_date_string, '%Y-%m-%d %H:%M')

    def scan_debian(self):
        # Scans update-success-stamp file's creation date and checks whether it's older than the last system update date
        # Returns a tuple: (ScanStatus, message)
        config_update_interval_days = int(self.config['update']['warn_last_update_interval_days'])
        last_update_date = self.get_apt_last_update_date('/var/lib/apt/periodic/update-success-stamp')
        if last_update_date is None:
            return ScanStatus.unknown, ''
        elif datetime.today() - last_update_date < timedelta(days=config_update_interval_days):
            return ScanStatus.success, ''
        else:
            return ScanStatus.fail, ''

    def get_apt_last_update_date(self, update_success_stamp_file_location):
        # update_success_stamp_file_location: usually `/var/lib/apt/periodic/update-success-stamp`
        # Returns the datetime instance of last update date or None if last update date is not found
        try:
            file_modification_epoch = os.path.getmtime(update_success_stamp_file_location)
        except FileNotFoundError:
            return None
        return datetime.fromtimestamp(file_modification_epoch)

    def scan_redhat(self):
        # Not implemented, returns (ScanStatus.unknown, '')
        # Returns a tuple: (ScanStatus, message)
        return ScanStatus.unknown, ''
