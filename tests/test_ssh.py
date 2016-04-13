import unittest
from unittest.mock import patch, mock_open, MagicMock

from scan_status import ScanStatus
from ssh import Ssh


class Test(unittest.TestCase):
    def test_scan_when_ok(self):
        # Prepare data and mocks
        test_subject = Ssh(None)
        test_subject.check_protocol = MagicMock(return_value=True)

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.check_protocol.assert_called_once_with('/etc/ssh/ssh_config')
        self.assertEqual(result[0], ScanStatus.success)

    def test_scan_when_failed(self):
        # Prepare data and mocks
        test_subject = Ssh(None)
        test_subject.check_protocol = MagicMock(return_value=False)

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.check_protocol.assert_called_once_with('/etc/ssh/ssh_config')
        self.assertEqual(result[0], ScanStatus.fail)

    def test_check_protocol_when_ok_no_protocol(self):
        # Prepare data and mocks
        with patch('builtins.open', mock_open(read_data='#	$OpenBSD: s\n\n# Host *\nSomeConfig')) as mock_file:
            test_subject = Ssh(None)

            # Run test scenario
            result = test_subject.check_protocol('/etc/ssh/ssh_config')

            # Assertions
            mock_file.assert_called_once_with('/etc/ssh/ssh_config')
            self.assertTrue(result)

    def test_check_protocol_when_ok_protocol_commented(self):
        # Prepare data and mocks
        with patch('builtins.open',
                   mock_open(read_data='#	$OpenBSD: s\n\n# Host *\nSomeConfig\n  # Protocol 1')) as mock_file:
            test_subject = Ssh(None)

            # Run test scenario
            result = test_subject.check_protocol('/etc/ssh/ssh_config')

            # Assertions
            mock_file.assert_called_once_with('/etc/ssh/ssh_config')
            self.assertTrue(result)

    def test_check_protocol_when_ok(self):
        # Prepare data and mocks
        with patch('builtins.open',
                   mock_open(read_data='#	$OpenBSD: s\n\n# Host *\nSomeConfig\n Protocol 2')) as mock_file:
            test_subject = Ssh(None)

            # Run test scenario
            result = test_subject.check_protocol('/etc/ssh/ssh_config')

            # Assertions
            mock_file.assert_called_once_with('/etc/ssh/ssh_config')
            self.assertTrue(result)

    def test_check_protocol_when_fail(self):
        # Prepare data and mocks
        with patch('builtins.open',
                   mock_open(read_data='#	$OpenBSD: s\n\n# Host *\nSomeConfig\n Protocol 1')) as mock_file:
            test_subject = Ssh(None)

            # Run test scenario
            result = test_subject.check_protocol('/etc/ssh/ssh_config')

            # Assertions
            mock_file.assert_called_once_with('/etc/ssh/ssh_config')
            self.assertFalse(result)

    def test_check_protocol_when_fail_fallback(self):
        # Prepare data and mocks
        with patch('builtins.open',
                   mock_open(read_data='#	$OpenBSD: s\n\n# Host *\nSomeConfig\n  Protocol 2, 1')) as mock_file:
            test_subject = Ssh(None)

            # Run test scenario
            result = test_subject.check_protocol('/etc/ssh/ssh_config')

            # Assertions
            mock_file.assert_called_once_with('/etc/ssh/ssh_config')
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
