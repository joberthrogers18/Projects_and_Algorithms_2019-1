import os


class Huffman:

    def __init__(self, word, trim=(), dencode=1):
        print(type(trim))
        self.word = word
        self.frequence = {}
        self.sort_frequence = []
        self.codes = {}
        self.trim = trim
        self.word_encode = ''
        self.word_decode = ''

        if dencode:
            self.define_frequence()
            self.sortFrequence()
            self.buildTree()
            self.trim = self.trimTree(self.sort_frequence)
            self.assignCodes(self.trim)
            self.encode()
        else:
            self.word_encode = word
            self.decode()

    def define_frequence(self):
        # Function to take the number of character in phrase tha will
        # be translated

        freq_character = {}

        for char in self.word:
            if char in freq_character:
                freq_character[char] += 1
            else:
                freq_character[char] = 1

        self.frequence = freq_character

    def sortFrequence(self):

        keys_frequence = self.frequence.keys()

        for key in keys_frequence:
            self.sort_frequence.append((self.frequence[key], key))

        self.sort_frequence.sort()

    def buildTree(self):

        while len(self.sort_frequence) > 1:
            the_firsts = self.sort_frequence[0: 2]
            rest = self.sort_frequence[2:]
            combine_freq = the_firsts[0][0] + the_firsts[1][0]
            rest.append((combine_freq, the_firsts))
            rest.sort(key=lambda tup: tup[0])
            self.sort_frequence = rest

        self.sort_frequence = self.sort_frequence[0]

    def trimTree(self, tree):

        p = tree[1]
        if type(p) == type(""):
            return p
        else:
            return (self.trimTree(p[0]), self.trimTree(p[1]))

    def assignCodes(self, node, pat=''):

        if type(node) == type(""):
            self.codes[node] = pat
        else:
            self.assignCodes(node[0], pat + '0')
            self.assignCodes(node[1], pat + '1')

    def encode(self):
        for char in self.word:
            self.word_encode += self.codes[char]

    def decode(self):

        p = self.trim

        for bit in self.word_encode:
            if bit == '0':
                p = p[0]
            else:
                p = p[1]
            if type(p) == type(""):
                self.word_decode += p
                p = self.trim


if __name__ == "__main__":

    file = open("teste_encoded.txt", "r")

    first_line = file.readline()

    if first_line[:2] == "*(":

        word_dencode = ''

        for line in file:
            word_dencode += line

        dencode = Huffman(word=word_dencode, trim=eval(
            first_line[1:]), dencode=0)

        file_dencode = open(os.path.basename(file.name)[
                            0: -4]+"_dencoded.txt", "w+")
        file_dencode.write(dencode.word_decode)

    else:
        file.seek(0)

        word_for_encode = ''

        for line in file:
            word_for_encode += line

        encodefy = Huffman(word=word_for_encode)

        file_encode = open(os.path.basename(file.name)[
                           0: -4] + "_encoded.txt", "w+")

        file_encode.write("*" + str(encodefy.trim) + "\n")
        file_encode.write(str(encodefy.word_encode))

    file.close()
