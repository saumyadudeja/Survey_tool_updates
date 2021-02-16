from django.test import TestCase
from polling_app.models.survey import Survey
from polling_app.models.question import Question
from polling_app.models.answerOption import AnswerOption
from polling_app.models.respondent import Respondent
from polling_app.models.answer import Answer
from polling_app.models.category import Category
from polling_app.models.response import Response
from datetime import datetime

class TestModels(TestCase):

    def setUp(self):
        pass
        
    def test_model_for_accuracy(self):
        category1 = Category()
        category1.title = "Demographics"
        category1.description = "The demographic questions belong to this category"
        category1=Category.objects.create(title=category1.title,
                                        description=category1.description)
        self.assertEquals(category1.__str__(),category1.title)

        question1 = Question()
        question1.text = "Employment status"
        question1.required = True
        question1.category= category1
        question1.type = "Single Choice"
        question1=Question.objects.create(text = question1.text,
                                        required= question1.required,
                                        category=question1.category,
                                        type=question1.type)
        self.assertEquals(question1.__str__(),question1.text)

        survey1 = Survey()
        survey1.name = "Test Survey"
        survey1.isPublished = True
        survey1.publishDate = datetime.now()
        survey1.expiryDate = datetime.now()
        
        survey1=Survey.objects.create(name=survey1.name,
                                        isPublished=survey1.isPublished,
                                        publishDate=survey1.publishDate,
                                        expiryDate=survey1.expiryDate)
        survey1.related_question.add(question1)

        answeroption1 = AnswerOption()
        answeroption1.option = 'Employed'
        answeroption1.question = question1
        answeroption1.key_name = 'null'
        answeroption1.value = 'null'
        answeroption1.image = 'null'
        answeroption1=AnswerOption.objects.create(option=answeroption1.option,
                                            question=answeroption1.question,
                                            key_name=answeroption1.key_name,
                                            value=answeroption1.value,
                                            image=answeroption1.image)

        answeroption2 = AnswerOption()
        answeroption2.option = 'Unemployed'
        answeroption2.question = question1
        answeroption2.key_name = 'null'
        answeroption2.value = 'null'
        answeroption2.image = 'null'
        answeroption2= AnswerOption.objects.create(option=answeroption2.option,
                                            question=answeroption2.question,
                                            key_name=answeroption2.key_name,
                                            value=answeroption2.value,
                                            image=answeroption2.image)

        self.assertEquals(answeroption1.__str__(),answeroption1.option)
        self.assertEquals(answeroption2.__str__(),answeroption2.option)

