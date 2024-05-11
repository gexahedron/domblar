from chord_utils import *

def get_chords():
    chords = []

    # starting solo of second voice
    # 0
    chords.append(Chord(1.28, ch([None, 2616, None]), hz2c([None, None, None]), [None, 2543, None], 'kri'))
    chords.append(Chord(2.63, ch([None, 2598, None]), hz2c([None, None, None]), [None, 2543, None], 'ste'))
    chords.append(Chord(3.03, ch([None, 2615, None]), hz2c([None, None, None]), [None, 2543, None], 'aghs'))
    chords.append(Chord(3.38, ch([None, 2619, None]), hz2c([None, None, None]), [None, 2543, None], 'dga'))
    chords.append(Chord(3.79, ch([None, 2823, None]), hz2c([None, None, None]), [None, 2747, None], 'mkvdre'))
    chords.append(Chord(4.20, ch([None, 2499, None]), hz2c([None, None, None]), [None, 2432, None], 'tit'))

    # first verse
    # 6
    chords.append(Chord(6.30, ch([2197, 26, 756]), hz2c([None, None, None]), [2228, 2228, 2951], 'si'))
    chords.append(Chord(6.82, ch([2266, 16, 708]), hz2c([None, None, None]), [2228, 2228, 2951], 'kvdi'))
    chords.append(Chord(7.32, ch([2254, 28, 738]), hz2c([None, None, None]), [2228, 2228, 2951], 'li'))
    chords.append(Chord(7.72, ch([2220, 27, 729]), hz2c([None, None, None]), [2228, 2228, 2951], 'sa'))

    chords.append(Chord(8.15,  ch([2172, 560, 764]),  hz2c([None, None, None]), [2228, 2747, 2951], 'si'))
    chords.append(Chord(8.61,  ch([2209, 525, 750]),  hz2c([None, None, None]), [2228, 2747, 2951], 'kvdi'))
    chords.append(Chord(8.99,  ch([2207, 543, 769]),  hz2c([None, None, None]), [2228, 2747, 2951], 'li'))
    chords.append(Chord(9.43,  ch([1834, 720, 1151]), hz2c([None, None, None]), [1843, 2543, 2951], 'sa/ta'))
    chords.append(Chord(10.88, ch([1834, 720, 782]),  hz2c([None, None, None]), [1843, 2543, 2543], 'i/li'))
    chords.append(Chord(11.28, ch([2003, 537, 787]),  hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(12.32, ch([2008, 551, 736]),  hz2c([None, None, None]), [2024, 2543, 2747], 'trgun'))

    chords.append(Chord(13.25, ch([1981, 550, 1030]), hz2c([None, None, None]), [2024, 2543, 3010], 've'))
    chords.append(Chord(13.85, ch([2050, 503, 925]),  hz2c([None, None, None]), [2024, 2543, 2951], 'li'))
    chords.append(Chord(14.10, ch([1968, 579, 819]),  hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(14.54, ch([1996, 548, 560]),  hz2c([None, None, None]), [2024, 2543, 2543], 'sa'))
    chords.append(Chord(15.02, ch([1998, 561, 783]),  hz2c([None, None, None]), [2024, 2543, 2747], 'pla'))

    chords.append(Chord(15.88, ch([1982, 581, 1027]),    hz2c([None, None, None]), [2024, 2543, 3010], 've'))
    chords.append(Chord(16.56, ch([2038, 520, 946]),     hz2c([None, None, None]), [2024, 2543, 2951], 'bis'))
    chords.append(Chord(16.85, ch([2039, 539, 730]),     hz2c([None, None, None]), [2024, 2543, 2747], 'shi'))
    chords.append(Chord(17.27, ch([2041, 703, 889]),     hz2c([None, None, None]), [2024, 2747, 2951], 'na'))
    chords.append(Chord(17.75, ch([2041, 523, 514]),     hz2c([None, None, None]), [2024, 2543, 2543], 'a'))
    chords.append(Chord(18.16, ch([None, 2431+69, -69]), hz2c([None, None, None]), [None, 2543, 2432], 'ta'))

    chords.append(Chord(18.86, ch([2213, 502, 739]),  hz2c([None, None, None]), [2228, 2747, 2951], 'tskho'))
    chords.append(Chord(20.38, ch([2259, 337, 699]),  hz2c([None, None, None]), [2228, 2543, 2951], 'vre'))
    chords.append(Chord(21.48, ch([2100, 667, 725]),  hz2c([None, None, None]), [2024, 2747, 2543], 'bis'))
    chords.append(Chord(21.83, ch([1845, 736, 1247]), hz2c([None, None, None]), [1843, 2543, 3090], 'mi'))
    chords.append(Chord(22.61, ch([1906, 680, 1055]), hz2c([None, None, None]), [1843, 2543, 2951], 'mni'))
    chords.append(Chord(23.42, ch([1852, 512, 580]),  hz2c([None, None, None]), [1843, 2432, 2432], "ch'e"))
    chords.append(Chord(24.17, ch([1890, 327, 672]),  hz2c([None, None, None]), [1843, 2228, 2543], 'be'))
    chords.append(Chord(25.01, ch([2046, 9, 710]),    hz2c([None, None, None]), [2024, 2024, 2747], 'li'))

    # second verse
    # 36
    chords.append(Chord(27.81, ch([2045, 512, 901]),  hz2c([None, None, None]), [2024, 2543, 2951], 'kri'))
    chords.append(Chord(29.16, ch([2007, 564, 945]),  hz2c([None, None, None]), [2024, 2543, 2951], 'ste'))
    chords.append(Chord(29.64, ch([2004, 576, 952]),  hz2c([None, None, None]), [2024, 2543, 2951], 'aghs'))
    chords.append(Chord(30.00, ch([1994, 593, 1023]), hz2c([None, None, None]), [2024, 2543, 2951], 'dga'))
    chords.append(Chord(30.40, ch([2000, 781, 787]),  hz2c([None, None, None]), [2024, 2747, 2747], 'mkvdre'))
    chords.append(Chord(30.79, ch([2030, 400, 744]),  hz2c([None, None, None]), [2024, 2432, 2747], 'tit'))

    # for next 6 chords bottom voice is wrong in gvm (both pitches and syllables)
    # so i've taken them from tony
    chords.append(Chord(32.15, [2180, 2175, 2894], hz2c([None, None, None]), [2228, 2228, 2951], 'si'))
    chords.append(Chord(32.56, [2249, 2264, 2936], hz2c([None, None, None]), [2228, 2228, 2951], 'kvdi'))
    chords.append(Chord(33.01, [2243, 2245, 2955], hz2c([None, None, None]), [2228, 2228, 2951], 'li'))
    chords.append(Chord(33.35, [2197, 2210, 2973], hz2c([None, None, None]), [2228, 2228, 2951], 'ta'))

    chords.append(Chord(33.74, [2228, 2751, 2893],     hz2c([None, None, None]), [2228, 2747, 2951], 'si'))
    chords.append(Chord(34.14, [2211, 2737, 2945],     hz2c([None, None, None]), [2228, 2747, 2951], 'kvdi'))
    chords.append(Chord(34.51, ch([2218, 520, 733]),   hz2c([None, None, None]), [2228, 2747, 2951], 'li'))
    chords.append(Chord(34.89, ch([1836, 697, 1105]),  hz2c([None, None, None]), [1843, 2543, 2951], 'sa'))
    chords.append(Chord(36.04, ch([None, None, 2570]), hz2c([None, None, None]), [None, None, 2543], 'i'))
    chords.append(Chord(36.55, ch([2020, 498, 741]),   hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(37.56, ch([2028, 506, 709]),   hz2c([None, None, None]), [2024, 2543, 2747], 'trgun'))

    chords.append(Chord(38.51, ch([2004, 521, 1008]), hz2c([None, None, None]), [2024, 2543, 3090], 've'))
    chords.append(Chord(38.98, ch([2018, 497, 956]),  hz2c([None, None, None]), [2024, 2543, 2951], 'li'))
    chords.append(Chord(39.26, ch([2014, 513, 765]),  hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(39.64, ch([2021, 508, 522]),  hz2c([None, None, None]), [2024, 2543, 2543], 'sa'))
    chords.append(Chord(40.06, ch([1991, 538, 767]),  hz2c([None, None, None]), [2024, 2543, 2747], 'pla'))

    chords.append(Chord(41.00, ch([1999, 531, 1039]), hz2c([None, None, None]), [2024, 2543, 3090], 've'))
    chords.append(Chord(41.62, ch([2028, 519, 965]),  hz2c([None, None, None]), [2024, 2543, 2951], 'bis'))
    chords.append(Chord(41.87, ch([2031, 519, 747]),  hz2c([None, None, None]), [2024, 2543, 2747], 'shi'))
    chords.append(Chord(42.27, ch([2023, 686, 927]),  hz2c([None, None, None]), [2024, 2747, 2951], 'na'))
    chords.append(Chord(42.72, ch([2023, 500, 502]),  hz2c([None, None, None]), [2024, 2543, 2543], 'a'))
    chords.append(Chord(43.09, ch([1981, 384, 464]),  hz2c([None, None, None]), [2024, 2432, 2432], 'ta'))

    chords.append(Chord(43.69, ch([2213, 502, 739]),  hz2c([None, None, None]), [2228, 2747, 2951], 'tskho'))
    chords.append(Chord(45.46, ch([2247, 322, 695]),  hz2c([None, None, None]), [2228, 2543, 2951], 'vre'))
    chords.append(Chord(46.59, ch([2099, 615, None]), hz2c([None, None, None]), [2024, 2747, None], 'bis'))
    chords.append(Chord(47.10, ch([1828, 707, 1213]), hz2c([None, None, None]), [1843, 2543, 3090], 'mi'))
    chords.append(Chord(47.84, ch([1848, 710, 1113]), hz2c([None, None, None]), [1843, 2543, 2951], 'mni'))
    chords.append(Chord(48.65, ch([1689, 701, 703]),  hz2c([None, None, None]), [1843, 2432, 2432], "ch'e"))
    chords.append(Chord(49.44, ch([1844, 336, 686]),  hz2c([None, None, None]), [1843, 2228, 2543], 'be'))
    chords.append(Chord(50.25, ch([2036+18, -18, 697-18]), hz2c([None, None, None]), [2024, 2024, 2747], 'li'))

    # third verse
    # 72
    chords.append(Chord(53.23, ch([2035, 514, 904]), hz2c([None, None, None]), [2024, 2543, 2951], 'kri'))
    chords.append(Chord(54.49, ch([1991, 558, 951]), hz2c([None, None, None]), [2024, 2543, 2951], 'ste'))
    chords.append(Chord(55.09, [2000, None, 2936],   hz2c([None, None, None]), [2024, None, 2951], 'aghs'))
    chords.append(Chord(55.32, ch([2020, 530, 928]), hz2c([None, None, None]), [2024, 2543, 2951], 'dga'))
    chords.append(Chord(55.69, ch([2025, 703, 718]), hz2c([None, None, None]), [2024, 2747, 2747], 'mkvdre'))
    chords.append(Chord(56.09, ch([2013, 415, 698]), hz2c([None, None, None]), [2024, 2432, 2747], 'tit'))

    chords.append(Chord(57.47, ch([2118, 37, 746]), hz2c([None, None, None]), [2228, 2228, 2951], 'si'))
    chords.append(Chord(57.87, ch([2226, 6, 695]),  hz2c([None, None, None]), [2228, 2228, 2951], 'kvdi'))
    chords.append(Chord(58.31, ch([2232, 9, 695]),  hz2c([None, None, None]), [2228, 2228, 2951], 'li'))
    chords.append(Chord(58.65, ch([2197, 2, 738]),  hz2c([None, None, None]), [2228, 2228, 2951], 'ta'))

    chords.append(Chord(59.00, ch([2188, 484, 697]),   hz2c([None, None, None]), [2228, 2747, 2951], 'si'))
    chords.append(Chord(59.39, ch([2209, 527, 719]),   hz2c([None, None, None]), [2228, 2747, 2951], 'kvdi'))
    chords.append(Chord(59.76, ch([2203, 534, 720]),   hz2c([None, None, None]), [2228, 2747, 2951], 'li'))
    chords.append(Chord(60.16, ch([1793, 716, 1143]),  hz2c([None, None, None]), [1843, 2543, 2951], 'sa/ta'))
    chords.append(Chord(61.30, ch([None, None, 2529]), hz2c([None, None, None]), [None, None, 2951], 'i'))
    chords.append(Chord(61.86, ch([1997, 501, 743]),   hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(62.81, ch([2020, 492, 718]),   hz2c([None, None, None]), [2024, 2543, 2747], 'trgun'))

    chords.append(Chord(63.63, ch([2007, 497, 988]), hz2c([None, None, None]), [2024, 2543, 3090], 've'))
    chords.append(Chord(64.29, ch([2012, 503, 931]), hz2c([None, None, None]), [2024, 2543, 2951], 'li'))
    chords.append(Chord(64.49, ch([2013, 500, 771]), hz2c([None, None, None]), [2024, 2543, 2747], 'da'))
    chords.append(Chord(64.83, ch([2035, 471, 497]), hz2c([None, None, None]), [2024, 2543, 2543], 'sa'))
    chords.append(Chord(65.26, ch([2013, 505, 748]), hz2c([None, None, None]), [2024, 2543, 2747], 'pla'))

    chords.append(Chord(66.13, ch([1958, 554, 1045]), hz2c([None, None, None]), [2024, 2543, 3090], 've'))
    chords.append(Chord(66.76, ch([1989, 545, 955]),  hz2c([None, None, None]), [2024, 2543, 2951], 'bis'))
    chords.append(Chord(67.00, ch([2000, 535, 705]),  hz2c([None, None, None]), [2024, 2543, 2747], 'shi'))
    chords.append(Chord(67.39, ch([2006, 692, 910]),  hz2c([None, None, None]), [2024, 2747, 2951], 'na'))
    chords.append(Chord(67.86, ch([2006, 476, 542]),  hz2c([None, None, None]), [2024, 2543, 2543], 'a'))
    chords.append(Chord(68.27, ch([1997, 347, 509]),  hz2c([None, None, None]), [2024, 2432, 2432], 'ta'))

    chords.append(Chord(68.95, ch([2220, 489, 716]),  hz2c([None, None, None]), [2228, 2747, 2951], 'tskho'))
    chords.append(Chord(70.79, ch([2245, 317, 679]),  hz2c([None, None, None]), [2228, 2543, 2951], 'vre'))
    chords.append(Chord(72.04, [2105, 2755, None],    hz2c([None, None, None]), [2024, 2747, None], 'bis'))
    chords.append(Chord(72.61, ch([1791, 742, 1215]), hz2c([None, None, None]), [1843, 2543, 3090], 'mi'))
    chords.append(Chord(73.40, ch([1853, 694, 1082]), hz2c([None, None, None]), [1843, 2543, 2951], 'mni'))
    chords.append(Chord(74.29, ch([1701, 658, 667]),  hz2c([None, None, None]), [1843, 2432, 2432], "ch'e"))
    chords.append(Chord(75.13, ch([1800, 336, 709]),  hz2c([None, None, None]), [1843, 2136, 2543], 'be'))
    chords.append(Chord(76.20, ch([2004, 25, 720]),   hz2c([None, None, None]), [2024, 2024, 2747], 'li'))
    chords.append(Chord(76.20+3, [None, None, None],   hz2c([None, None, None]), [2024, 2024, 2747], '-'))

    return chords
