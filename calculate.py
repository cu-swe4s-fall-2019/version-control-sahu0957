import argparse
import math_lib as ml

parser = argparse.ArgumentParser()
parser.add_argument("numerator", help="first number to add, and numerator", type=int)
parser.add_argument("denominator", help="second number to add, and denominator", type=int)
args = parser.parse_args()


if __name__ == '__main__':    
    x3 = ml.add(args.numerator,args.denominator)
    x4 = ml.div(args.numerator,args.denominator)
    print("your two numbers added together are:")
    print(x3)
    print("your first number divided by your second number:")
    print(x4)
