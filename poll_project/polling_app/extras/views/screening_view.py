from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from polling_app.models.respondent import Respondent
from polling_app.forms import ScreeningForm

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
            form.save()
            return HttpResponseRedirect('home')
        return render(request, self.template_name,context)
        


        # if request.method=='POST':
        #     form=ScreeningForm(request.POST)
        #     if form.is_valid():
                # age = form.cleaned_data['age']
                # gender = form.cleaned_data['gender']
                # location = form.cleaned_data['location']
                # form.save()

        # else:
        #     form=ScreeningForm()
        # context={'form':form}
        # #context['form']=ScreeningForm()
        # print(request.POST) 
        # return render(request,template_name,context)