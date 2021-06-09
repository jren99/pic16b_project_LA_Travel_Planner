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
    '''
    this function displays a travel plan summary includes travel length and time for each day.
    '''
    s=""
    for i in range(0, len(maps)):
        if 'distance' in route_list[i]:
            s += ("Day {}:".format(i+1)
            + " The traveling distance is {} miles".format(round(route_list[i]["distance"]/1609,1))
            + " and the traveling duration is {} min. ".format(round(route_list[i]["duration"]/60,1) ))
        else:
            s += ("Day {}:".format(i+1) + " This day has no travels.")
    return s