# <Jiaqi Li>
# CS - UY 1121
# 26 January 2023
# Lab 1
# Problem #1

def fizz_buzz(num):
    if ((num%5)==0):
        if((num%3)==0):
            return ("FizzBuzz")
        else:
            return ("Buzz")
    if ((num%3)==0):
        if((num%5)==0):
            return ("FizzBuzz")
        else:
            return ("Fizz")
    if (((num%3)!=0) and (num%5)!=0):
        return (str(num))