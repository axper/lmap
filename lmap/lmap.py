import os

import yaml

from openports import OpenPorts
from root import Root
from ssh import Ssh
from umask import Umask
from update import Update
from worldwritable import WorldWritable


def main():
    """
    Runs the program
    """
    config = get_config()
    scanners = []
    if config['enabled']['openports']:
        scanners.append(OpenPorts(config))
    if config['enabled']['root']:
        scanners.append(Root(config))
    if config['enabled']['ssh']:
        scanners.append(Ssh(config))
    if config['enabled']['umask']:
        scanners.append(Umask(config))
    if config['enabled']['update']:
        scanners.append(Update(config))
    if config['enabled']['worldwritable']:
        scanners.append(WorldWritable(config))

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
