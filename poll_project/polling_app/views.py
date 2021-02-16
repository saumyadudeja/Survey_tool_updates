from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import csv
from polling_app.forms import ScreeningForm,ResponseForm
from django.shortcuts import get_object_or_404
from django.views.generic import View, DetailView, TemplateView
from polling_app.models.respondent import Respondent
from polling_app.models.survey import Survey
from polling_app.models.question import Question
from polling_app.models.answerOption import AnswerOption
from collections import defaultdict
from django.http import Http404
from polling_app.decorators import survey_available
#from polling_app.forms import SurveyForm



def export_view(modelAdmin,request,queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="responses.csv"'

    writer = csv.writer(response)

    for i in range(1,Respondent.objects.count()+1):
        writer.writerow([i])
        #res=Respondent.objects.filter(id=i)
    writer.writerow(Respondent.objects.all())
    return response

def home(request):
    context = {}
    return render(request, 'polling_app/home.html', context)

class Screening(View):
    template_name = 'polling_app/screening.html'
    form_class = ScreeningForm
    initial = {'key':'value'}

    def get(self,request, *args,**kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form':form}

        return render(request, self.template_name,context)

    def post(self,request, *args,**kwargs):
        form = self.form_class(request.POST)
        context = {'form':form}
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            location = form.cleaned_data['location']
            try:
                form.save()
            except:
                raise Http404("Overflow Error. Integer out of range")
            #return HttpResponseRedirect('survey-detail')
        return render(request, self.template_name,context)


class SurveyDetail(View):
    #@survey_available
    form_class = ResponseForm
    #initial = {'key':'value'}
    template_name = "polling_app/survey.html"

    @survey_available
    def get(self,request, *args,**kwargs):
        #survey_id = self.kwargs.get('id',None)
        survey = kwargs.get("survey")
        # print(survey)
        respondent = kwargs.get("respondent")
        # print(respondent) None
        # print(survey.id)
        template_name = "polling_app/survey.html"
        form = ResponseForm(survey=survey,respondent=respondent)

        asset_context = {
            # If any of the widgets of the current form has a "date" class, flatpickr will be loaded into the template
            "flatpickr": any([field.widget.attrs.get("class") == "date" for _, field in form.fields.items()])
        }
        context = {
            "response_form": form,
            "survey": survey,
            "asset_context": asset_context,
        }

        print('response form')
        print(form)
        # print(context['response_form'])

        return render(request,template_name,context)

    @survey_available
    def post(self,request, *args,**kwargs):
        survey = kwargs.get("survey")
        form = ResponseForm(request.POST, survey=survey)
        #, respondent=self.respondent)
        #form = self.form_class(request.POST)
        context = {"response_form": form, "survey": survey}

        if form.is_valid():
            form.save()
        return render(request, self.template_name,context)

class SurveyCompleted(TemplateView):

    template_name = "survey/completed.html"

    def get_context_data(self, **kwargs):
        context = {}
        survey = get_object_or_404(Survey, isPublished=True, id=kwargs["id"])
        context["survey"] = survey
        return context
