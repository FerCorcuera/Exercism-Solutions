def proverb(*items,qualifier = None):
    prov = []
    if items == ():
        return []
    # if len(items) == 1 and items[0] == 'nail':
    #     return ['And all for the want of a nail.']
    for x,y in zip(items,items[1::]):
        text = 'For want of a ' + x + ' the ' + y + ' was lost.'
        prov = prov + [text]
        
    # prov.reverse()
    if qualifier is not None:
        last = 'And all for the want of a ' + qualifier + ' nail.'
    else:
        last = 'And all for the want of a ' + items[0] + '.'
    prov.append(last) 
    return prov
