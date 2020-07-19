    import math

    ab = int(input())
    bc = int(input())

    degree_sign = u"\N{DEGREE SIGN}"

    print (str(int(round(math.degrees(math.atan2(ab,bc)))))+degree_sign)
