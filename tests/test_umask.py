import unittest
from unittest.mock import patch, MagicMock, call

from scan_status import ScanStatus
from umask import Umask


class Test(unittest.TestCase):
    def test_scan_when_ok(self):
        # Prepare data and mocks
        umask = 0o0072
        test_subject = Umask(None)
        test_subject.get_umask_without_change = MagicMock(return_value=umask)

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.get_umask_without_change.assert_called_once_with()
        self.assertEqual(result[0], ScanStatus.success)

    def test_scan_when_wrong(self):
        # Prepare data and mocks
        umask = 0o0025
        test_subject = Umask(None)
        test_subject.get_umask_without_change = MagicMock(return_value=umask)

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.get_umask_without_change.assert_called_once_with()
        self.assertEqual(result[0], ScanStatus.fail)

    @unittest.mock.patch('umask.os')
    def test_get_umask_without_change(self, mock_os):
        # Prepare data and mocks
        mock_os.umask = MagicMock(return_value=0o123)

        # Run test scenario
        result = Umask(None).get_umask_without_change()

        # Assertions
        mock_os.umask.assert_has_calls(
            [
                call(0o0777),
                call(0o123),
            ]
        )
        self.assertEqual(result, 0o123)


if __name__ == '__main__':
    unittest.main()
