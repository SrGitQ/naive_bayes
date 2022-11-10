

class BagWords:
    def __init__(self, ):

        self.classification:int | str = ''
        self.bag:dict[str] = {}
    
    def insert_word(self, word:str):
        if word in self.bag:
            self.bag[word] += 1
        else:
            self.bag[word] = 1

