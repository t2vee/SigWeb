import argparse

from Utils.Log import Log
from Server import Web

ENABLE_CONSOLE_GARBAGE = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='start SigWeb')
    parser.add_argument('-a', '--address', action='store', default='0.0.0.0',
                        help='listening address')
    parser.add_argument('-p', '--port', action='store', help='listening port', default=42000, type=int)
    parser.add_argument('-c', '--config', action='store', help='config file')

    args = parser.parse_args()

    try:
        Web.start(args)
    except KeyboardInterrupt:
        Log.info('Shutting down...')
