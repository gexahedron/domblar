from chord_utils import *

def get_chords():
    chords = []

    # starting solo of second voice
    # 0
    chords.append(Chord(3.49, ch([None, 2771, None]), hz2c([None, 272.5, None]), [None, 2850, None], 'a'))
    chords.append(Chord(4.30, ch([None, 2785, None]), hz2c([None, 275.1, None]), [None, 2850, None], 'i'))
    chords.append(Chord(4.70, ch([None, 2798, None]), hz2c([None, 277.0, None]), [None, 2850, None], 'ha'))
    chords.append(Chord(6.46, ch([None, 2970, None]), hz2c([None, 305.4, None]), [None, 3010, None], 'ri'))
    chords.append(Chord(7.02, ch([None, 2820, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'ro'))

    # first verse
    # 5
    chords.append(Chord(7.76,  ch([2280, 377, 583]), hz2c([204.5, 256.2, 286.3]), [2341, 2680, 2850], 'ra'))
    # fixme middle and top in tony
    chords.append(Chord(8.54,  ch([2112, 353, 682]), hz2c([185.8, 256.2, 286.3]), [2114, 2499, 2850], 'sha'))
    chords.append(Chord(9.44,  ch([1877, 765, 768]), hz2c([163.4, 256.2, 286.3]), [1877, 2680, 2680], 're'))
    chords.append(Chord(10.11, ch([1902, 530, 889]), hz2c([165.6, 256.2, 286.3]), [1972, 2499, 2850], 'ro'))
    chords.append(Chord(10.94, ch([1905, 378, 718]), hz2c([165.0, 256.2, 286.3]), [1972, 2341, 2680], 'sha'))
    chords.append(Chord(12.49, ch([2088, 476, 900]), hz2c([183.8, 256.2, 286.3]), [2088, 2564, 3010], 'ra'))
    chords.append(Chord(13.99, ch([2114, 384, 726]), hz2c([187.3, 256.2, 286.3]), [2114, 2499, 2850], 'sha'))

    chords.append(Chord(15.38, ch([2253, 549, 844]), hz2c([209.3, 256.2, 286.3]), [2341, 2850, 3110], 'da'))
    chords.append(Chord(15.96, ch([2272, 535, 855]), hz2c([209.3, 256.2, 286.3]), [2341, 2850, 3110], 'le'))
    chords.append(Chord(16.64, ch([2318, 466, 694]), hz2c([210.1, 256.2, 286.3]), [2341, 2850, 3010], 'ko'))
    chords.append(Chord(17.25, ch([2307, 454, 548]), hz2c([209.3, 256.2, 286.3]), [2341, 2850, 2850], 'jas'))

    chords.append(Chord(17.87, ch([2299, 722, 750]), hz2c([207.7, 256.2, 286.3]), [2341, 3010, 3010], 'khel'))
    chords.append(Chord(18.42, ch([2324, 539, 766]), hz2c([211.1, 256.2, 286.3]), [2341, 2850, 3110], 'ghva'))
    chords.append(Chord(19.09, ch([2304, 369, 694]), hz2c([208.3, 256.2, 286.3]), [2341, 2680, 3010], 'zha'))
    chords.append(Chord(19.70, ch([2149, 296, 660]), hz2c([190.0, 256.2, 286.3]), [2172, 2499, 2850], 'le'))
    chords.append(Chord(20.45, ch([1913, 600, 732]), hz2c([166.4, 256.2, 286.3]), [1933, 2636, 2636], 're'))
    chords.append(Chord(20.98, ch([1931, 486, 886]), hz2c([170.1, 256.2, 286.3]), [1933, 2417, 2850], 'ro'))
    chords.append(Chord(21.58, ch([1933, 377, 699]), hz2c([167.4, 256.2, 286.3]), [1933, 2341, 2636], 'sha'))
    chords.append(Chord(22.87, ch([2117, 537, 703]), hz2c([187.1, 256.2, 286.3]), [2155, 2850, 2850], 'ra'))
    chords.append(Chord(24.17, ch([2155, 352, 677]), hz2c([190.6, 256.2, 286.3]), [2155, 2510, 2850], 'sha'))
    chords.append(Chord(25.50, ch([2307,   1,  19]), hz2c([209.3, 256.2, 286.3]), [2341, 2341, 2341], 'sha'))

    # second verse
    # 26
    chords.append(Chord(27.47, ch([None, 2826, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'sha'))
    chords.append(Chord(28.11, ch([None, 2804, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'i'))
    chords.append(Chord(28.49, ch([None, 2856, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'ho'))

    chords.append(Chord(29.70, ch([2304, 665, 818]), hz2c([207.8, 256.2, 286.3]), [2341, 3010, 3110], 'ri'))
    chords.append(Chord(30.26, ch([2327, 553, 771]), hz2c([211.4, 256.2, 286.3]), [2341, 2850, 3110], 'ro'))
    chords.append(Chord(30.82, ch([2310, 415, 711]), hz2c([208.8, 256.2, 286.3]), [2341, 2680, 3010], 'ra'))
    chords.append(Chord(31.37, ch([2138, 357, 706]), hz2c([188.6, 256.2, 286.3]), [2114, 2499, 2850], 'sha'))
    chords.append(Chord(31.59, ch([2138, 357, 307]), hz2c([188.6, 256.2, 286.3]), [2114, 2499, 2499], 'a'))
    chords.append(Chord(32.02, ch([1921, 718, 730]), hz2c([167.5, 256.2, 286.3]), [1877, 2680, 2680], 're'))
    chords.append(Chord(32.58, ch([1912, 541, 934]), hz2c([164.9, 256.2, 286.3]), [1877, 2499, 2850], 'ro'))
    chords.append(Chord(33.17, ch([1927, 406, 743]), hz2c([167.2, 256.2, 286.3]), [1877, 2341, 2680], 'sha'))
    chords.append(Chord(34.42, ch([2160, 509, 686]), hz2c([191.4, 256.2, 286.3]), [2172, 2680, 3010], 'ra'))
    chords.append(Chord(35.60, ch([2184, 330, 865]), hz2c([193.7, 256.2, 286.3]), [2172, 2499, 2850], 'sha'))

    # fixme tony
    chords.append(Chord(36.70, ch([2310, 459, 815]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'khel'))
    chords.append(Chord(37.16, ch([2318, 534, 815]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3110], 'ghva'))
    chords.append(Chord(37.75, ch([2354, 397, 686]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'zha'))
    chords.append(Chord(38.26, ch([None, 2866, 29]),  hz2c([ None, 256.2, 286.3]), [None, 2850, 3010], 'lekh'))
    chords.append(Chord(38.82, ch([2337, 480, 719]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], 'tet'))
    chords.append(Chord(39.30, ch([2337, 387, 772]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], 'nam'))
    chords.append(Chord(39.87, ch([1986, 714, 1044]), hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2850], 'ko'))
    chords.append(Chord(40.37, ch([1773, 654, 1081]), hz2c([193.7, 256.2, 286.3]), [1773, 2499, 2850], 'jas'))
    chords.append(Chord(41.00, ch([1981, 683, 691]),  hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2680], 're'))
    chords.append(Chord(41.47, ch([2017, 398, 639]),  hz2c([193.7, 256.2, 286.3]), [1972, 2417, 2680], 'ro'))
    chords.append(Chord(42.06, ch([2009, 325, 667]),  hz2c([193.7, 256.2, 286.3]), [1972, 2341, 2680], 'sha'))
    chords.append(Chord(43.18, ch([2168, 488, 688]),  hz2c([193.7, 256.2, 286.3]), [2172, 2680, 2850], 'ra'))
    chords.append(Chord(44.29, ch([2207, 345, 649]),  hz2c([193.7, 256.2, 286.3]), [2172, 2564, 2850], 'sha'))
    chords.append(Chord(45.42, ch([2355,  21, -12]),  hz2c([193.7, 256.2, 286.3]), [2341, 2341, 2341], 'sha'))

    # third verse
    # 53
    # fixme tony and redux
    chords.append(Chord(47.32, ch([None, 2846, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'sha'))
    chords.append(Chord(47.92, ch([None, 2843, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'i'))
    chords.append(Chord(48.20, ch([None, 2856, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'ho'))

    chords.append(Chord(49.37, ch([2293, 642, 837]), hz2c([207.8, 256.2, 286.3]), [2341, 3010, 3110], 'ri'))
    chords.append(Chord(49.79, ch([2326, 539, 831]), hz2c([211.4, 256.2, 286.3]), [2341, 2850, 3110], 'ro'))
    chords.append(Chord(50.36, ch([2326, 379, 734]), hz2c([208.8, 256.2, 286.3]), [2341, 2680, 3010], 'ra'))
    chords.append(Chord(50.95, ch([2162, 684, 711]), hz2c([188.6, 256.2, 286.3]), [2114, 2499, 2850], 'sha'))
    chords.append(Chord(51.51, ch([1984, 728, 1043]), hz2c([167.5, 256.2, 286.3]), [1877, 2680, 2680], 're'))
    chords.append(Chord(52.02, ch([1984, 486, 886]), hz2c([164.9, 256.2, 286.3]), [1877, 2499, 2850], 'ro'))
    chords.append(Chord(52.59, ch([1996, 364, 682]), hz2c([167.2, 256.2, 286.3]), [1877, 2341, 2680], 'sha'))
    chords.append(Chord(53.75, ch([2183, 514, 698]), hz2c([191.4, 256.2, 286.3]), [2172, 2680, 3010], 'ra'))
    chords.append(Chord(54.90, ch([2199, 360, 678]), hz2c([193.7, 256.2, 286.3]), [2172, 2499, 2850], 'sha'))

    chords.append(Chord(56.03, ch([2357, 398, 778]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'chu'))
    chords.append(Chord(56.39, ch([2341, 485, 842]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3110], 'kvan'))
    chords.append(Chord(56.95, ch([2336, 442, 748]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'tkhe'))
    chords.append(Chord(57.46, ch([2264, 592, 607]),  hz2c([193.7, 256.2, 286.3]), [2264, 2850, 3010], 'ral'))
    chords.append(Chord(57.92, ch([2335, 365, 713]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], 'kho'))
    chords.append(Chord(58.38, ch([2369, 477, 786]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], "q'el"))
    chords.append(Chord(58.88, ch([2337, 376, 699]), hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2850], 'pe'))
    chords.append(Chord(59.35, ch([2137, 313, 774]), hz2c([193.7, 256.2, 286.3]), [1773, 2499, 2850], 'nekh'))
    chords.append(Chord(59.65, ch([None, 2833, None]), hz2c([None, 256.2, None]), [None, 2499, None], 'kh'))
    chords.append(Chord(59.97, ch([2011, 674, 1034]),  hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2680], 're'))
    chords.append(Chord(60.45, [1995, 2514, 2891],  hz2c([193.7, 256.2, 286.3]), [1972, 2417, 2680], 'ro'))
    chords.append(Chord(60.59, [1995, 2514, 3092],  hz2c([193.7, 256.2, 286.3]), [1972, 2417, 2680], 'o'))
    chords.append(Chord(60.66, [1995, 2514, 2905],  hz2c([193.7, 256.2, 286.3]), [1972, 2417, 2680], 'o'))
    chords.append(Chord(60.98, ch([2015, 336, 647]),  hz2c([193.7, 256.2, 286.3]), [1972, 2341, 2680], 'sha'))
    chords.append(Chord(62.03, ch([2185, 527, 693]),  hz2c([193.7, 256.2, 286.3]), [2172, 2680, 2850], 'ra'))
    chords.append(Chord(63.07, ch([2207, 377, 666]),  hz2c([193.7, 256.2, 286.3]), [2172, 2564, 2850], 'sha'))
    chords.append(Chord(64.15, ch([2355,  19,  22]),  hz2c([193.7, 256.2, 286.3]), [2341, 2341, 2341], 'sha'))

    # fourth verse
    # 80
    chords.append(Chord(65.67, ch([None, 2385, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'sha'))
    chords.append(Chord(66.31, ch([None, 2307, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'i'))
    chords.append(Chord(66.68, ch([None, 2870, None]), hz2c([None, 280.3, None]), [None, 2850, None], 'ho'))

    chords.append(Chord(67.76, ch([2301, 675, 815]), hz2c([207.8, 256.2, 286.3]), [2341, 3010, 3110], 'ri'))
    chords.append(Chord(68.16, ch([2352, 526, 832]), hz2c([211.4, 256.2, 286.3]), [2341, 2850, 3110], 'ro'))
    chords.append(Chord(68.72, ch([2361, 354, 694]), hz2c([208.8, 256.2, 286.3]), [2341, 2680, 3010], 'ra'))
    chords.append(Chord(69.26, ch([2207, 300, 667]), hz2c([188.6, 256.2, 286.3]), [2114, 2499, 2850], 'sha'))
    chords.append(Chord(69.82, ch([2009, 640, 1013]), hz2c([167.5, 256.2, 286.3]), [1877, 2680, 2680], 're'))
    chords.append(Chord(70.35, ch([1989, 523, 908]), hz2c([164.9, 256.2, 286.3]), [1877, 2499, 2850], 'ro'))
    chords.append(Chord(71.00, ch([1999, 361, 712]), hz2c([167.2, 256.2, 286.3]), [1877, 2341, 2680], 'sha'))
    chords.append(Chord(72.08, ch([2183, 524, 706]), hz2c([191.4, 256.2, 286.3]), [2172, 2680, 3010], 'ra'))
    chords.append(Chord(73.29, ch([2200, 420, 681]), hz2c([193.7, 256.2, 286.3]), [2172, 2499, 2850], 'sha'))

    chords.append(Chord(74.35, ch([2301, 449, 859]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'zhi'))
    chords.append(Chord(74.75, ch([2318, 498, 874]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3110], 'kan'))
    chords.append(Chord(75.28, ch([2340, 437, 750]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 3010], 'ghom'))
    chords.append(Chord(75.80, ch([None, 2734, 141]),  hz2c([None, 256.2, 286.3]), [None, 2850, 3010], 'lar'))
    chords.append(Chord(76.32, ch([2302, 389, 702]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], 'khen'))
    chords.append(Chord(76.81, ch([2319, 369, 802]),  hz2c([193.7, 256.2, 286.3]), [2341, 2850, 2850], 'de'))
    chords.append(Chord(77.30, ch([2328, 370, 733]), hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2850], 'rya'))
    chords.append(Chord(77.78, ch([2135, 375, 791]), hz2c([193.7, 256.2, 286.3]), [1773, 2499, 2850], 'lekh'))
    chords.append(Chord(78.40, ch([1964, 704, 764]),  hz2c([193.7, 256.2, 286.3]), [1972, 2680, 2680], 're'))
    chords.append(Chord(78.82, ch([1993, 504, 739]),  hz2c([193.7, 256.2, 286.3]), [1972, 2417, 2680], 'ro'))
    chords.append(Chord(79.40, ch([2033, 438, 693]),  hz2c([193.7, 256.2, 286.3]), [1972, 2341, 2680], 'sha'))
    chords.append(Chord(79.98, ch([None, 2351, None]),  hz2c([None, 256.2, None]), [None, 2341, None], 'a'))
    chords.append(Chord(80.58, ch([2191, 455, 710]),  hz2c([193.7, 256.2, 286.3]), [2172, 2680, 2850], 'ra'))
    chords.append(Chord(81.64, ch([2223, 353, 680]),  hz2c([193.7, 256.2, 286.3]), [2172, 2564, 2850], 'sha'))
    chords.append(Chord(82.77, ch([2370,   2,   9]),  hz2c([193.7, 256.2, 286.3]), [2341, 2341, 2341], 'sha'))
    chords.append(Chord(82.77+1.9, [None, None, None], hz2c([None, None, None]), [None, None, None], '-'))

    return chords
