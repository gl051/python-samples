""" Demo-ing argparse. """

import argparse
parser = argparse.ArgumentParser(description='This is a sample program')
parser.add_argument("user", help="user")
parser.add_argument("age", help="age for the user", type=int)
parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
args = parser.parse_args()
print('User {}, Age {}'.format(args.user, args.age))
if args.verbose:
    print('Running in verbose mode')
