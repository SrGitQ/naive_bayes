from unittest import TestCase
from src.na_ba import NaiveBayes

class TestClassifier(TestCase):

    def test_bag_words(self):
        train_1 = {'text':'Hoy hice la tarea, porque soy una persona muy responsable, me gusta hacer tarea, hacer la taarea es bueno, creo que hacer tarea me relaja', 'status':'positive'}
        train_2 = {'text':'Hoy no hice tarea, no me gusta, aburrido', 'status':'negative'}

        train_case = [train_1, train_2]

        case_1 = {'text':'hacer la tarea es bueno', 'status':'positive'}

        obj = NaiveBayes()
        assert isinstance(obj, NaiveBayes)
