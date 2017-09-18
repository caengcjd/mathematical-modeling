def num2place(p):
    if p == 0:
        return 'D1'
    elif p == 1:
        return "D2"
    elif 2 <= p < 8:
        return 'Z%d' % (p - 1)
    elif 8 <= p < 68:
        return 'F%d' % (p - 7)
    elif 68 <= p < 130:
        return 'J%d' % (p - 67)
