#!/usr/bin/python
# coding: utf-8

import sys
import os

def main():
    BIN_DIR = os.path.dirname(os.path.realpath(__file__))
    ROOT_DIR = os.path.abspath(os.path.join(BIN_DIR, '..'))

    sys.path.extend([ROOT_DIR, os.path.join(ROOT_DIR, 'lib', 'loglady'), os.path.join(ROOT_DIR, 'lib', 'ansiterm')])
    import ohno.ohno

    instance = ohno.ohno.Ohno(ROOT_DIR)
    instance.loop()

if __name__ == '__main__':
    main()
