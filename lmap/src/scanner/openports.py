from socket import SOCK_DGRAM
from socket import SOCK_STREAM

import psutil

from scanner.base_scanner import BaseScanner
from scanner.scan_status import ScanStatus


class OpenPorts(BaseScanner):
    def __init__(self, config):
        # config is a dictionary of this program's configuration
        self.config = config

    def scan(self):
        """
        :returns: a tuple of (ScanStatus, message).
        """
        output = 'Type, IP, Port, PID, Username, Thread Count, Command line\n'
        for connection in psutil.net_connections(kind='inet'):
            if self.is_port_is_open_and_externally_accessible(connection):
                output += self.get_line_for_connection(connection)
        return ScanStatus.success, output

    def get_line_for_connection(self, connection):
        """
        :returns: the single-line information about given connection. The line ends with a newline.
        """
        line = [
            self.get_connection_type_string(connection.type),
            str(connection.laddr[0]) + ':' + str(connection.laddr[1]),
            connection.pid,
        ]
        if connection.pid is not None:
            process = psutil.Process(connection.pid)
            line.append(process.username())
            line.append(' '.join(process.cmdline()))
        return ' '.join(str(i) for i in line)

    def is_port_is_open_and_externally_accessible(self, connection):
        # Checks whether given connection's port is open and externally accessible
        # Returns True if is, otherwise False
        if connection.type == SOCK_STREAM:
            return connection.status == 'LISTEN'
        if connection.type == SOCK_DGRAM:
            return True

    def get_connection_type_string(self, connection_type):
        # connection_type: socket.SOCK_STREAM or friends
        # Returns 'tcp' for socket.SOCK_STREAM, 'udp' for socket.SOCK_DGRAM
        # Raises ValueError if connection_type is anything else
        if connection_type == SOCK_DGRAM:
            return 'udp'
        elif connection_type == SOCK_STREAM:
            return 'tcp'
        else:
            raise ValueError('Unknown connection type: ', connection_type)
