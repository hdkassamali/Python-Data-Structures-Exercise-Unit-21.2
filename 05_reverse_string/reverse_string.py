def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    reversed_string = ""
    for idx in range(len(phrase) - 1, -1, -1):
        reversed_string += phrase[idx]
    return reversed_string
