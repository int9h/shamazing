import re

class Shamazing:
    """It's just sha-mazing

    Author Manuel Wildauer <m.wildauer@gmail.com>
    """

    VERSION = "0.0.3"

    def string(string):
        """Find the longest string [a-z] in given string and return it

        Arguments:
            string (string): the String to parse

        Returns:
            string: the longest found string or None if no string was found
        """
        if type(string) is str:
            strings = re.findall(r'[a-zA-Z]+', string) or None
            if strings is not None:
                # we have found a string
                return max(strings, key=len)
            return None
        raise TypeError

    def integer(string):
        """Find the longest string [0-9] in given string and return it

        Arguments:
            string (string): the String to parse

        Returns:
            string: the longest found string [0-9] or None if no string was found
        """
        if type(string) is str:
            ints = re.findall(r'[0-9]+', string) or None
            if ints is not None:
                return max(ints, key=len)
            return None
        raise TypeError

    def stringFromList(listOfStrings):
        """Find the longest string [a-z] in a list of strings

        Arguments:
            listOfStrings (list): a list of strings to iterate

        Returns:
            string: the longest found string [a-z]
        """
        if type(listOfStrings) is list:
            strings = list()
            for sha in listOfStrings:
                strings.append(Shamazing.string(sha))

            return max(strings, key=len)
        raise TypeError

    def integerFromList(listOfStrings):
        """Find the longest string [0-9] in a list of strings

        Arguments:
            listOfStrings (list): a list of strings to iterate

        Returns:
            string: the longest found string [0-9]
        """
        if type(listOfStrings) is list:
            integers = list()
            for sha in listOfStrings:
                integers.append(Shamazing.integer(sha))

            return max(integers, key=len)
        raise TypeError
