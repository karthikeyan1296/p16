from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def validate_name(name):
    m=re.match('[a-zA-Z]+',name)
    if m.group()!=name:
        raise ValidationError("Name is Not Valid")
    return name


class sampleForm(forms.Form):

    name=forms.CharField(max_length=200,required=True,label="NAME :",
    validators=[validate_name])

    ip_address=forms.CharField(max_length=100,required=True,
    validators=[validators.validate_ipv4_address])

    email=forms.EmailField(max_length=200,required=True,label="EMAIL :",
    validators=[validators.MinLengthValidator(10)])

    confirm_email=forms.EmailField(max_length=200,required=True,label="CONFIRM EMAIL :",
    validators=[validators.MinLengthValidator(10)])

    pwd=forms.CharField(max_length=200,required=True,label="Password :",
    widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
    
    profile_pic=forms.ImageField(max_length=200,required=True,label="Profile Pic :")

#    def clean(self,*args,**kwargs):
#       cleaned_data=super().clean() #getting all the data that is filled in the form
#       email=cleaned_data.get("email")
#       cemail=cleaned_data.get("confirm_email")
#       if email!=cemail:
#           raise ValidationError("Emails are nat same")
#        return cleaned_data


    def clean(self,*args,**kwargs):
        cleaned_data=super().clean() #getting all the data that is filled in the form
        email=cleaned_data.get("email")
        cemail=cleaned_data.get("confirm_email")
        if email==cemail:
            return cleaned_data
        self.add_error('confirm_email',"Incorrect email")#this method will decide to which field we need to show the error
        #self.add_error("fieldname",error message)