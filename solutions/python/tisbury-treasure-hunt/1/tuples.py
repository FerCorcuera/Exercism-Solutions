"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    tup = tuple(azara_record[1])
    if (tup[0] == rui_record[1][0]) and (tup[1] == rui_record[1][1]):
        return True
    else: return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record,rui_record) == True:
        return azara_record + rui_record
    else: 
        return "not a match"


def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        cleaned = (record[0], record[2], record[3], record[4])  # drop record[1] (Azara coordinate)
        report += f"{cleaned}\n"
    return report
        


            
    
