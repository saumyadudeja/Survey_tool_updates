from django import forms

class ScreeningForm(forms.Form):

    MALE="male"
    FEMALE="female"
    DIVERSE="diverse"

    GENDER_CHOICES=(
        (MALE,"Male"),
        (FEMALE,"Female"),
        (DIVERSE,"Diverse"),
    )

    location = forms.CharField(label='Location',max_length=50)
    age = forms.IntegerField(label='Age')
    gender = forms.CharField(max_length=30,choices=GENDER_CHOICES,label='Gender')