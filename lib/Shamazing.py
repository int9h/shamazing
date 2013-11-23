import re

"""
" @author Manuel Wildauer <m.wildauer@gmail.com>
"
"""


class Shamazing:

    VERSION = "0.0.2"

    """
    " @param string string
    " @return string
    """
    def string(string):
        strings = re.findall(r'[a-zA-Z]+', string) or False
        if strings is not False:
            return max(strings, key=len)

        return "No strings found"

    """
    " @param string string
    " @return string
    """
    def integer(string):
        ints = re.findall(r'[0-9]+', string) or False
        if ints is not False:
            return max(ints, key=len)

        return "No integer found"

    """
    " @param list listOfStrings
    " @return string
    """
    def stringFromList(listOfStrings):
        strings = list()
        for sha in listOfStrings:
            strings.append(Shamazing.string(sha))

        return max(strings, key=len)

    """
    " @param list listOfStrings
    " @return string
    """
    def integerFromList(listOfStrings):
        integers = list()
        for sha in listOfStrings:
            integers.append(Shamazing.integer(sha))

        return max(integers, key=len)
