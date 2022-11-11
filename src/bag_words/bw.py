import math


class BagWords:
    def __init__(self, ):

        self.classification:int | str = ''
        self.vocabulary:dict[str] = {}
        self.log_priority:float = 0.0
        self.documents_counter:int = 0
        self.likelihood:dict[str, float] = {}
        self.bigdoc:list = []
    
    def insert_word(self, word:str):
        if word in self.bag:
            self.vocabulary[word] += 1
        else:
            self.vocabulary[word] = 1
    
    def calculate_log_priority(self, total_documents:int):
        self.log_priority = math.log(self.documents_counter/total_documents)
    
    def calculate_loglikelihood(self, general_vocabulary_size):
        for word in self.vocabulary:
            frequency = self.vocabulary[word]

            self.vocabulary[word] = math.log(frequency+1/general_vocabulary_size+1)

