"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    
    for a in items_to_add:
    
        if current_cart.setdefault(a,"error") == "error":
            current_cart[a] = 1
        else:
            current_cart[a] = current_cart[a] +1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dic = dict.fromkeys(notes,1)

    return dic


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas |= recipe_updates

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    dic = dict(sorted(cart.items()))
    return dic


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    doc = {}
    for keys, values in cart.items():
    
        if aisle_mapping.setdefault(keys,"error") != "error":
            aisle_mapping[keys].insert(0,values)
            doc[keys] = aisle_mapping[keys]
        else:
            pass
    
    doc = dict(sorted(doc.items(),reverse=True))
    

    return doc


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for keys, values in fulfillment_cart.items():
        if store_inventory.setdefault(keys,"error") != "error":
            if store_inventory[keys][0] >  0 :
                store_inventory[keys][0] = store_inventory[keys][0] - fulfillment_cart[keys][0]
        
        if store_inventory[keys][0] == 0:
            store_inventory[keys][0] = 'Out of Stock'

    return store_inventory
