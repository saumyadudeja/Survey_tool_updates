from django.db import models
from datetime import timedelta,date
from django.utils.timezone import now
#from polling_app.models.surveyQuestion import SurveyQuestion
from polling_app.models.question import Question

class Survey(models.Model):
    name = models.CharField(max_length=400)
    isPublished = models.BooleanField('Published?')
    publishDate = models.DateField('publication date',default=now)
    expiryDate = models.DateField('expiry date',default=date.today() + timedelta(days=10))
    related_question = models.ManyToManyField(Question)
    #,through='SurveyQuestion')

    class Meta:
        ordering = ['name']
        verbose_name = "survey"
        verbose_name_plural = "surveys"

    def __str__(self):
        return str(self.name)

    @property
    def safe_name(self):
        return self.name.replace(" ", "_").encode("utf-8").decode("ISO-8859-1")
    
    def get_absolute_url(self):
        return reverse("survey_detail", kwargs={"id": self.pk})

# class SurveyQuestion(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, blank=True, null=True,related_name='survey_no')
#     question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='question_no')
    
