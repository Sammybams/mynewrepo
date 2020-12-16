def is_perfect_square(num):
    """The function 'is_perfect_square' takes in a number as input parameter and returns that it is a perfect square or not."""

    try:
        square_root = num**(1/2)    #This finds the square root of the number.
        a = str(square_root).index('.')
        after_point = str(square_root)[a+1::]   #This separates the numbers after the decimal point from the square root.

        #Loop checks if the number(s) after the decimal point is/are equal to zero and returns True and if not it returns False.
        if int(after_point)==0:
            return True
        else:
            return False

    except:
        return "Invalid input."
    
print(is_perfect_square(9))
print(is_perfect_square(111))
print(is_perfect_square(225))
print(is_perfect_square(500))
