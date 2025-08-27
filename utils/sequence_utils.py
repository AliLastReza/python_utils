import functools
import operator


def flatten_list(list_var):
    return functools.reduce(operator.iconcat, list_var, [])
