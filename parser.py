""" E -> R | F E E
    R -> N | -N
    N -> nX
    X -> nX | epsilo
    F -> aY
    Y -> aY | epsilo
"""


def parse(str):
    print "stacks: " + "E$" + ", inputs: " + str + "$"
    return parse_aux("E$", str + "$")


def parse_aux(stacks, inputs):
    res = ""
    if not stacks and not inputs:
        print "stacks: " + stacks + ", inputs: " + inputs
        return True
    elif stacks[0] == inputs[0]:
        stacks = stacks[1:]
        inputs = inputs[1:]
        print "stacks: " + stacks + ", inputs: " + inputs
        return parse_aux(stacks, inputs)
    elif stacks[0] == 'E':
        res = reduxE(inputs[0])
    elif stacks[0] == 'N':
        res = reduxN(inputs[0])
    elif stacks[0] == 'X':
        res = reduxX(inputs[0])
    elif stacks[0] == 'R':
        res = reduxR(inputs[0])
    elif stacks[0] == 'F':
        res = reduxF(inputs[0])
    elif stacks[0] == 'Y':
        res = reduxY(inputs[0])
    else:
        print "stacks: " + stacks + ", inputs: " + inputs
        return False

    stacks = stacks[1:]
    stacks = res + stacks
    print "stacks: " + stacks + ", inputs: " + inputs
    return parse_aux(stacks, inputs)


def reduxE(c):
    if c.isdigit() or c == '-':
        return "R"
    elif c.isalpha():
        return "F E E"
    else:
        return "\0"


def reduxN(c):
    if c.isdigit():
        return c + "X"
    else:
        return "\0"


def reduxX(c):
    if c == ' ' or c == '$':
        return ""
    elif c.isdigit():
        return c + "X"
    else:
        return "\0"


def reduxR(c):
    if c.isdigit() or c == '-':
        return "N"
    else:
        return "\0"


def reduxF(c):
    if c.isalpha():
        return c + "Y"
    else:
        return "\0"


def reduxY(c):
    if c == ' ':
        return ""
    elif c.isalpha():
        return c + "Y"
    else:
        return "\0"


def main():
    print parse("ab 5 meno 4 5")


main()

