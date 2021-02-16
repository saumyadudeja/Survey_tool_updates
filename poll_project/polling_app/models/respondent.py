from django.db import models

class Respondent(models.Model):

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

    location = models.CharField(max_length=50,choices=LOCATION_CHOICES)
    age = models.IntegerField()
    gender = models.CharField(max_length=30,choices=GENDER_CHOICES)

    def __str__(self):
        #msg = 'The respondent is {}, {} years old and from {}'.format(self.gender,self.age,self.location)
        return self.id

    class meta:
        verbose_name = "respondent"
        verbose_name_plural = "respondents"
