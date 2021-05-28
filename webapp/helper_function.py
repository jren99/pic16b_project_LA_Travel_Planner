def isfloat(value):
    '''
    helper function to decide whether an input can be converted to a number
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False