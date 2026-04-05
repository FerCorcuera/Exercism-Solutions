"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dic = {}
    
    for a in items:
        valor = a
        if dic.setdefault(valor, "error")!="error":
            dic[valor] = dic[valor] + 1
        else:
            dic[valor] = 1
        

    return dic


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    dic = inventory
    list = items
    for a in list:
        valor = a
        if dic.setdefault(valor, "error")!="error":
            dic[valor] = dic[valor] + 1
        else:
            dic[valor] = 1
    
    return dic


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    dic = inventory
    list = items

    for a in list:
        value = a
        if dic.setdefault(value,"error") == "error":
            dic.pop(value,"deleted")
        else:
            if dic[value] > 0:
                dic[value] = dic[value] - 1
            elif dic[value] == 0:    
                dic[value] = 0
    return dic


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    dic = inventory
    a = item

    if dic.pop(a,"error") == a:
        return dic
    else:
        return dic
    


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    dic = inventory
    list = []
    for key, value in dic.items():
        if value > 0:
            
            list.append((key,value))
        else:
            pass

    return list

