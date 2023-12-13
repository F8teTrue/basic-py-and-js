'''Roman numbers is a number-system used by the ancient Romans.

You can still see them today, maybe in tattoos and on watches.

An example is the number 26, which translates to the

Roman number of XXVI.'''

 

# TASK

'''

Make a num_to_roman transformer, that takes in an integer

and prints the transformed value.

Roman values:

1 = I, IV = 4, 5 = V, IX = 9, 10 = X,

L = 50, XC = 90, C = 100, CD = 400 D = 500, CM = 900 M = 1000

'''


def num_to_roman(number):
    roman = ''
    
    while number > 0:

        if number >= 1000:
            roman += 'M'
            number -= 1000
        elif number >= 900:
            roman += 'CM'
            number -= 900
        elif number >= 500:
            roman += 'D'
            number -= 500
        elif number >= 400:
            roman += 'CD'
            number -= 400
        elif number >= 100:
            roman += 'C'
            number -= 100
        elif number >= 90:
            roman += 'XC'
            number -= 90
        elif number >= 50:
            roman += 'L'
            number -= 50
        elif number >= 10:
            roman += 'X'
            number -= 10
        elif number >= 9:
            roman += 'IX'
            number -= 9
        elif number >= 5:
            roman += 'V'
            number -= 5
        elif number >= 4:
            roman += 'IV'
            number -= 4
        elif number >= 1:
            roman += 'I'
            number -= 1
        
    print(roman)

num_to_roman(2723)

def roman_to_num(roman):
    number = 0

    while roman != '':

        if 'CM' in roman:
            number += 900
            roman = roman.replace('CM', '', 1)
        elif 'CD' in roman:
            number += 400
            roman = roman.replace('CD', '', 1)
        elif 'XC' in roman:
            number += 90
            roman = roman.replace('XC', '', 1)
        elif 'XL' in roman:
            number += 40
            roman = roman.replace('XL', '', 1)
        elif 'IX' in roman:
            number += 9
            roman = roman.replace('IX', '', 1)
        elif 'IV' in roman:
            number += 4
            roman = roman.replace('IV', '', 1)
        elif 'M' in roman:
            number += 1000
            roman = roman.replace('M', '', 1)
        elif 'D' in roman:
            number += 500
            roman = roman.replace('D', '', 1) 
        elif 'C' in roman:
            number += 100
            roman = roman.replace('C', '', 1)
        elif 'L' in roman:
            number += 50
            roman = roman.replace('L', '', 1)
        elif 'X' in roman:
            number += 10
            roman = roman.replace('X', '', 1)
        elif 'V' in roman:
            number += 5
            roman = roman.replace('V', '', 1)
        elif 'I' in roman:
            number += 1
            roman = roman.replace('I', '', 1)
    
    print(number)

roman_to_num('MMMCMXLVII')

def roman_to_num(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    number = 0

    while roman != '':
        if roman[:2] in roman_numerals:
            number += roman_numerals[roman[:2]]
            roman = roman[2:]
        else:
            number += roman_numerals[roman[0]]
            roman = roman[1:]

    print(number)

roman_to_num('MMMCMXLVII')
