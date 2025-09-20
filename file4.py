def decimal_to_binary_converter():
    """

    """
    
    try:
        decimal_num = int(input("Enter a decimal number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    
    if decimal_num == 0:
        print("The binary representation of 0 is 0.")
        return


    binary_num_string = ""

    temp_num = decimal_num

    while temp_num > 0:
        

        remainder = temp_num % 2
    decimal_to_binary_converter()
