import unittest
from unittest.mock import patch, MagicMock

from scanner.root import Root
from scanner.scan_status import ScanStatus


class Test(unittest.TestCase):
    @unittest.mock.patch('scanner.root.os')
    def test_scan_when_getuid_is_other(self, mock_os):
        # Prepare data and mocks
        mock_os.getuid = MagicMock(return_value=1000)

        # Run test scenario
        result = Root(None).scan()

        # Assertions
        mock_os.getuid.assert_called_once_with()
        self.assertEquals(result[0], ScanStatus.success)

    @unittest.mock.patch('scanner.root.os')
    def test_scan_when_getuid_is_0_and_environ_sudo_uid_is_set(self, mock_os):
        # Prepare data and mocks
        mock_os.getuid = MagicMock(return_value=0)
        mock_os.environ.get = MagicMock(return_value=1000)

        # Run test scenario
        result = Root(None).scan()

        # Assertions
        mock_os.getuid.assert_called_once_with()
        mock_os.environ.get.assert_called_once_with('SUDO_UID')
        self.assertEquals(result[0], ScanStatus.success)

    @unittest.mock.patch('scanner.root.os')
    def test_scan_when_getuid_is_0_and_environ_sudo_uid_is_not_set(self, mock_os):
        # Prepare data and mocks
        mock_os.getuid = MagicMock(return_value=0)
        mock_os.environ.get = MagicMock(return_value=None)

        # Run test scenario
        result = Root(None).scan()

        # Assertions
        mock_os.getuid.assert_called_once_with()
        mock_os.environ.get.assert_called_once_with('SUDO_UID')
        self.assertEquals(result[0], ScanStatus.fail)


if __name__ == '__main__':
    unittest.main()
