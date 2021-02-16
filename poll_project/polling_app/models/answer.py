from django.db import models
from polling_app.models.response import Response
from polling_app.models.answerOption import AnswerOption
from polling_app.models.question import Question


class Answer(models.Model):
    answerOption = models.ForeignKey(AnswerOption,on_delete=models.CASCADE)
    body = models.CharField(max_length=20)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id