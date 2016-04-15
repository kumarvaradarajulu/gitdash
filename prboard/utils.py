import prboard.constants as constants


def parse_pr_filters(filter_str):
    """
    Function to parse PR filter specified.
        "By PR Number ---->  num:123"
        "By PR Labels ---->  labels:label1,label2,label3"
        "By PR Title  ---->  title:pr_title   (wilcard match)"
        "By PR Title  ---->  etitle:pr_title  (exact match)"
        "By PR All    ---->  num:123,labels:label1,label2,label3,title:pr_title"

    Args:
        filter_str (str): Filter String to be parsed

    Returns:
        filters (list): List of filter objects

    """
    filter_mappings = constants.FILTER_COMMAND_MAPPING
    filts = filter_str.split(',')
    filter_objects = []
    for f in filts:
        try:
            cmd, value = f.split(':')
            filter_class = filter_mappings[cmd]
            filter_objects.append(filter_class(filter_value=value))
        except (ValueError, KeyError):
            continue

    return filter_objects
