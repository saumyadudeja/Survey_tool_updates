from django.views.generic import TemplateView
#from polling_app.models import 



class IndexView(TemplateView):
    template_name = "polling_app/home.html"
    #context = {}
    #def __init__(self,request):
        #return render(request,template_name,context) 
    