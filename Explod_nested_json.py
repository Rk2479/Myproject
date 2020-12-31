def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
            print(val)
        if isinstance(val, list):
            for subdict in val:
                print('subdict is:', subdict)
                deeper = flatten(subdict).items()
                print(deeper)
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
                print(out)
        else:
            out[key] = val
    return out
    
d = {'a': 1, 'b': 2, 'c': {'c1': [{'c21': {'ram':100,'Rh':200}, 'c22': 2, 'c23': 3}]}, 'x': 1, 'y': 2}

print(flatten(d))
