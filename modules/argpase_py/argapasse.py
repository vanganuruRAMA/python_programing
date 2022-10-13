import argparse


parser = argparse.ArgumentParser()
#args=parser.parse_args()
parser.add_argument("number1", help="first number")
parser.add_argument("number2", help="second number")
parser.add_argument("operation", help="operation")
args=parser.parse_args()
print(args.number1)
print(args.number2)
print(args.operation)

#parser.parse_args()

'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args(1)
print(args.echo)
'''