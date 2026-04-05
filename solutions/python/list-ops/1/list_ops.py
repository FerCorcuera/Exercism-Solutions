def append(list1, list2):
    return list1 + list2


def concat(lists):
    final_list = []
    for x in lists:
        final_list = final_list + x

    return final_list
        
    


def filter(function, list):
    output = []
    for x in list:
        if function(x):
            output = output + [x]

    return output


def length(list):
    counter = 0
    for x in list:
        counter += 1

    return counter


def map(function, list):
    output = []
    for x in list:
        output = output + [function(x)]

    return output


def foldl(function, list, initial):
    acc = initial
    for x in list:
        acc = function(acc,x)

    return acc


def foldr(function, list, initial):
    acc = initial
    for x in range(0,len(list)):
        acc = function(acc,list[len(list)-x -1 ])

    return acc


def reverse(list):
    return list[::-1]
