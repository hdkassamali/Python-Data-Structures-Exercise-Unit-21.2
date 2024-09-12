def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """
    flipped_case_string = ""
    for letter in phrase:
        if letter.isupper() and letter.lower() == to_swap.lower():
            flipped_case_string += letter.lower()
        elif letter.islower() and letter.lower() == to_swap.lower():
            flipped_case_string += letter.upper()
        else:
            flipped_case_string += letter
    return flipped_case_string
