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
        if type(string) is str:
            strings = re.findall(r'[a-zA-Z]+', string) or None
            if strings is not None:
                return max(strings, key=len)
            return None
        raise TypeError

    """
    " @param string string
    " @return string
    """
    def integer(string):
        if type(string) is str:
            ints = re.findall(r'[0-9]+', string) or None
            if ints is not None:
                return max(ints, key=len)
            return None
        raise TypeError

    """
    " @param list listOfStrings
    " @return string
    """
    def stringFromList(listOfStrings):
        if type(listOfStrings) is list:
            strings = list()
            for sha in listOfStrings:
                strings.append(Shamazing.string(sha))

            return max(strings, key=len)
        raise TypeError

    """
    " @param list listOfStrings
    " @return string
    """
    def integerFromList(listOfStrings):
        if type(listOfStrings) is list:
            integers = list()
            for sha in listOfStrings:
                integers.append(Shamazing.integer(sha))

            return max(integers, key=len)
        raise TypeError
