def capitalize_all(t):

    res =[]
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(nested_list):

    new = []
    
    for t in nested_list:
        new.extend(capitalize_all(t))

    return new
   

test = [['hi','ook'],['bye']]
    
x= capitalize_nested(test)
