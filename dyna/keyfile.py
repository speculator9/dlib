from typing import List

from dyna.funcs import *
from dyna.kw import *
class KeyFile(object):
    keydata: List[str]

    def __init__(self, path):
        self.path = path
        self.keydata = self._keydata

    @property
    def _keydata(self):
        """Hidden method returns the data in text file as list of lines"""
        with open(self.path) as file:
            data = file.read().splitlines()
        return data

    @property
    def cards(self):
        """Method returns the cards in the existing deck as list"""
        crds = []

        for line in self.keydata:
            if "*" in line:
                crds.append(line.strip())

        return crds

    @property
    def duplicate_cards(self):
        dup_cards = dict()
        for card in set(self.cards):
            count = self.cards.count(card)
            if count > 1:
                dup_cards[card] = count

        return dup_cards

    @property
    def dataop(self):
        dic = dict()
        for key in set(self.cards):
            dic[key] = find_key(self.keydata, key)

        return dic

    @property
    def cardobject(self):
        dic = dict()

        for key in self.dataop:
            dic[key] = KeyWd(key, self.dataop[key])

        return dic


    def out_data(self):
        deck_keys = ['*KEYWORD', '*END']
        out = []

        out.append('*KEYWORD')
        for key in list(set(self.cards) - set(deck_keys)):

            if key not in self.duplicate_cards.keys():
                out.append(key)
                out.extend( self.dataop[key][0])

            else:
                for num in range(0, self.duplicate_cards[key]):
                    out.append(key)
                    out.extend(self.dataop[key][num])

        out.append('*END')

        return out

    def save(self, path=r'E:\Github\dlib\test', name=r'\savecheck.k'):
        with open(path + name, 'w+') as file:
            for line in self.out_data():
                file.write(f"{line}\n")

if __name__ == '__main__':
    c = KeyFile(r'E:\Github\dlib\test\check.k')
    # c.duplicate_cards
    # c.save()