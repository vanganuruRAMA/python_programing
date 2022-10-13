#!/usr/bin/env python

import argparse

# required defines a mandatory argument 
# default defines a default value if not specified

parser = argparse.ArgumentParser()

parser.add_argument('-b', type=int, required=False, help="defines the base value")
parser.add_argument('-e', type=int, default=2, help="defines the exponent value")
parser.add_argument('-user', type=str, default='admin', help="please enter user name")
parser.add_argument('-passwd', type=str, default='admin', help="please enter passwd name")
args = parser.parse_args()


user= args.user
passwd= args.passwd
print("user name is:", user)
print("user name is:", passwd)

# for i in range(exp):
    # val *= base

# print(val)