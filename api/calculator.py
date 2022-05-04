from math import floor


def to_base20(value):
    alphabet = {
        0: '2',
        1: '3',
        2: '4',
        3: '5',
        4: '6',
        5: '7',
        6: '8',
        7: '9',
        8: 'C',
        9: 'F',
        10: 'G',
        11: 'H',
        12: 'J',
        13: 'M',
        14: 'P',
        15: 'Q',
        16: 'R',
        17: 'V',
        18: 'W',
        19: 'X'
    }
    result = ""
    while value != 0:
        mod = value % 20
        result = alphabet[mod] + result
        value = int(value / 20)
    return result


def to_olc(lat, long):
    lat = int((lat + 90) * 8000)
    print(lat)
    long = int((long + 180) * 8000)
    print(long)
    lat_code = to_base20(lat)
    long_code = to_base20(long)
    result = lat_code[0] + long_code[0] \
        + lat_code[1] + long_code[1] \
        + lat_code[2] + long_code[2] \
        + lat_code[3] + long_code[3] + '+' \
        + lat_code[4] + long_code[4]
    return result


lat = 48.8583
long = 2.2923
print(to_olc(lat, long))
