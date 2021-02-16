from django.db import models

from polling_app.models.respondent import Respondent
from polling_app.models.survey import Survey
import uuid


class Response(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    respondent = models.ForeignKey(Respondent, null=True, on_delete=models.SET_NULL)
    interview_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "Set of answers to surveys"
        verbose_name_plural = "Sets of answers to surveys"


    def __str__(self):
        return self.interview_uuid
    
    


