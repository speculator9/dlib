# path = r'E:\Github\dlib\test\check.k'
from typing import List

from dyna.funcs import *


class KeyFile(object):
    keydata: List[str]

    def __init__(self, path):
        self.path = path
        self.keydata = self._keydata
        self.card_lines = dict()
        self.card_count = None

    @property
    def cards(self):
        """Method returns the cards in the existing deck as list"""
        crds = []

        for line in self.keydata:
            if "*" in line:
                crds.append(line.strip())

        return crds

    @property
    def _keydata(self):
        """Hidden method returns the data in text file as list of lines"""
        with open(self.path) as file:
            data = file.readlines()
        return data

    @property
    def _card_count(self):

        card_dic = {}

        for card in self.cards:
            start, lines = find_key(self.keydata, card)
            card_dic[card] = {'num_lines': '',
                              'lines': lines,
                              'start': start}

        self.card_count = card_dic
        return self.card_count

    def add_keyword(self, keyword, num_lines):
        if "*" not in keyword or not isinstance(num_lines, int):
            raise ValueError("The Keyword Should start with * or num_lines should be integer")
        self.keydata.append(keyword)
        self.card_lines[keyword] = num_lines
        self.__update__()


    def __update__(self):
        """Update the card count by counting the cards again"""
        self._card_count

        for kw in self.card_count.keys():
            self.card_count[kw]['num_lines']  = self.card_lines[kw]


    def append_keyword(self, kw, data, count=0):
        kw_start = self.card_count['kw']

        pass


if __name__ == '__main__':
    c = KeyFile(r'E:\Github\dlib\test\check1.k')
    # print(c.cards)
    c.add_keyword("*Check", 1)
    c.add_keyword("*CHeck", 2)
