import os
import unittest
from unittest.mock import patch, MagicMock, call

from scan_status import ScanStatus
from worldwritable import WorldWritable


def raise_file_not_found_error(x):
    raise FileNotFoundError


class Test(unittest.TestCase):
    def test_scan_when_success(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        test_subject.scan_worldwritable_files_starting_with_dot = MagicMock(return_value=[])
        test_subject.scan_worldwritable_directories_with_no_sticky_bit_set = MagicMock(return_value=[])
        test_subject.scan_worldwritable_files_owned_by_root = MagicMock(return_value=[])

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.scan_worldwritable_files_starting_with_dot.assert_called_once_with()
        test_subject.scan_worldwritable_directories_with_no_sticky_bit_set.assert_called_once_with()
        test_subject.scan_worldwritable_files_owned_by_root.assert_called_once_with()
        self.assertEqual(result[0], ScanStatus.success)
        self.assertEqual(result[1], '')

    def test_scan_when_two_failures(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        test_subject.scan_worldwritable_files_starting_with_dot = MagicMock(return_value=[])
        test_subject.scan_worldwritable_directories_with_no_sticky_bit_set = MagicMock(return_value=['/some/failure'])
        test_subject.scan_worldwritable_files_owned_by_root = MagicMock(return_value=['/other/failure'])
        test_subject.get_scan_text = MagicMock(side_effect=['Test2 Failed', 'Test3 Failed'])

        # Run test scenario
        result = test_subject.scan()

        # Assertions
        test_subject.get_scan_text.assert_has_calls(
            [
                call('World writable directories with no sticky bit set', ['/some/failure']),
                call('World writable files owned by root', ['/other/failure']),
            ]
        )
        test_subject.scan_worldwritable_files_starting_with_dot.assert_called_once_with()
        test_subject.scan_worldwritable_directories_with_no_sticky_bit_set.assert_called_once_with()
        test_subject.scan_worldwritable_files_owned_by_root.assert_called_once_with()
        self.assertEqual(result[0], ScanStatus.fail)
        self.assertEqual(result[1], 'Test2 Failed\nTest3 Failed')

    def test_get_scan_text_when_list_does_not_have_items(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)

        # Run test scenario
        result = test_subject.get_scan_text('Check name', [])

        # Assertions
        self.assertEqual(result, 'Success: Check name')

    def test_get_scan_text_when_list_has_items(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)

        # Run test scenario
        result = test_subject.get_scan_text('Check name', ['file1', 'file2'])

        # Assertions
        self.assertEqual(result, 'Failure: Check name:\n\tfile1\n\tfile2')

    @unittest.mock.patch('worldwritable.os')
    def test_scan_worldwritable_directories_with_no_sticky_bit_set(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.walk.return_value = [
            ('/world/writable/not/sticky', (), ()),
            ('/not/world/writable/not/sticky', (), ()),
            ('/world/writable/sticky', (), ()),
        ]
        test_subject.is_world_writable = MagicMock(side_effect=[True, False, True])
        test_subject.is_sticky_bit_set = MagicMock(side_effect=[False, True])

        # Run test scenario
        result = test_subject.scan_worldwritable_directories_with_no_sticky_bit_set()

        # Assertions
        self.assertEqual(result, ['/world/writable/not/sticky'])
        mock_os.walk.assert_called_once_with('/')
        test_subject.is_world_writable.assert_has_calls(
            [
                call('/world/writable/not/sticky'),
                call('/not/world/writable/not/sticky'),
                call('/world/writable/sticky'),
            ]
        )
        test_subject.is_sticky_bit_set.assert_has_calls(
            [
                call('/world/writable/not/sticky'),
                call('/world/writable/sticky'),
            ]
        )

    @unittest.mock.patch('worldwritable.os')
    def test_scan_worldwritable_files_starting_with_dot(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.walk.return_value = [
            ('/dir1', ('/dir1/subdir1',), ('world_writable_starting_with_dot', 'not_world_writable_starting_with_dot')),
            ('/dir2', (), ()),
            ('/dir3', ('/dir3/subdir3',), ('world_writable_not_starting_with_dot',)),
        ]
        test_subject.is_world_writable = MagicMock(side_effect=[True, False, True])
        test_subject.is_starts_with_dot = MagicMock(side_effect=[True, False])

        # Run test scenario
        result = test_subject.scan_worldwritable_files_starting_with_dot()

        # Assertions
        self.assertEqual(result, ['world_writable_starting_with_dot'])
        mock_os.walk.assert_called_once_with('/')
        test_subject.is_world_writable.assert_has_calls(
            [
                call('world_writable_starting_with_dot'),
                call('not_world_writable_starting_with_dot'),
                call('world_writable_not_starting_with_dot'),
            ]
        )
        test_subject.is_starts_with_dot.assert_has_calls(
            [
                call('world_writable_starting_with_dot'),
                call('world_writable_not_starting_with_dot'),
            ]
        )

    @unittest.mock.patch('worldwritable.os')
    def test_scan_worldwritable_files_owned_by_root(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.walk.return_value = [
            ('/dir1', ('/dir1/subdir1',), ('world_writable_owned_by_root', 'not_world_writable_owned_by_root')),
            ('/dir2', (), ()),
            ('/dir3', ('/dir3/subdir3',), ('world_writable_not_owned_by_root',)),
        ]
        test_subject.is_world_writable = MagicMock(side_effect=[True, False, True])
        test_subject.is_owned_by_root = MagicMock(side_effect=[True, False])

        # Run test scenario
        result = test_subject.scan_worldwritable_files_owned_by_root()

        # Assertions
        self.assertEqual(result, ['world_writable_owned_by_root'])
        mock_os.walk.assert_called_once_with('/')
        test_subject.is_world_writable.assert_has_calls(
            [
                call('world_writable_owned_by_root'),
                call('not_world_writable_owned_by_root'),
                call('world_writable_not_owned_by_root'),
            ]
        )
        test_subject.is_owned_by_root.assert_has_calls(
            [
                call('world_writable_owned_by_root'),
                call('world_writable_not_owned_by_root'),
            ]
        )

    @unittest.mock.patch('worldwritable.os')
    def test_is_world_writable_when_file_does_not_exist(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.side_effect = raise_file_not_found_error
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_world_writable(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_world_writable_when_is(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0o40002, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_world_writable(path)

        # Assertions
        self.assertTrue(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_world_writable_when_is_not(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0o40005, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_world_writable(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_sticky_bit_set_when_is_not_set(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0o00000, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_sticky_bit_set(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_sticky_bit_set_when_is_set(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0o01000, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_sticky_bit_set(path)

        # Assertions
        self.assertTrue(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_sticky_bit_set_when_file_does_not_exist(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.side_effect = raise_file_not_found_error
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_sticky_bit_set(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_owned_by_root_when_is_not(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0, 0, 0, 0, 1, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_owned_by_root(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_owned_by_root_when_is(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.return_value = os.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_owned_by_root(path)

        # Assertions
        self.assertTrue(result)
        mock_os.stat.assert_called_once_with(path)

    @unittest.mock.patch('worldwritable.os')
    def test_is_owned_by_root_when_file_does_not_exist(self, mock_os):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        mock_os.stat.side_effect = raise_file_not_found_error
        path = '/does/not/actually/exist'

        # Run test scenario
        result = test_subject.is_owned_by_root(path)

        # Assertions
        self.assertFalse(result)
        mock_os.stat.assert_called_once_with(path)

    def test_is_starts_with_dot_when_does(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        path = '/starts/with/.dot'

        # Run test scenario
        result = test_subject.is_starts_with_dot(path)

        # Assertions
        self.assertTrue(result)

    def test_is_starts_with_dot_when_does_not(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        path = '/does/not/start/with/dot'

        # Run test scenario
        result = test_subject.is_starts_with_dot(path)

        # Assertions
        self.assertFalse(result)

    def test_is_starts_with_dot_when_empty_string(self):
        # Prepare data and mocks
        test_subject = WorldWritable(None)
        path = ''

        # Run test scenario
        result = test_subject.is_starts_with_dot(path)

        # Assertions
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
