class Element(object):
    isX = False
    value = 0

    def __init__(self, isX=None, val=None):
        self.isX = isX
        self.value = val


def buildEquation( leftArray, rightArray ):
    leftResult = ""
    rightResult = ""

    leftArraySize = len( leftArray )
    rightArraySize = len( rightArray )
    #print( "array size: {0:3d} , {0:3d}".format(leftArraySize, rightArraySize))

    if 0 == leftArraySize :
        print( "0 left array: {0}".format( rightArray))
    if 0 == rightArraySize :
        print( "0 left array: {0}".format( leftArray))

    i = 0
    while i < leftArraySize:
        element = leftArray[i]
        i += 1

        operator = " + "
        if element.value < 0:
            operator = " - "

        leftResult += operator + str(abs(element.value))
        if element.isX :
            leftResult += "X"

    i = 0
    while i < rightArraySize:
        element = rightArray[i]
        i += 1

        operator = " + "
        if element.value < 0:
            operator = " - "

        rightResult += operator + str(abs(element.value))
        if element.isX:
            rightResult += "X"

    #trim leading space and leading "+" if exist
    leftResult = leftResult.strip()
    rightResult = rightResult.strip()

    if leftResult[0] == "+":
        leftResult = leftResult[1:]

    if rightResult[0] == "+":
        rightResult = rightResult[1:]

    return leftResult + " = " + rightResult