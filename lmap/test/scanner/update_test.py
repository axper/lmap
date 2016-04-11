import os
import unittest
from datetime import datetime, timedelta

from scanner.update import Update
from unittest.mock import patch, mock_open, MagicMock
from scanner.scan_status import ScanStatus
from tempfile import NamedTemporaryFile


def raise_file_not_found_error():
    raise FileNotFoundError


class Test(unittest.TestCase):
    def test_get_pacman_last_update_date_when_not_found(self):
        # Prepare data and mocks
        file_contents_list = ['no such lines here']

        # Run test scenario
        last_update_date = Update(None).get_pacman_last_update_date(file_contents_list)

        # Assertions
        self.assertIsNone(last_update_date)

    def test_get_pacman_last_update_date_when_found(self):
        # Prepare data and mocks
        file_contents_list = ['line1', '[2016-04-05 10:24] [PACMAN] starting full system upgrade', 'line3']

        # Run test scenario
        last_update_date = Update(None).get_pacman_last_update_date(file_contents_list)

        # Assertions
        self.assertEqual(last_update_date, datetime.strptime('2016-04-05 10:24', '%Y-%m-%d %H:%M'))

    def test_scan_arch_when_is_older(self):
        # Prepare data and mocks
        with patch('builtins.open', mock_open()) as mock_file:
            config = {
                'update': {
                    'warn_last_update_interval_days': '2'
                }
            }
            update = Update(config)
            update.get_pacman_last_update_date = MagicMock(return_value=datetime.today() - timedelta(days=10))

            # Run test scenario
            result = update.scan_arch()

            # Assertions
            self.assertEqual(result[0], ScanStatus.fail)
            mock_file.assert_called_once_with('/var/log/pacman.log')
            update.get_pacman_last_update_date.assert_called_once_with([])

    def test_scan_arch_when_is_newer(self):
        # Prepare data and mocks
        with patch('builtins.open', mock_open()) as mock_file:
            config = {
                'update': {
                    'warn_last_update_interval_days': '2'
                }
            }
            update = Update(config)
            update.get_pacman_last_update_date = MagicMock(return_value=datetime.today() - timedelta(days=1))

            # Run test scenario
            result = update.scan_arch()

            # Assertions
            self.assertEqual(result[0], ScanStatus.success)
            mock_file.assert_called_once_with('/var/log/pacman.log')
            update.get_pacman_last_update_date.assert_called_once_with([])

    def test_scan_arch_when_last_update_date_not_found(self):
        # Prepare data and mocks
        with patch('builtins.open', mock_open()) as mock_file:
            config = {
                'update': {
                    'warn_last_update_interval_days': '2'
                }
            }
            update = Update(config)
            update.get_pacman_last_update_date = MagicMock(return_value=None)

            # Run test scenario
            result = update.scan_arch()

            # Assertions
            self.assertEqual(result[0], ScanStatus.unknown)
            mock_file.assert_called_once_with('/var/log/pacman.log')
            update.get_pacman_last_update_date.assert_called_once_with([])

    def test_scan_when_unknown(self):
        # Prepare data and mocks
        with patch('platform.linux_distribution', lambda: ('Unknown linux distribution', None, None)):
            update = Update(None)

            # Run test scenario
            result = update.scan()

            # Assertions
            self.assertEqual(result[0], ScanStatus.unknown)

    def test_scan_when_arch(self):
        # Prepare data and mocks
        with patch('platform.linux_distribution', lambda: ('arch', None, None)):
            update = Update(None)
            update.scan_arch = MagicMock(return_value=(ScanStatus.success, 'message'))

            # Run test scenario
            result = update.scan()

            # Assertions
            self.assertEqual(result, (ScanStatus.success, 'message'))
            update.scan_arch.assert_called_once_with()

    def test_scan_when_debian(self):
        # Prepare data and mocks
        with patch('platform.linux_distribution', lambda: ('debian', None, None)):
            update = Update(None)
            update.scan_debian = MagicMock(return_value=(ScanStatus.success, 'message'))

            # Run test scenario
            result = update.scan()

            # Assertions
            self.assertEqual(result, (ScanStatus.success, 'message'))
            update.scan_debian.assert_called_once_with()

    def test_scan_when_redhat(self):
        # Prepare data and mocks
        with patch('platform.linux_distribution', lambda: ('redhat', None, None)):
            update = Update(None)
            update.scan_redhat = MagicMock(return_value=(ScanStatus.unknown, 'message'))

            # Run test scenario
            result = update.scan()

            # Assertions
            self.assertEqual(result, (ScanStatus.unknown, 'message'))
            update.scan_redhat.assert_called_once_with()

    def test_get_apt_last_update_date_when_file_does_not_exist(self):
        # Prepare data and mocks
        with patch('builtins.open', raise_file_not_found_error):
            update = Update(None)

            # Run test scenario
            result = update.get_apt_last_update_date('/tmp/this/file/does/not/exist')

            # Assertions
            self.assertIsNone(result)

    def test_get_apt_last_update_date_when_file_exists(self):
        # Prepare data and mocks
        with patch('builtins.open', raise_file_not_found_error), NamedTemporaryFile() as temp_file:
            update = Update(None)
            seconds_epoch_in_1999 = 923398970
            os.utime(temp_file.name, (seconds_epoch_in_1999, seconds_epoch_in_1999))

            # Run test scenario
            result = update.get_apt_last_update_date(temp_file.name)

            # Assertions
            self.assertEqual(result.timestamp(), seconds_epoch_in_1999)

    def test_scan_debian_when_is_older(self):
        # Prepare data and mocks
        config = {
            'update': {
                'warn_last_update_interval_days': '2'
            }
        }
        update = Update(config)
        update.get_apt_last_update_date = MagicMock(return_value=datetime.today() - timedelta(days=10))

        # Run test scenario
        result = update.scan_debian()

        # Assertions
        self.assertEqual(result[0], ScanStatus.fail)
        update.get_apt_last_update_date.assert_called_once_with('/var/lib/apt/periodic/update-success-stamp')

    def test_scan_debian_when_is_newer(self):
        # Prepare data and mocks
        config = {
            'update': {
                'warn_last_update_interval_days': '2'
            }
        }
        update = Update(config)
        update.get_apt_last_update_date = MagicMock(return_value=datetime.today() - timedelta(days=1))

        # Run test scenario
        result = update.scan_debian()

        # Assertions
        self.assertEqual(result[0], ScanStatus.success)
        update.get_apt_last_update_date.assert_called_once_with('/var/lib/apt/periodic/update-success-stamp')

    def test_scan_debian_when_last_update_date_not_found(self):
        # Prepare data and mocks
        config = {
            'update': {
                'warn_last_update_interval_days': '2'
            }
        }
        update = Update(config)
        update.get_apt_last_update_date = MagicMock(return_value=None)

        # Run test scenario
        result = update.scan_debian()

        # Assertions
        self.assertEqual(result[0], ScanStatus.unknown)
        update.get_apt_last_update_date.assert_called_once_with('/var/lib/apt/periodic/update-success-stamp')

    def test_scan_redhat(self):
        # Prepare data and mocks
        update = Update(None)

        # Run test scenario
        result = update.scan_redhat()

        # Assertions
        self.assertEqual(result[0], ScanStatus.unknown)


if __name__ == '__main__':
    unittest.main()
