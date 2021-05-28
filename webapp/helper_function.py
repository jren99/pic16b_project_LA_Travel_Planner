def isfloat(value):
    '''
    helper function to decide whether an input can be converted to a number
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

def route_summary(maps, route_list):
    for i in range(0, len(maps)):
        x ="Day {}".format(i+1)
        y = "The traveling distance is {} m".format(route_list[i]["distance"]) 
        z = "The traveling duration is {} min".format(route_list[i]["duration"]/60)
    return [x,y,z]