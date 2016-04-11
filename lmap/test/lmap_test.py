import unittest
from unittest.mock import MagicMock

import lmap


def raise_file_not_found_error(x):
    raise FileNotFoundError


class Test(unittest.TestCase):
    def test_get_config(self):
        # Prepare data and mocks

        # Run test scenario
        result = lmap.get_config()

        # Assertions
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    @unittest.mock.patch('lmap.OpenPorts')
    @unittest.mock.patch('lmap.Update')
    @unittest.mock.patch('lmap.WorldWritable')
    def test_main(self, mock_open_ports, mock_update, mock_world_writable):
        # Prepare data and mocks
        config = MagicMock()
        lmap.get_config = MagicMock(return_value=config)

        # Run test scenario
        lmap.main()

        # Assertions
        lmap.get_config.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
