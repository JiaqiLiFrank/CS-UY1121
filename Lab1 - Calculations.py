def calc(operation):
    first_space = operation.find(" ")
    operand1 = operation[:first_space]
    operation = operation[first_space+1:]
    second_space = operation.find(" ")
    operand2 = operation[second_space+1:]
    operator = operation[0]
    final_result = 0
    if (operator == "+"):
        final_result = int(operand1) + int(operand2)
    if (operator == "-"):
        final_result = int(operand1) - int(operand2)
    if (operator == "*"):
        final_result = int(operand1) * int(operand2)
    output = "this execution of the function should return " + str(final_result)
    return output
