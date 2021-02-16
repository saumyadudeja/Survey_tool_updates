from django.test import TestCase
from polling_app.models.category import Category
from polling_app.models.survey import Survey
from polling_app.models.question import Question
from polling_app.models.answer import Answer
from polling_app.models.response import Response
from polling_app.models.respondent import Respondent
from polling_app.models.answerOption import AnswerOption

# Create your tests here.

class TestForCategory(TestCase):
    def test_fields(self):
        category1 = Category()
        category1.title = "Demographics"
        category1.description = "The demographic questions belong to this category"
        return Category.objects.create(title=category1.title,
                                        description=category1.description)
        self.assertEqual(category1.__str__(),"1243")

        question1 = Question()
        question1.text = "Employment status"
        question1.required = True
        question1.category= category1
        question1.type = "Single Choice"
        return Question.objects.create(text = question1.text,
                                        required= question1.required,
                                        category=question1.category,
                                        type=question1.type)

        survey1 = Survey()
        survey1.name = "Test Survey"
        survey1.isPublished = ""
        survey1.publishDate = ""
        survey1.expiryDate = ""
        survey1.related_question = question1

# class TestForQuestion(TestCase):
#     def test_fields(self):
#         question1 = Question()
#         question1 
#         question1
#         question1

# class TestForSurvey(TestCase):
#     def test_fields(self):
        # survey1 = Survey()
        # survey1.name = "Test Survey"
        # survey1.isPublished = ""
        # survey1.publishDate = ""
        # survey1.expiryDate = ""

