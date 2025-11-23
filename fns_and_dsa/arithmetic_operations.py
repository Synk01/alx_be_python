def perform_operation(num1 , num2 , operation):
    # define operation
    match operation :
    case "add" :
        return num1 + num2
    case "subtract" :
        return num2 - num1
    case "multiply":
        return num2 * num1
     case "divide":
        if num2 == 0:
            return "DIVISION_BY_ZERO"
        return num1 / num2
    case _:
        return "INVALID_OPERATION"
