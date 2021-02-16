from django.db import models

from polling_app.models.question import Question


class AnswerOption(models.Model):
    option = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name="Questions",related_name="answerOptions")
    key_name = models.CharField(max_length=200,default=None,blank=True)
    value = models.CharField(max_length=200,default=None,blank=True)
    image = models.ImageField(default=None,blank=True)

    def __init__(self, *args, **kwargs):
        try:
            question = Question.objects.get(pk=kwargs["question_id"])
        except KeyError:
            question = kwargs.get("question")
        option = kwargs.get("option")
        super(AnswerOption, self).__init__(*args, **kwargs)

    #@property
    def get_options_related_to_question(self, question):
        choices_list = []
        for choice in self.objects.filter(question=question):
            choices_list.append(choice)
        return tuple(choices_list)

    def __str__(self):
        return self.option


