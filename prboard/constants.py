from functools import partial

import prboard.filters as filters


class State(object):
    """

    """
    Open = 'open'
    Closed = 'closed'
    All = 'all'


FILTER_COMMAND_MAPPING = {
    'num': filters.PRNumberFilter,
    'title': filters.PRFilter,
    'etitle': partial(filters.PRFilter, wildcard=True),
    'labels': filters.LabelFilter
}