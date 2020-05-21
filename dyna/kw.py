class KeyWd(object):

    def __init__(self, keyword: str, data: list) -> None:
        if  '*' not in keyword:
            raise ValueError('keyword argument must contain * at start')
        self.kwd = keyword
        self.data = data
        self.number = len(self.data)

    def __repr__(self):
        return f"The keyword object for keyword {self.kwd}"

    def append_line(self, line: str, id: int):
        return self.data[id].append(line)

    def delete_lineby_location(self, location: int, id: int):
        self.data[id].pop(location)

    def delete_lineby_match(self, line: str, id: int):
        self.data[id].remove(line)


if __name__ == '__main__':
    x =[['       1               0               0               0       0       0',
         '       2            0.15               0             5.4       0       0'],
        ['       1               0               0               0       0       0',
         '       2            0.15               0             5.4       0       0']
        ]

    c = kw('*NODE', x)

