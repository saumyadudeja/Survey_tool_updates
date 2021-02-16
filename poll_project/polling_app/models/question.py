from django.db import models
from polling_app.models.category import Category
#from .answerOption import AnswerOption

class Question(models.Model):

    TEXT="text"
    SINGLE_CHOICE="single_choice"
    DATE="date"
    MULTIPLE_CHOICE="multiple_choice"
    STATED_PREFERENCE="stated_preference"

    QUESTION_TYPES = (
        (TEXT,"Text"),
        (SINGLE_CHOICE,"Single Choice"),
        (DATE,"Date"),
        (MULTIPLE_CHOICE,"Multiple Choice"),
        (STATED_PREFERENCE,"Stated Preference"),
    )

    text = models.TextField("Text")
    required = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    order = models.IntegerField("Order",default=0)
    type = models.CharField(max_length=200,choices=QUESTION_TYPES,default=text)

    class Meta:
        ordering = ['text']
        verbose_name = "question"
        verbose_name_plural = "questions"

    # def get_choices(self):
    #     """
    #     Parse the choices field and return a tuple formatted appropriately
    #     for the 'choices' argument of a form widget.
    #     """
    #     choices_list = []
    #     for choice in AnswerOption.objects.filter(self.objects.get(self.id)):
    # #self.AnswerOption.all():

    #     #AnswerOption.objects.filter(self.objects.get(self.id)):
    #         choices_list.append((slugify(choice, allow_unicode=True), choice))
    #     choices_tuple = tuple(choices_list)
    #     return choices_tuple
    # @property
    # def answers_as_text(self):
    #     """ Return answers as a list of text.

    #     :rtype: List """
    #     answers_as_text = []
    #     for answer_opt in self.answers.all():
    #         for value in answer.values:
    #             answers_as_text.append(value)
    #     return answers_as_text

    # def get_clean_choices(self,answerOption):
    #     """ Return list of choices """

    #     choices_list = []
    #     for choice in answerOption.objects.filter(question=self):
    #         choices_list.append(choice)
    #     return choices_list

    # def get_choices(self):
    #     """
    #     Parse the choices field and return a tuple formatted appropriately
    #     for the 'choices' argument of a form widget.
    #     """
    #     choices_list = []
    #     for choice in self.get_clean_choices():
    #         choices_list.append((slugify(choice, allow_unicode=True), choice))
    #     choices_tuple = tuple(choices_list)
    #     return choices_tuple

    def __str__(self):
        msg = "Question '{}' ".format(self.text)
        if self.required:
            msg += "(*) "
        #msg += "{}".format(self.get_clean_choices())
        return msg
