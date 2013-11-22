import re

class Shamazing:

    def string(string):
        return max(re.findall(r'[a-zA-Z]+', string), key=len)

    def integer(string):
        return max(re.findall(r'[0-9]+', string), key=len)
