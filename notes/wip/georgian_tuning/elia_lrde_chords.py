from chord_utils import *

def get_chords():
    chords = []

    chords.append(Chord(0.78, ch([None, 2727, None]), hz2c([None, 265.9, None]), [None, 2756, None], 'e'))
    chords.append(Chord(1.98, ch([None, 2545, None]), hz2c([None, 239.2, None]), [None, 2584, None], 'lya'))
    chords.append(Chord(2.38, ch([None, 2409, None]), hz2c([None, 221.2, None]), [None, 2431, None], 'lar'))
    chords.append(Chord(2.80, ch([None, 2225, None]), hz2c([None, 199.0, None]), [None, 2259, None], 'de'))
    chords.append(Chord(3.47, ch([None, 2565, None]), hz2c([None, 241.9, None]), [None, 2584, None], 'i'))
    chords.append(Chord(5.20, ch([None, 2407, None]), hz2c([None, 238.2, None]), [None, 2552, None], 'i'))

    # first verse
    # 6
    chords.append(Chord(5.66,  ch([2022, 384, 702]),  hz2c([177.2, 219.6, 265.7]), [2055, 2431, 2756], 'la'))
    chords.append(Chord(7.57,  ch([2051, 454, 676]),  hz2c([179.5, 234.0, 265.7]), [2055, 2501, 2724], 'i/qi'))
    chords.append(Chord(9.18,  ch([2025, 457, 703]),  hz2c([177.8, 230.7, 265.7]), [2055, 2482, 2724], 'le/me'))
    chords.append(Chord(10.07, ch([2086, 421, 671]),  hz2c([183.3, 234.0, 270.2]), [2106, 2501, 2775], 'i'))
    chords.append(Chord(10.59, ch([2039, 436, 688]),  hz2c([178.4, 229.9, 265.9]), [2055, 2482, 2724], 'a'))
    chords.append(Chord(11.03, ch([1785, 558, 828]),  hz2c([154.3, 211.6, 249.8]), [1781, 2329, 2622], 'uo'))
    chords.append(Chord(11.53, ch([1516, 906, None]), hz2c([131.4, 222.9,  None]), [1507, 2399, None], 'o'))
    chords.append(Chord(11.99, ch([1660, 410, 747]),  hz2c([142.9, 181.8, 221.3]), [1679, 2055, 2399], 'o/le'))
    chords.append(Chord(13.47, ch([1860, 532, 713]),  hz2c([161.2, 222.2, 239.5]), [1851, 2431, 2552], 'si'))
    chords.append(Chord(14.17, ch([1837, 433, 763]),  hz2c([161.2, 204.0, 246.5]), [1851, 2259, 2603], 'a'))
    chords.append(Chord(14.87, ch([2053, 30, 36]),    hz2c([180.4, 183.2, 183.8]), [2055, 2055, 2055], 'uo'))

    # second verse
    # 17
    chords.append(Chord(16.91, ch([2061, 479, 710]),   hz2c([180.7, 238.6, 270.7]), [2055, 2552, 2756], 'a/sa'))
    chords.append(Chord(18.28, ch([2062, 502, 713]),   hz2c([180.7, 241.9, 271.9]), [2055, 2552, 2756], 'i'))
    chords.append(Chord(19.07, ch([2062, None, 716]),  hz2c([180.7,  None, 276.2]), [2055, None, 2756], 'i/a'))
    chords.append(Chord(19.86, ch([2011, 524, 767]),   hz2c([175.7, 237.8, 276.2]), [2004, 2552, 2756], 'a/da'))
    chords.append(Chord(21.19, ch([2053, 348, 734]),   hz2c([180.0, 220.1, 276.2]), [2055, 2399, 2756], 'a/ma/ua'))
    chords.append(Chord(21.85, ch([1822, 416, 865]),   hz2c([157.3, 200.3, 260.9]), [1851, 2227, 2724], 'a'))
    chords.append(Chord(22.69, ch([1713, 840, 1166]),  hz2c([147.9, 240.4, 291.0]), [1679, 2552, 2877], 'ki'))
    chords.append(Chord(23.60, ch([1713, 840, 1166]),  hz2c([146.9, 241.0, 291.0]), [1679, 2552, 2877], 'ri'))
    chords.append(Chord(23.97, ch([1655, 713, 1113]),  hz2c([142.9, 216.0, 272.3]), [1679, 2380, 2756], 'o/a'))
    chords.append(Chord(24.58, ch([1604, 596, 1043]),  hz2c([138.9, 195.9, 254.1]), [1679, 2227, 2654], 'uo/ra/a'))
    chords.append(Chord(24.99, ch([None, 2326, -111]), hz2c([ None, 210.9, 198.0]), [None, 2329, 2227], 'o/a'))
    chords.append(Chord(25.47, ch([1651, 414, 723]),   hz2c([143.1, 181.3, 216.8]), [1679, 2055, 2380], 'le'))
    chords.append(Chord(27.10, ch([1863, 507, 854]),   hz2c([160.1, 216.3, 264.0]), [1851, 2380, 2724], 'si/ri'))
    chords.append(Chord(27.73, ch([1842, 383, 705]),   hz2c([160.1, 198.8, 239.6]), [1851, 2227, 2552], 'a'))
    chords.append(Chord(28.40, ch([2062, 4, 6]),       hz2c([181.6, 181.6, 181.4]), [2055, 2055, 2055], 'uo'))

    # third verse
    # 32
    chords.append(Chord(30.41, ch([2028, 491, 734]),  hz2c([177.9, 236.0, 271.5]), [2055, 2552, 2756], 'kra'))
    chords.append(Chord(32.21, ch([2030, 538, 766]),  hz2c([178.5, 242.4, 276.0]), [2055, 2603, 2775], 'si'))
    chords.append(Chord(32.81, ch([1686, 677, 1072]), hz2c([144.9, 215.5, 270.6]), [1679, 2380, 2756], 'uo'))
    chords.append(Chord(33.34, ch([1686, 677, 670]),  hz2c([144.9, 215.5, 214.7]), [1679, 2380, 2380], 'uo/o'))
    chords.append(Chord(33.98, ch([1834, 362, 710]),  hz2c([158.0, 194.9, 239.4]), [1851, 2208, 2552], 'de/re'))
    # 37
    chords.append(Chord(35.18, ch([2020, 513, 732]),  hz2c([176.8, 237.6, 269.4]), [2055, 2552, 2756], 'kra'))
    chords.append(Chord(36.71, ch([2011, 564, 730]),  hz2c([175.1, 243.4, 267.4]), [2055, 2603, 2756], 'si'))
    chords.append(Chord(37.20, ch([1683, 705, 709]),  hz2c([145.6, 218.5, 219.2]), [1679, 2380, 2399], 'uo')) # 2380 and 2399
    chords.append(Chord(38.34, ch([1795, 431, 751]),  hz2c([153.9, 199.0, 239.2]), [1851, 2227, 2552], 'de/le'))
    # 41
    chords.append(Chord(39.30, ch([2006, 502, 716]),  hz2c([176.7, 234.8, 268.5]), [2055, 2552, 2756], 'a'))
    chords.append(Chord(39.97, ch([2039, 530, 714]),  hz2c([176.7, 242.5, 268.5]), [2055, 2603, 2756], 'li/i'))
    chords.append(Chord(40.41, ch([2016, 366, 720]),  hz2c([176.7, 217.8, 268.5]), [2055, 2380, 2756], 'a/gha'))
    chords.append(Chord(40.89, ch([2037, 533, 727]),  hz2c([176.7, 242.7, 268.5]), [2055, 2603, 2756], 'li/i'))
    chords.append(Chord(41.51, ch([2028, 518, 720]),  hz2c([176.7, 239.3, 268.5]), [2055, 2552, 2756], 'me/ma'))
    chords.append(Chord(42.24, ch([2083, 500, 679]),  hz2c([182.1, 244.5, 270.3]), [2106, 2603, 2756], 'i'))
    chords.append(Chord(42.47, ch([2065, 325, 650]),  hz2c([181.9, 218.8, 264.0]), [2106, 2380, 2756], 'a'))
    chords.append(Chord(42.95, ch([1784, 465, 773]),  hz2c([153.3, 201.5, 241.1]), [1781, 2227, 2552], 'uo'))
    chords.append(Chord(43.16, ch([1515, 735, 1043]), hz2c([131.4, 201.5, 241.1]), [1507, 2227, 2552], 'uo/o'))
    chords.append(Chord(43.59, ch([1674, 408, 719]),  hz2c([144.5, 183.1, 219.2]), [1679, 2055, 2380], 'lo/le'))
    chords.append(Chord(44.84, ch([1884, 516, 657]),  hz2c([162.4, 219.9, 240.1]), [1851, 2380, 2552], 'si/li'))
    chords.append(Chord(45.26, ch([1874, 390, 680]),  hz2c([162.4, 203.5, 240.1]), [1851, 2227, 2552], 'a'))
    chords.append(Chord(45.88, ch([2062, 10, 11]),    hz2c([181.3, 182.1, 182.1]), [2055, 2055, 2055], 'uo'))

    # fourth verse
    # 54
    chords.append(Chord(47.98, ch([2055, 488, 684]),  hz2c([180.0, 239.1, 268.3]), [2055, 2552, 2756], 'so/sa'))
    chords.append(Chord(49.38, ch([2069, 500, 682]),  hz2c([183.1, 242.6, 268.3]), [2106, 2552, 2756], 'li'))
    chords.append(Chord(50.77, ch([2043, 498, 704]),  hz2c([179.8, 238.7, 268.3]), [2055, 2552, 2756], 'a/da/ma'))
    chords.append(Chord(52.36, ch([2066, 337, 712]),  hz2c([179.8, 220.1, 273.7]), [2055, 2399, 2756], 'ma/ua'))
    chords.append(Chord(52.95, ch([1884, 348, 779]),  hz2c([163.6, 199.8, 257.9]), [1902, 2227, 2673], 'a'))
    chords.append(Chord(53.80, ch([1680, 877, 1199]), hz2c([146.1, 240.7, 290.4]), [1679, 2552, 2877], 'ki'))
    chords.append(Chord(54.87, ch([1713, 860, 1192]), hz2c([149.5, 242.8, 290.4]), [1679, 2552, 2877], 'ri'))
    chords.append(Chord(55.35, ch([1663, 697, 1088]), hz2c([144.6, 215.0, 269.5]), [1679, 2329, 2756], 'a'))
    # the next one is a bit questionable/tricky, so, let's stick to this interpretation:
    # intervals: 1663+567-1635=595, 1663+963-1635=991
    chords.append(Chord(55.97, ch([1635, 595, 991]), hz2c([141.6, 199.3, 250.6]), [1679, 2227, 2622], 'uo/ra/lol'))
    chords.append(Chord(56.28, ch([1635, 701, 577]), hz2c([141.6, 212.2, 197.9]), [1679, 2329, 2227], 'le/a/lol'))
    chords.append(Chord(56.76, ch([1682, 385, 693]), hz2c([144.8, 181.6, 217.1]), [1679, 2055, 2380], 'le/me')) # 2380 in top voice
    chords.append(Chord(58.65, ch([1882, 524, 837]), hz2c([163.1, 222.0, 269.0]), [1851, 2431, 2756], 'si/li')) # 2399 in middle voice
    chords.append(Chord(59.34, ch([1855, 414, 726]), hz2c([159.8, 203.8, 243.8]), [1851, 2259, 2552], 'a'))
    chords.append(Chord(60.15, ch([2078, -8, -5]),   hz2c([182.2, 181.8, 182.0]), [2055, 2055, 2055], 'uo'))
    chords.append(Chord(60.15+2.04, [None, None, None], hz2c([None, None, None]), [None, None, None], '-'))

    return chords
