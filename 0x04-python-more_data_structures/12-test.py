def roman_to_int(roman_string):
    tbl = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60,
            'LXX': 70, 'LXXX': 80, 'XC': 90, 'C': 100,
            'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
            'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
            'M': 1000, 'MM': 2000, 'MMM': 3000
            }
    if roman_string in tbl:
        return tbl[roman_string]
    else:
        if len(roman_string) == 1:
            return tbl[roman_string]
        elif len(roman_string) == 2:
            return tbl[roman_string[0]] + tbl[roman_string[1]]
        elif len(roman_string) == 3:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            return c3
        elif len(roman_string) == 4:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            return c3 + tbl[roman_string[3]]
        elif len(roman_string) == 5:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            return c3 + tbl[roman_string[3]] + tbl[roman_string[4]]
        elif len(roman_string) == 6:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            return c3 + c4_6
        elif len(roman_string) == 7:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            return c3 + c4_6 + tbl[roman_string[6]]
        elif len(roman_string) == 8:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            return c3 + c4_6 + tbl[roman_string[6]] + tbl[roman_string[7]]
        elif len(roman_string) == 9:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            c7_9 = tbl[roman_string[6]] + tbl[roman_string[7]] + tbl[roman_string[8]]
            return c3 + c4_6 + c7_9
        elif len(roman_string) == 10:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            c7_9 = tbl[roman_string[6]] + tbl[roman_string[7]] + tbl[roman_string[8]]
            return c3 + c4_6 + c7_9 + tbl[roman_string[9]]
        elif len(roman_string) == 11:
            c3 = tbl[roman_string[0]] + tbl[roman_string[1]] + tbl[roman_string[2]]
            c4_6 = tbl[roman_string[3]] + tbl[roman_string[4]] + tbl[roman_string[5]]
            c7_9 = tbl[roman_string[6]] + tbl[roman_string[7]] + tbl[roman_string[8]]
            c10_11 = tbl[roman_string[9]] + tbl[roman_string[10]]
            return c3 + c4_6 + c7_9 + c10_11
print(roman_to_int("VII"))
print(roman_to_int("LXVII"))

