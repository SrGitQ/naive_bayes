from bag_words.bw import BagWords


class NaiveBayes:
    def __init__(self, ):
        print('Naive Bayes object created.')
        
        self.classifications:dict[str, 'BagWords'] = {}
        self.raw_data = []
        self.total_documents:int = 0
        self.general_vocabulary:list = []
    
    def fit_model(self, data:list[dict[str, str]]):
        self.__set_classifications(data)

        [self.classifications[class_].calculate_log_priority() for class_ in self.classifications]

        for class_ in self.classifications:
            for word, freq in self.classifications[class_].vocabulary:
                self.general_vocabulary.append(word)

        [self.classifications[class_].calculate_loglikelihood(len(self.general_vocabulary)) for class_ in self.classifications]

    
    def predict_data(self, data:dict[str, str]):
        pass

    def __set_classifications(self, data:list[dict[str, str]]):
        self.total_documents = len(data)
        classifications:dict[str, 'BagWords'] = {}

        for text, status in data: # should be cleaned
            splitted_data = text.split(' ')

            if status not in classifications:
                classifications[status] = BagWords()
                classifications[status].classification = status
            
            if len(splitted_data) == 0:
                pass
            
            [classifications[status].insert_word(word) for word in splitted_data]
            classifications[status].documents_counter += 1
            classifications[status].bigdoc.append(text)

        self.classifications = classifications

    

