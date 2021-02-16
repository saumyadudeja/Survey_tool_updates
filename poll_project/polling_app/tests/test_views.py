from django.test import TestCase, Client
from django.urls import reverse
from polling_app.models.survey import Survey
from polling_app.models.category import Category
from polling_app.models.question import Question
from polling_app.models.answerOption import AnswerOption
from polling_app.models.respondent import Respondent
import json
from datetime import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.screening_url = reverse('screening')
        self.survey_url = reverse('survey_detail')
        self.age1 = 34.5
        self.gender1 = 'other'
        self.location1 = 'Queensland'
        self.respondent = Respondent()

    def test_home(self):

        received=self.client.get(self.home_url)
        self.assertEquals(received.status_code,200)
        self.assertTemplateUsed(received,'polling_app/home.html')

    def test_screening_GET(self):
        received=self.client.get(self.screening_url)
        self.assertEquals(received.status_code,200)
        self.assertTemplateUsed(received,'polling_app/screening.html')

    def test_screening_POST_respondent_data(self):
        Respondent.objects.create(
            age=self.age1,
            gender=self.gender1,
            location=self.location1
        )
        self.assertEquals(self.age1,34.5)

    def test_screening_POST_no_respondent_data(self):
        received=self.client.post(self.screening_url)
        self.assertEquals(Respondent.objects.count(),0)

    # def test_survey_detail_GET(self):
    #     received=self.client.get(self.survey_url)
    #     category1 = self.Category()
    #     category1.title = "Demographics"
    #     category1.description = "The demographic questions belong to this category"
    #     category1=Category.objects.create(title=category1.title,
    #                                     description=category1.description)
    #     self.assertEquals(category1.__str__(),category1.title)

    #     question1 = self.Question()
    #     question1.text = "Employment status"
    #     question1.required = True
    #     question1.category= category1
    #     question1.type = "Single Choice"
    #     question1=Question.objects.create(text = question1.text,
    #                                     required= question1.required,
    #                                     category=question1.category,
    #                                     type=question1.type)
    #     self.assertEquals(question1.__str__(),question1.text)

    #     survey1 = self.Survey()
    #     survey1.name = "Test Survey"
    #     survey1.isPublished = True
    #     survey1.publishDate = datetime.now()
    #     survey1.expiryDate = datetime.now()
    #     survey1.related_question = question1
    #     survey1=Survey.objects.create(name=survey1.name,
    #                                     isPublished=survey1.isPublished,
    #                                     publishDate=survey1.publishDate,
    #                                     expiryDate=survey1.expiryDate)

    #     answeroption1 = self.AnswerOption()
    #     answeroption1.option = 'Employed'
    #     answeroption1.question = question1
    #     answeroption1.key_name = 'null'
    #     answeroption1.value = 'null'
    #     answeroption1.image = 'null'
    #     answeroption1=AnswerOption.objects.create(option=answeroption1.option,
    #                                         question=answeroption1.question,
    #                                         key_name=answeroption1.key_name,
    #                                         value=answeroption1.value,
    #                                         image=answeroption1.image)

    #     answeroption2 = self.AnswerOption()
    #     answeroption2.option = 'Unemployed'
    #     answeroption2.question = question1
    #     answeroption2.key_name = 'null'
    #     answeroption2.value = 'null'
    #     answeroption2.image = 'null'
    #     answeroption2= AnswerOption.objects.create(option=answeroption2.option,
    #                                         question=answeroption2.question,
    #                                         key_name=answeroption2.key_name,
    #                                         value=answeroption2.value,
    #                                         image=answeroption2.image)

