def transform(legacy_data):
    data = {}
    for key in legacy_data.keys():
        
        for x in legacy_data[key]:
            x = x.lower()
            data[x] = key

    return data
        
