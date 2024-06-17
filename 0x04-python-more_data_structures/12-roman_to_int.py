def roman_to_int(roman_string) -> int:
    tbl = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60,
            'LXX': 70, 'LXXX': 80, 'XC': 90, 'C': 100,
            'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
            'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
            'M': 1000, 'MM': 2000, 'MMM': 3000
            }

    Rn = roman_string
    if type(Rn) != str or Rn is None:
        return 0
    if roman_string in tbl:
        return tbl[roman_string]
    elif Rn not in tbl:
        if len(Rn) <= 2:
            if len(Rn) == 1:
                return tbl[Rn[0]]
            elif len(Rn) == 2:
                return tbl[Rn[0:]]
        elif len(Rn) >= 3 and len(Rn) < 6:
            c3 = tbl[Rn[0]] + tbl[Rn[1]]
            if len(Rn) == 3:
                return c3
            elif len(Rn) == 4:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2:]]
            elif len(roman_string) == 5:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2]] +\
                       tbl[Rn[3:]]
        elif len(Rn) >= 6 and len(Rn) < 9:
            if len(Rn) == 6:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2]] +\
                       tbl[Rn[3]] + tbl[Rn[4:]]
            elif len(Rn) == 7:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2]] +\
                       tbl[Rn[3]] + tbl[Rn[4]] + tbl[Rn[5:]]
            elif len(roman_string) == 8:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2]] +\
                       tbl[Rn[3]] + tbl[Rn[4]] + tbl[Rn[5]] + tbl[Rn[6:]]
        elif len(Rn) >= 9 and len(Rn) < 12:
            if len(Rn) == 9:
                return tbl[Rn[0]] + tbl[Rn[1]] + tbl[Rn[2]] +\
                       tbl[Rn[3]] + tbl[Rn[4]] + tbl[Rn[5]] +\
                       tbl[Rn[6]] + tbl[Rn[7:]]
            elif len(Rn) == 10:
                return tbl[Rn[0]] + tbl[Rn[1]] +\
                       tbl[Rn[2]] + tbl[Rn[3]] + tbl[Rn[4]] +\
                       tbl[Rn[5]] + tbl[Rn[6]] + tbl[Rn[7]] + tbl[Rn[8:]]
            elif len(Rn) == 11:
                return tbl[Rn[0]] + tbl[Rn[1]] +\
                       tbl[Rn[2]] + tbl[Rn[3]] + tbl[Rn[4]] +\
                       tbl[Rn[5]] + tbl[Rn[6]] + tbl[Rn[7]] +\
                       tbl[Rn[8]] + tbl[Rn[9:]]
    else:
        return
