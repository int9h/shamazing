#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import re,hashlib,uuid
from optparse import OptionParser
parser = OptionParser()
(option, args) = parser.parse_args()


def createSHA():
    return str(hashlib.sha1(str(uuid.uuid4()).encode()).hexdigest())

class Shamazing:
    def string(self, string):
        return max(re.findall(r'[a-zA-Z]+', string), key=len)

    def integer(self, string):
        return max(re.findall(r'[0-9]+', string), key=len)

shamazing = Shamazing()

if len(args) != 0:
    sha = args[0]
else:
    sha = createSHA()
    print ("SHA1 is: " + sha)

print("Longest string: " + shamazing.string(sha))
print("Longest integer: " + shamazing.integer(sha))

