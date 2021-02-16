from polling_app.models.survey import Survey

from polling_app.models.category import Category
from polling_app.models.question import Question
from polling_app.models.respondent import Respondent
from polling_app.models.response import Response
from polling_app.models.answer import Answer
from polling_app.models.answerOption import AnswerOption

#from polling_app.models.surveyQuestion import SurveyQuestion

"""
Permit to import everything from survey.models without knowing the details.
"""

__all__ = ["Survey", "Category", "Question","Respondent", "Response", "Answer","AnswerOption"]
#"SurveyQuestion"
