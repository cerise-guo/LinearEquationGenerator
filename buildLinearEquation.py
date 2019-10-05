import random
from elements import Element
from datetime import datetime
from elements import buildEquation


def generateEquation():
    # ax + bx = c + d
    random.seed(datetime.now())
    a = random.randint(-10, 10)
    if a == 0:
        a = random.randint(1, 10)
    b = random.randint(-10, 10)
    if b == 0:
        b = random.randint(1, 10)
    x = random.randint(-10, 10)
    if x == 0:
        x = random.randint(1, 10)
    total = a * x + b * x
    c = random.randint(-10, 10)
    if c == 0:
        c = random.randint(1, 10)
    d = total - c
    #print("{0:3d}X + {1:3d}X = {2:3d} + {3:3d}".format(a, b, c, d))
    #print("X = {0:3d}".format(x))

    leftSide = ""
    rightSide = ""

    def trueOrFalse():
        if random.randint(1, 100) > 50:
            return True;

        return False;

    # true ==> move ax to right side of =
    moveAX = trueOrFalse()
    # true ==> move bx to right side of =
    moveBX = trueOrFalse()
    # true ==> move C to left side of =
    moveC = trueOrFalse()
    # true ==> move D to left side of =
    moveD = trueOrFalse()

    #cannot allow all elements at right
    if moveAX == True and moveBX == True and moveC == False:
        moveD = True

    # cannot allow all elements at left
    if moveAX == False and moveBX == False and moveC == True:
        moveD = False

    # true ==>  = mX + ...
    # False ==> = ... + mX
    rightSideXFirst = trueOrFalse()
    # true ==>  mX + ... =
    # False ==> ... + mX =
    leftSideXFirst = trueOrFalse()
    leftElements = []
    if leftSideXFirst:
        if moveAX == False:
            leftElements.append(Element(True, a))

        if moveBX == False:
            leftElements.append(Element(True, b))

        if moveC == True:
            leftElements.append(Element(False, c * (-1)))

        if moveD == True:
            leftElements.append(Element(False, d * (-1)))

    else:
        if moveC == True:
            leftElements.append(Element(False, c * (-1)))

        if moveD == True:
            leftElements.append(Element(False, d * (-1)))

        if moveAX == False:
            leftElements.append(Element(True, a))

        if moveBX == False:
            leftElements.append(Element(True, b))
    rightElements = []
    if rightSideXFirst:
        if moveAX == True:
            rightElements.append(Element(True, a * (-1)))

        if moveBX == True:
            rightElements.append(Element(True, b * (-1)))

        if moveC == False:
            rightElements.append(Element(False, c))

        if moveD == False:
            rightElements.append(Element(False, d))

    else:
        if moveC == False:
            rightElements.append(Element(False, c))

        if moveD == False:
            rightElements.append(Element(False, d))

        if moveAX == True:
            rightElements.append(Element(True, a * (-1)))

        if moveBX == True:
            rightElements.append(Element(True, b * (-1)))
    result = buildEquation(leftElements, rightElements)
    #print("debug : {0:3d}X + {1:3d}X = {2:3d} + {3:3d} , x = {4:3d}".format(a, b, c, d, x))

    return result + "  ; X = {0:3d}".format(x)


