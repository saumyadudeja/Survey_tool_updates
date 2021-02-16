from django.test import SimpleTestCase
from django.urls import reverse, resolve
from polling_app.views import home, Screening,SurveyDetail

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_screening_url_is_resolved(self):
        url = reverse('screening')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,Screening)

    def test_survey_detail_url_is_resolved(self):
        url = reverse('survey_detail')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,SurveyDetail)