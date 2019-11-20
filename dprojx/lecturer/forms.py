# dappx/forms.py
from django import forms
from lecturer.models import LecturerInfo
from django.contrib.auth.models import User
class LecturerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class LecturerInfoForm(forms.ModelForm):
    class Meta():
        model = LecturerInfo
        fields = ('name', 'college', 'department', 'lecturer_id')