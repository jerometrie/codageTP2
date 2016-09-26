#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
:authors: DELECLUSE MARILLESSE
:date: 27/09/16
:object: TP2 Codage
"""

##### Fonctions à réaliser pour le TP #####

# Question 5

def integer_to_digit(integer):
    """
    Converts an integer into the corresponding hexadecimal digit.
    The integer given should be between 0 and 15 and return a string.

    :param integer: *(int)*
    :return: the hexadecimal digit representing the integer
    :rctype: *str*
    :UC: 0 <= integer < 16
    :Examples:
    >>> integer_to_digit(0)
    '0'
    >>> integer_to_digit(10)
    'A'
    >>> integer_to_digit(-3)
    Traceback (most recent call last):
    AssertionError: Veuillez entrer un entier entre 0 et 15
    
    >>> integer_to_digit(3.2)
    Traceback (most recent call last):
    AssertionError: Veuillez entrer un entier
    """

    assert(type(integer) == int), "Veuillez entrer un entier"
    assert(integer >= 0 and integer <= 15), "Veuillez entrer un entier entre 0 et 15"
    
    if(integer <= 9):
        res = chr(ord('0') + integer)
    else:
        res = chr(ord('A') - 10 + integer)
    return res

# Question 6

def integer_to_string(n, b):
    """
    Converts an integer n into base b.
    The result is returned as a string.

    :param n, b: *(int)*
    :return: a string representing the number converted into base b.
    :rctype: *str*
    :UC: b > 1 and n >= 0
    :Examples:
    >>> integer_to_string(8,2)
    '1000'
    """

    res = ""
    temp = n

    while(temp // b > 0):
        res = res + integer_to_digit(temp % b)
        temp = temp // b

    res = res + integer_to_digit(temp) # Adds the last digit of the converted number

    res = res[::-1] # Reverses the string
                    
    return res
    
# Question 9

def deux_puissance(n):
    """
    Returns 2 to the power of n.
    :param n: *(int)*
    :rctype: *int*
    :UC: n >= 0
    :Examples:
    >>> deux_puissance(0)
    1
    >>> deux_puissance(3)
    8
    """

    return 1 << n

# Question 12

def integer_to_binary_str(n):
    """
    Returns a string representing the conversion into binary of the integer entered as a parameter.
    :param: *(int)*
    :rctype: *str*
    :UC: n >= 0
    :Examples:
    >>> integer_to_binary_str(0)
    '0'
    >>> integer_to_binary_str(8)
    '1000'
    >>> integer_to_binary_str(-8)
    Traceback (most recent call last):
    AssertionError: Entrez un entier positif!
    """

    # Tests of n
    assert(n >= 0), "Entrez un entier positif!"

    if(n == 0):
        return "0"
    else:

        # Initialisation
        res = ''
        temp = n
        i = 0

        # Extract all bits from temp and concatenate the result
        while(temp > 0):
            res = res + str(((n >> i) & 1))
            temp = temp >> 1
            i += 1

        # Reverse the resulting string
        res = res[::-1]

        return res


# Question 13

def binary_str_to_integer(b):
    """
    Returns an int representing the conversion into decimal of the binary string entered as a parameter.
    :param: *(str)*
    :rctype: *int*
    :UC: b is a string composed of '0's and '1's
    :Examples:
    >>> binary_str_to_integer('1000')
    8
    >>> binary_str_to_integer('0')
    0
    >>> binary_str_to_integer(10001)
    Traceback (most recent call last):
    AssertionError: Entrez une chaîne de caractères!
    """
    # Test de b
    assert(type(b) == str), "Entrez une chaîne de caractères!"

    # Initialisation
    res = 0
    temp = b
    i = 0

    return int(b, 2)



##### Tests et réponses aux autres question #####

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Question 1

    n = 999
    print(n, 'converti en hexadécimal: {:x}'.format(n))
    print(n, 'converti en hexadécimal et MAJUSCULES: {:X}'.format(n))
    print(n ,'converti en octal: {:o}'.format(n))


    # Question 2

    n = 1331
    print('{:d} en binaire est {:s}'.format(n, bin(n)[2:]))
    print('{:d} en octal est {:s}'.format(n, oct(n)[2:]))
    print('{:d} en hexadécimal est {:s}'.format(n, hex(n)[2:]))

    # Question 3
    
    n = 1
    print("Question 3:")
    print("ch(ord('0') + 1 =", chr(ord('0') + n))
    print(ord('0'))
    # De 0 à 9 on obtient les chiffres décimaux 0...9.
    # Ensuite, pour n >=10, les caractères selon l'ordre de la table de
    # caractères Unicode

    # Question 4

    n = 10
    print("Pour n =", n, "on obtient", chr(ord('A') - 10 + n))
    
    # Question 5 - Test de la fonction integer_to_digit()

    print("Question 5:")
    for j in range(0, 16):
        print(integer_to_digit(j))
        
    
    # Question 7 - Affichage du tableau de conversion

    print("Question 7:")
    for i in range(0, 21):
        print("{:4d}".format(i, integer_to_string(i, 2)),
              ":", "{:>5s}".format(integer_to_string(i, 2)),
              "{:>3s}".format(integer_to_string(i, 8)),
              "{:>3s}".format(integer_to_string(i, 16)))

    # Question 8 et 9

    n = 5
    m = 3

    print(bin(n), "AND", bin(m), "donne", bin(n & m), "en opération bit à bit")
    print(bin(n), "OR", bin(m), "donne", bin(n | m), "en opération bit à bit")
    print(bin(n), "XOR", bin(m), "donne", bin(n ^ m), "en opération bit à bit")
    print("NOT", bin(m), "donne", bin(~(m)), "en opération bit à bit")
    print(n, "décalé à gauche de 1 bit donne", n << 1)
    print(n, "décalé à droite de 1 bit donne", n >> 1)

    # Le décalage à gauche rajoute un 0 en bit de poids fort, ce qui revient à multiplier
    # le nombre par 2.
    # Le décalage à droite fait l'inverse, il divise par 2 (division euclidienne).

    # Question 11

    # Pour tester si un entier est pair, il suffit de le comparer avec le même entier décalé à droite
    # puis à gauche, bit à bit. Le décalage à droite enlève de bit de poids faible et le décalage à
    # gauche met "0" à sa place. Si les 2 nombres sont égaux, c'est que l'entier de départ avait aussi
    # un 0 en bit de poids faible et était donc pair.

    # Question 12
    print("Question 12:")
    print(integer_to_binary_str(15))

    # Question 13
    print("Question 13:")
    print(binary_str_to_integer('1111'))





    

