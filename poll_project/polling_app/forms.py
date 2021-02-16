from django import forms
from polling_app.models.respondent import Respondent
from polling_app.models.survey import Survey
from polling_app.models.category import Category
from polling_app.models.question import Question
from polling_app.models.response import Response
from polling_app.models.answerOption import AnswerOption
from django.shortcuts import Http404, get_object_or_404
import uuid


class ScreeningForm(forms.ModelForm):

    MALE="male"
    FEMALE="female"
    DIVERSE="diverse"

    GENDER_CHOICES=(
        (MALE,"Male"),
        (FEMALE,"Female"),
        (DIVERSE,"Diverse"),
    )

    GERMANY="germany"
    AUSTRIA="austria"
    SWITZERLAND="switzerland"
    FRANCE="france"

    LOCATION_CHOICES=(
        (GERMANY,"Germany"),
        (AUSTRIA,"Austria"),
        (SWITZERLAND,"Switzerland"),
        (FRANCE,"France"),
    )

    location = forms.ChoiceField(label='Location',choices=LOCATION_CHOICES)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER_CHOICES,label='Gender')

    class Meta:
        model = Respondent
        fields = ['age','gender','location']


class ResponseForm(forms.ModelForm):

    FIELDS = {
        Question.TEXT : forms.CharField,
        Question.SINGLE_CHOICE: forms.ChoiceField,
        Question.DATE: forms.DateField,
        Question.MULTIPLE_CHOICE: forms.MultipleChoiceField,
        Question.STATED_PREFERENCE: forms.ChoiceField,
        # Question.AnswerOption: forms.ChoiceField
    }

    WIDGETS = {
      	Question.TEXT: forms.TextInput,
        Question.SINGLE_CHOICE: forms.RadioSelect,
        Question.DATE: forms.DateInput,
        Question.MULTIPLE_CHOICE: forms.CheckboxSelectMultiple,
        Question.STATED_PREFERENCE: forms.RadioSelect,
        # Question.AnswerOption: forms.RadioSelect
    }

    class Meta:
        model = Response
        fields = ()

    def __init__(self, *args, **kwargs):
        self.survey = kwargs.pop("survey")
        self.respondent = kwargs.pop("respondent")

        super(ResponseForm,self).__init__(*args,**kwargs)
        self.interview_uuid = uuid.uuid4().hex
        #prefetch later
        self.response = False
        self.answers = False
        self.choices = False
        # self.get_question_choices=kwargs.get('choices')
        # self.answerOptions = True
        # kwargs["answerOptions"] = self.answerOptions(**kwargs)
        # print("choices")
        # print(self.choices)
        print('kwars data')
        print(kwargs.get('data'))
        self.add_questions(kwargs.get("data"))
        # if self.response is not None:
        #     for name in self.fields.keys():
        #         self.fields[name].widget.attrs["disabled"] = False

    def add_questions(self, data):
        for i, question in enumerate(self.survey.related_question.all().order_by("order")):
            print('question')
            print(question)
            self.add_question(question)
            #self.get_question_choices(question)

    def get_question_widget(self, question, **kwargs):
        """ Return the widget we should use for a question.

        :param Question question: The question
        :rtype: django.forms.widget or None """
        try:
            return self.WIDGETS[question.type]
        except KeyError:
            return None

    def get_question_choices(self, question):
        """ Return the choices we should use for a question."""
        choice_list = []
        if question.type not in [Question.TEXT,Question.DATE]:
            for option in AnswerOption.objects.filter(question=question).prefetch_related("question"):
                choice_list.append(option)
        #choices = tuple(choice_list)

        return choice_list

    def get_question_choices_new(self, question, **kwargs):
        choice_list=[]
        kwargs['choices']=self.get_question_choices(question)
        # for key,value in kwargs['choices'].items():
        #     choice_list.append(kwargs['choices'].value)
        # choices = tuple(choice_list)
        # print(kwargs['choices'])
        #print('hello'.kwargs['choices'])
        return kwargs['choices']

    def get_question_field(self, question, **kwargs):
        """ Return the field we should use in our form."""
        try:
            return self.FIELDS[question.type](**kwargs)
        except KeyError:
            return None
        print("get_question_field ran well")

    def add_question(self, question):
        """ Add a question to the form.

        :param Question question: The question to add.
        :param dict data: The pre-existing values from a post request. """

        #kwargs = {"label": question.text, "required": question.required}
        choices = self.get_question_choices_new(question)
        # print('choi')
        # print(choices.key)
        # print(choices.keys)
        self.choices= choices
        # print(choices)

        # print('choices arg')
        # print(self.choices)
        options=[]

        for answer in self.choices:
            option = str(answer)
            choicer=(option,option)
            options.append(choicer)


        answer_choice=tuple(options)

        if question.type == Question.TEXT:
            kwargs = {"label": question.text,"required": question.required}
        elif question.type == Question.DATE:
            kwargs = {"label": question.text,"required": question.required}
        else:
            kwargs = {"label": question.text,"required": question.required,'choices':answer_choice}

        # kwargs['choices'] = self.choices
        #,"choices":choices

        # kwargs["answerOptions"] = question.answerOptions
        # print(question.answerOptions)
        widget = self.get_question_widget(question)
                #if widget:
            #kwargs["widget"] = widget
        field = self.get_question_field(question, **kwargs)
        # print('printing field')
        # print(question.type)
        if question.type == Question.DATE:
            field.widget.attrs["class"] = "number"


        self.fields["question_%d" % question.id] = field


    def save(self,commit=True):
        """save the response object"""
        if response is None:
            response = super(ResponseForm,self).save(commit=False)
        response.survey = self.survey
        response.interview_uuid = self.uuid
        response.respondent = self.respondent
        response.save()
        data = {"survey_id": response.survey.id, "interview_uuid": response.interview_uuid, "responses":[]}
        for field_name, field_value in list(self.cleaned_data.items()):
            if field_name.startswith("question_"):
                # warning: this way of extracting the id is very fragile and
                # entirely dependent on the way the question_id is encoded in
                # the field name in the __init__ method of this form class.
                q_id = int(field_name.split("_")[1])
                question = Question.objects.get(pk=q_id)
                if self.get_question_choices(question)!=[]:
                    answer = Answer(answerOption(question=question))
                answer.body = field_value
                data["responses"].append((answer.body))
                answer.response = response
                answer.save()
        survey_completed.send(sender=Response, instance=response, data=data)
        return response






    #def get_question_initial(self, question, data):
        #""" Get the initial value that we should use in the Form"""
