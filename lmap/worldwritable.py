import os
import stat

from base_scanner import BaseScanner
from scan_status import ScanStatus


class WorldWritable(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        # Scans the file system for world writable files and directories with permission anomalies
        worldwritable_files_starting_with_dot = self.scan_worldwritable_files_starting_with_dot()
        worldwritable_directories_with_no_sticky_bit_set = self.scan_worldwritable_directories_with_no_sticky_bit_set()
        worldwritable_files_owned_by_root = self.scan_worldwritable_files_owned_by_root()
        if not worldwritable_files_starting_with_dot and \
                not worldwritable_directories_with_no_sticky_bit_set and \
                not worldwritable_files_owned_by_root:
            scan_status = ScanStatus.success
            message = ''
        else:
            scan_status = ScanStatus.fail
            message_parts = []
            if worldwritable_files_starting_with_dot:
                message_parts.append(self.get_scan_text('World writable files starting with dot',
                                                        worldwritable_files_starting_with_dot))
            if worldwritable_directories_with_no_sticky_bit_set:
                message_parts.append(self.get_scan_text('World writable directories with no sticky bit set',
                                                        worldwritable_directories_with_no_sticky_bit_set))
            if worldwritable_files_owned_by_root:
                message_parts.append(self.get_scan_text('World writable files owned by root',
                                                        worldwritable_files_owned_by_root))
            message = '\n'.join(message_parts)
        return scan_status, message

    def get_scan_text(self, check_name, locations):
        # Generates a formatted string for given check's name and file locations
        if locations:
            return 'Failure: ' + check_name + ':\n\t' + '\n\t'.join(locations)
        else:
            return 'Success: ' + check_name

    def scan_worldwritable_directories_with_no_sticky_bit_set(self):
        # Searches for worldwritable directories in the system which do not have the sticky bit set
        # Returns a list of such directories
        result = []
        for directory, subdirectories, files in os.walk('/'):
            if self.is_world_writable(directory) and not self.is_sticky_bit_set(directory):
                result.append(directory)
        return result

    def scan_worldwritable_files_starting_with_dot(self):
        # Searches for worldwritable files in the system whose name starts with dot
        # Returns a list of such files
        result = []
        for directory, subdirectories, files in os.walk('/'):
            for file in files:
                if self.is_world_writable(file) and self.is_starts_with_dot(file):
                    result.append(file)
        return result

    def scan_worldwritable_files_owned_by_root(self):
        # Searches for worldwritable files in the system which are owned by root
        # Returns a list of such files
        result = []
        for directory, subdirectories, files in os.walk('/'):
            for file in files:
                if self.is_world_writable(file) and self.is_owned_by_root(file):
                    result.append(file)
        return result

    def is_world_writable(self, path):
        # Checks whether the file or directory at given path is world writable
        # Only the "Others" number in permission triple is checked for the presence of "Writeable" bit
        # Returns true if is world writable, false otherwise
        # Returns false if the file is not found
        try:
            file_statistics = os.stat(path)
        except FileNotFoundError:
            return False
        return bool(file_statistics.st_mode & stat.S_IWOTH)

    def is_sticky_bit_set(self, path):
        # Checks whether the file or directory at given path has sticky bit set
        # Returns true if is set, false otherwise
        # Returns false if the file is not found
        try:
            file_statistics = os.stat(path)
        except FileNotFoundError:
            return False
        return bool(file_statistics.st_mode & stat.S_ISVTX)

    def is_owned_by_root(self, path):
        # Checks whether the file or directory at given path is owned by the root user
        # A root user has UID of 0
        # Returns true if is owned by root, false otherwise
        # Returns false if the file is not found
        try:
            file_statistics = os.stat(path)
        except FileNotFoundError:
            return False
        return file_statistics.st_uid == 0

    def is_starts_with_dot(self, path):
        # Checks whether name of the file or directory at given path starts with dot
        # Returns true if does, false otherwise
        # Returns false if the file is not found
        basename = os.path.basename(path)
        if not basename:
            return False
        return basename[0] == '.'
