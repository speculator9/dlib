path = r'E:\Github\dlib\test\check.k'

# from
class KeyFile(object):

    def __init__(self, path):
        self.path = path

    @property
    def cards(self):
        """Method returns the cards in the existing deck as list"""
        crds = []

        for line in self.keydata:
            if "*" in line:
                crds.append(line.strip())

        return crds

    @property
    def keydata(self):
        """Method returns the data in text file as list of lines"""
        with open(path) as file:
            data = file.readlines()
        return data

    @property
    def nnodes(self):

        pass


if __name__ =='__main__':
    c = KeyFile( r'E:\Github\dlib\test\check.k')
    print(c.cards)
