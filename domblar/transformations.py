import numbers


def transpose(n, m):
    if isinstance(n, numbers.Number):
        return n + m
    if isinstance(n, list):
        return [transpose(note, m) for note in n]
    return n
