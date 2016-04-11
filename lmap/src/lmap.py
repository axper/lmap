import os

import yaml

from scanner.openports import OpenPorts
from scanner.update import Update
from scanner.worldwritable import WorldWritable


def main():
    """
    Runs the program
    """
    config = get_config()
    scanners = [
        Update(config),
        OpenPorts(config),
        WorldWritable(config),
    ]
    for scanner in scanners:
        print('-' * 79)
        print('Running:', scanner.__class__.__name__)
        result = scanner.scan()
        print('Status:', result[0])
        print('Message:\n' + result[1])


def get_config():
    """
    :return: A dictionary containing the program's configuration.
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + 'config.yml', 'r') as f:
        return yaml.load(f)


if __name__ == '__main__':
    main()
