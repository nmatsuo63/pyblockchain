import collections


def sorted_dict_by_key(unsorted_dict):
    return collections.OrdredDict(sorted(unsorted_dict.items(), key=lambda d: d[0]))
