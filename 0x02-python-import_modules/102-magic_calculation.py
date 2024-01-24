import __import__('magic_calculation_102')

def magic_calculation(a, b):
    add = magic_calculation_102.add
    sub = magic_calculation_102.sub
    
    # Check if a is less than b
    if a < b:
        c = add(a, b)
        
        # Sum the numbers from 4 to 6
        for i in range(4, 6):
            c = add(c, i)
        
        return c
    else:
        # If a is not less than b, perform subtraction
        return sub(a, b)
