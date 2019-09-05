# version_control
Get familiar with version control basics

Usage:
./run.sh [--help] numerator denominator
run.sh will print out the results of calculate.py 
First, run.sh  will print out the sum of two given integers
Second, the quotient of the numerator and the denominator


Functions:
math_lib.py div(a,b) will divide intergers a by b, returning None if b = 0
math_lib.py add(a,b) will add the two integers a and b together

calculate.py will execute functions add and div found in math_lib.py

v0.1: 
fixed bug: div method updated to handle zero denominators

v1.0: 
added add function to math_lib.py
added calculate.py, which prints the sum and quotient of your input integers
added run.sh to execute calculate.py
