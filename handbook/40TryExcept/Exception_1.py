# encoding: utf-8
import sys


class FormatError(Exception):

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def log_error(self):
        print('Error at ', self.line, self.file)


def parser():
    raise FormatError(sys._getframe().f_lineno, sys.argv[0].split('/')[-1])


try:
    parser()
except FormatError as exc:
    exc.log_error()
