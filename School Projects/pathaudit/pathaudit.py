#!/usr/bin/env python


__author__ = 'iambrozie'


import argparse
import sys
import hashlib
import os
import os.path


def hashpath(param):
    path = param.path
    out = param.output

    if os.path.isfile(path):
        print("%s is a file" % path)
        print("Hashing....")
        out.write("%s: %s" % (os.path.abspath(path), hashfile(path)))

    if os.path.isdir(path):
        print("%s is a directory" % path)
        print("Recursively hashing...")
        for root, dirs, files in os.walk(path):
            for file in files:
                filepath = os.path.join(root, file)
                out.write("%s: %s \n" % (os.path.abspath(filepath), hashfile(filepath)))


def audit(param):
    print("Auditing...")
    lines = param.auditfile.read().rstrip().split('\n')
    for line in lines:
        path_hash = line.rstrip().split(': ')
        filepath = os.path.normpath(''.join(path_hash[:1]))
        if filepath != '.':
            filehash = ''.join(path_hash[1:])
            try:
                currhash = hashfile(filepath)
                if currhash == filehash:
                    print('%s: success' % filepath)
                else:
                    print('%s: fail' % filepath)
                    print('was: %s' % filehash)
                    print('is: %s' % currhash)
            except IOError:
                print("%s: no longer a valid path" % filepath)


def hashfile(filename):
    hasher = hashlib.sha256()
    with open(filename, 'rb') as fd:
        buf = fd.read()
        hasher.update(buf)
        return hasher.hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands')

    # A hash path command
    hash_parser = subparsers.add_parser('hash', help='Hash the supplied path')
    hash_parser.add_argument('path',
                              action='store',
                              help='User supplied path')
    hash_parser.add_argument('-o',
                              nargs="?",
                              dest='output',
                              action='store',
                              help="User supplied output file",
                              type=argparse.FileType('w'),
                              default=sys.stdout)
    hash_parser.set_defaults(func=hashpath)

    # An audit command
    audit_parser = subparsers.add_parser('audit', help='Audit mode')
    audit_parser.add_argument('auditfile',
                              action='store',
                              help='The audit file',
                              type=argparse.FileType('r'))
    audit_parser.set_defaults(func=audit)

    args = parser.parse_args()
    args.func(args)