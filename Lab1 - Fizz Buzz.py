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
