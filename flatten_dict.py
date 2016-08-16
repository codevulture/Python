def flatten_dict(dic):
    j = {}
    for i in dic:
        if isinstance(dic[i], dict):
            for c in dic[i]:
                j["%s.%s" % (i,c)] = dic[i][c]
            return flatten_dict(j)
        else:
            j[i]=dic[i]
    print j

flatten_dict({'a': 1, 'b': {'x': 2, 'y': {'p':1,'q':{'g':5} } }, 'c': 4})
