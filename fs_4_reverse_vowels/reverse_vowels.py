def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = "aeiouAEIOU"
    vowel_list = []

    for letter in s:
        if letter in vowels:
            vowel_list.append(letter)

    index_count = 0
    vowel_list.reverse()
    reversed_string = ''

    for letter in s:
        if letter in vowels:
            reversed_string += vowel_list[index_count]
            index_count += 1
        else: 
            reversed_string += letter

    return reversed_string
