# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import os
from base64 import b64encode


class ObfuscateAll():

    def __call__(self, name):
        self.name = name
        with open(self.name, 'r') as f:
            self.string = f.read()
        self.write()

    @staticmethod
    def rot13(r_string):
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i+c)] = chr((i+13) % 26 + c)

        return "".join([d.get(c, c) for c in r_string])

    def write(self):
        with open(self.name, 'w') as f:
            f.write("import codecs;"
                    "from base64 import b64decode;"
                    "rot13 = lambda s: codecs.encode(s, 'rot13');"
                    "s = {string};"
                    "eval(rot13(\'{obfs_eval}\'))\n".format({}, string = b64encode(self.rot13(self.string).encode("UTF-8")),
                                                       obfs_eval = self.rot13("eval(rot13(b64decode(s).decode(\\'UTF-8\\')))")))


if __name__ == "__main__":
    while True:
        name = str(input("Scriptname [name.py] > "))
        if os.path.isfile(name):
            break
        else:
            print(f"File not found [{name}]")
            continue
    OA = ObfuscateAll()
    OA(name)

