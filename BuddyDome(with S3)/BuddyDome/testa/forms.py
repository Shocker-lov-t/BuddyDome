from django import forms
from .models import Course,Blog
from .models import Requestcourse
class CourseForm(forms.ModelForm):
    contributor = 'yes'
    nocontri= 'no'
    existing_contributor = [
        (contributor , 'yes'),
        (nocontri , 'no')
    ]
    existing_contributor = forms.ChoiceField(required=True, choices=existing_contributor)

    class Meta:
        model = Course

        fields = ('existing_contributor','n','e','t', 'a', 'l' , 'cr','re'  ,'resume')


class RequestForm(forms.ModelForm):
    class Meta:
        model= Requestcourse

        fields= ('name','email','title', 'area', 'level' , 'create','reference','impact')
        
        
               
class BlogForm(forms.ModelForm):
    nam=forms.CharField(label="Name",  required=True)
    ema=forms.CharField(label="Email",  required=True)
    tit=forms.CharField(label="Title",  required=True)
    af=forms.CharField(label="Field(e.g. AWS,GCP,etc.)",  required=False)
    rel=forms.CharField(label="Blog Link",  required=True)
     
    contributor = 'contributor'
    student='student'
    employee='employee'
    designation = [
        (contributor , 'contributor'),
        (student,'student'),
        (employee,'employee'),
    ]
    designation = forms.ChoiceField(required=True, choices=designation)

    class Meta:
        model = Blog
        nam=forms.CharField(max_length=250,required=True)
        fields = ('designation','nam','ema','tit', 'af' , 'crp','rel')
        