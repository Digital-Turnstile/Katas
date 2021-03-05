#By Max
def filter_list(l):
    output = [];
    for a in l:
        if(isinstance(a, str)):
            print('removed: ' + a)
        else:
            output.append(a)
    return output
