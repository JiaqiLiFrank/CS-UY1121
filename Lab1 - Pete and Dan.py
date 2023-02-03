# <Jiaqi Li>
# CS - UY 1121
# 26 January 2023
# Lab 1
# Problem #2

def pete_and_dan(fraction):
    output_result = "Origin"
    if (fraction == "whole"):
        output_result = 28
        return ("{:.2f} {}".format(output_result,"grams"))
    if (fraction == "half"):
        output_result = 14
        return ("{:.2f} {}".format(output_result,"grams"))
    if (fraction == "quarter"):
        output_result = (28/4)
        return ("{:.2f} {}".format(output_result,"grams"))
    if (fraction == "eighth"):
        output_result = (28/8)
        return ("{:.2f} {}".format(output_result,"grams"))
    if (fraction == "sixteenth"):
        output_result = (28/16)
        return ("{:.2f} {}".format(output_result,"grams"))N