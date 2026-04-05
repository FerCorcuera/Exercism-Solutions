"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, one, *rest = each_wagons_id

    *new_list, = one, *missing_wagons, *rest, first, second

    return new_list


def add_missing_stops(param_route,**param):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *stops, = param.values()
    stop_dic = {}
    stop_dic['stops'] = stops
    param_route = {**param_route,**stop_dic}    
    return param_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route
    more_route_information
    extended_route = {**route,**more_route_information}
    
    return extended_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    *wagons, = zip(*wagons_rows)
    wagons_list = []

    for a in wagons:
        wagons_list.append(list(a))
    
    return wagons_list
