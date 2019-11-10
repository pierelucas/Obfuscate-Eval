# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import os
from base64 import b64encode


class ObfuscateAll():

    def __call__(self, name):
        self.name = name
        with open(self.name, 'r') as f:
            self.string = f.read()
            print(self.string)
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
            f.write("from base64 import b64decode\n\n"
                    "def rot13(r_string):\n"
                    "\td = {}\n"
                    "\tfor c in (65, 97):\n"
                    "\t\tfor i in range(26):\n"
                    "\t\t\td[chr(i+c)] = chr((i+13) % 26 + c)\n"
                    "\treturn ''.join([d.get(c, c) for c in r_string])\n\n"
                    "s = {string}\n\neval(rot13(b64decode(s).decode('UTF-8')))\n".format({}, string = b64encode(self.rot13(self.string).encode("UTF-8"))))


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

