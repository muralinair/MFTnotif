from django import forms
#from django.contrib.auth.models import User
from userpage.models import UserProfileInfo

#class UserForm(forms.ModelForm):
#    password=forms.CharField(widget=forms.PasswordInput())
#    confirmPassword=forms.CharField(widget=forms.PasswordInput())
#    category=forms.ChoiceField(required=True,choices=[('Customer','Customer'),('Retailer','Retailer')],widget=forms.RadioSelect())
#    class Meta():
#        model=User
#        fields=("username","email","password")
#    
#    def clean(self):
#        cleaned_data = super(UserForm, self).clean()
#        password = cleaned_data.get("password")
#        confirm_password = cleaned_data.get("confirmPassword")
#
#        if password != confirm_password:
#            print("password: "+password)
#            print("confirm_password: "+password)
#            raise forms.ValidationError(
#                "password and confirm_password does not match"
#            )
#
#class UserProfileInfoForm(forms.ModelForm):
#    class Meta():
#        model=UserProfileInfo
#        fields=("category",)

class UserForm(forms.Form):
    username=forms.CharField(widget=forms.CharField())
    email=forms.CharField(widget=forms.CharField())
    password=forms.CharField(widget=forms.PasswordInput())
    confirmPassword=forms.CharField(widget=forms.PasswordInput())
    category=forms.ChoiceField(required=True,choices=[('Customer','Customer'),('Retailer','Retailer')],widget=forms.RadioSelect())
    #class Meta():
    #    model=UserProfileInfo
    #    fields=("username","email","password")
    
    #def clean(self):
    #    cleaned_data = super(UserForm, self).clean()
    #    password = cleaned_data.get("password")
    #    confirm_password = cleaned_data.get("confirmPassword")
    #
    #    if password != confirm_password:
    #        print("password: "+password)
    #        print("confirm_password: "+password)
    #        raise forms.ValidationError(
    #            "password and confirm_password does not match"
    #        )