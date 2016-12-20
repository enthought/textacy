""" Localization of python-Levenshtein API for use in similarity.py """


def distance(str1, str2):
    raise NotImplementedError


def hamming(str1, str2):
    raise NotImplementedError


def jaro_winkler(str1, str2, prefix_weight=0.1):
    raise NotImplementedError
