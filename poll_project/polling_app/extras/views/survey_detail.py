from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ResponseForm

class SurveyDetail(View):
    form_class = ResponseForm
    template_name = 'polling_app/survey.html'
    initial = {}
    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request,self.template_name,{'form':form})

    