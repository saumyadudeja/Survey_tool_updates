"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.views.generic.base import RedirectView

    
import polling_app.views as poll_views
#from django.contrib.auth.views import LoginView as login_views
from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.urls.base import reverse
from polling_app.views import Screening




urlpatterns = [
    path('login/', RedirectView.as_view(url='/admin'), name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('', poll_views.home, name='home'),
    path('screening/', poll_views.Screening.as_view(), name='screening'),
    #path('polling_app/',include('polling_app.urls')),
    path('survey/<int:id>',poll_views.SurveyDetail.as_view(), name='survey_detail' ),
    #path('survey/<int:pk>',poll_views.SurveyDetail.as_view(), name='survey_detail' )  
    ]
