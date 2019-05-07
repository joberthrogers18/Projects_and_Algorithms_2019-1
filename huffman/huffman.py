from heapq import heappush, heappop, heapify
from collections import defaultdict
import operator


class Huffman:

    def __init__(self, word):
        self.word = word
        self.frequence = {}
        self.sort_frequence = []
        self.codes = {}

        self.define_frequence()
        self.sortFrequence()
        self.buildTree()
        self.trim = self.trimTree(self.sort_frequence)
        self.assignCodes(self.trim)

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
            the_firsts = self.sort_frequence[0 : 2]
            rest = self.sort_frequence[2: ]
            combine_freq = the_firsts[0][0] + the_firsts[1][0]
            rest.append((combine_freq, the_firsts))
            rest.sort(key = lambda tup: tup[0])
            self.sort_frequence = rest
        
        self.sort_frequence = self.sort_frequence[0]

    def trimTree(self, tree):

        p = tree[1]
        if type(p) == type("") : return p
        else: return (self.trimTree(p[0]),self.trimTree(p[1]))

    def assignCodes(self,node, pat=''):
        
        if type(node) == type(""):
            self.codes[node] = pat
        else:
            self.assignCodes(node[0], pat + '0')
            self.assignCodes(node[1], pat + '1') 
        
if __name__ == "__main__":

    huffman = Huffman('Melanie eu te amo')
    print(huffman.codes)
