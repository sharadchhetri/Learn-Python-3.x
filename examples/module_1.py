def scooty(modelname,year):
    if modelname == 'pep':
        return "This scooty is suitable for short height people | Model Year:",year
    elif modelname == 'activa':
        return "This scooty is suitable for medium and long height people | Model Year:",year
    else:
        return "We do not have any check for your scooty model:",modelname

def car(modelname,year):
    if modelname == 'wagonr':
        return "Good Family Car, with lots of space inside | Model Year:",year
    elif modelname == 'alto':
        return "Good Car for hills road | Model Year:",year
    elif modelname == 'i10':
        return "Good Car but costly service | Model Year:",year
    elif modelname == 'jaguar':
        return "Good Car for rich people | Model Year:",year
    else:
        return "We do not have any check for your scooty model:",modelname

def carcost(modelname,year):
    a = year * 90 - 50000
    return a