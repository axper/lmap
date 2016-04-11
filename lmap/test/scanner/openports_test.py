import unittest
from socket import SOCK_DGRAM, SOCK_STREAM
from unittest.mock import MagicMock, call

from scanner.openports import OpenPorts
from scanner.scan_status import ScanStatus


def raise_file_not_found_error(x):
    raise FileNotFoundError


class Test(unittest.TestCase):
    @unittest.mock.patch('scanner.openports.psutil')
    def test_scan(self, mock_psutil):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        mock_psutil.net_connections = MagicMock(return_value=['closed connection', 'open connection'])
        test_subject.is_port_is_open_and_externally_accessible = MagicMock(side_effect=[False, True])
        test_subject.get_line_for_connection = MagicMock(return_value='open connection line')

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        self.assertEquals(result[0], ScanStatus.success)
        self.assertIsNotNone(result[1])
        mock_psutil.net_connections.assert_called_once_with(kind='inet')
        test_subject.is_port_is_open_and_externally_accessible.assert_has_calls(
            [
                call('closed connection'),
                call('open connection')
            ]
        )
        test_subject.get_line_for_connection.assert_called_once_with('open connection')

    def test_port_is_open_and_externally_accessible_when_udp(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        connection = MagicMock()
        connection.type = SOCK_DGRAM

        # Run test scenario
        result = test_subject.is_port_is_open_and_externally_accessible(connection)

        # Assertions
        self.assertTrue(result)

    def test_port_is_open_and_externally_accessible_when_tcp_and_connection_status_is_listen(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        connection = MagicMock()
        connection.type = SOCK_STREAM
        connection.status = 'LISTEN'

        # Run test scenario
        result = test_subject.is_port_is_open_and_externally_accessible(connection)

        # Assertions
        self.assertTrue(result)

    def test_port_is_open_and_externally_accessible_when_tcp_and_connection_status_is_not_listen(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        connection = MagicMock()
        connection.type = SOCK_STREAM
        connection.status = 'Not LISTEN'

        # Run test scenario
        result = test_subject.is_port_is_open_and_externally_accessible(connection)

        # Assertions
        self.assertFalse(result)

    def test_get_connection_type_string_when_tcp(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)

        # Run test scenario
        result = test_subject.get_connection_type_string(SOCK_STREAM)

        # Assertions
        self.assertEqual(result, 'tcp')

    def test_get_connection_type_string_when_udp(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)

        # Run test scenario
        result = test_subject.get_connection_type_string(SOCK_DGRAM)

        # Assertions
        self.assertEqual(result, 'udp')

    def test_get_connection_type_string_when_other(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)

        # Run test scenario
        with self.assertRaises(ValueError):
            test_subject.get_connection_type_string(None)

            # Assertions

    def test_get_line_for_connection_when_unknown_pid(self):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        connection = MagicMock()
        connection.type = SOCK_DGRAM
        connection.laddr = ('127.0.0.1', 80)
        connection.pid = None
        test_subject.get_connection_type_string = MagicMock(return_value='udp')

        # Run test scenario
        result = test_subject.get_line_for_connection(connection)

        # Assertions
        self.assertEquals('udp 127.0.0.1:80 None', result)

    @unittest.mock.patch('scanner.openports.psutil')
    def test_get_line_for_connection_when_known_pid(self, mock_psutil):
        # Prepare data and mocks
        test_subject = OpenPorts(None)
        connection = MagicMock()
        connection.type = SOCK_DGRAM
        connection.laddr = ('127.0.0.1', 80)
        connection.pid = 300
        process = MagicMock()
        process.username = MagicMock(return_value='Babken')
        process.cmdline = MagicMock(return_value=['ls', '-l', '-a'])
        test_subject.get_connection_type_string = MagicMock(return_value='udp')
        mock_psutil.Process = MagicMock(return_value=process)

        # Run test scenario
        result = test_subject.get_line_for_connection(connection)

        # Assertions
        self.assertEquals('udp 127.0.0.1:80 300 Babken ls -l -a', result)
        mock_psutil.Process.assert_called_once_with(connection.pid)


if __name__ == '__main__':
    unittest.main()
