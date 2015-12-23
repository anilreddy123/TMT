from django import forms
from .models import *


class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise models.ValidationError(("The two password fields did not match."))
        return self.cleaned_data



class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients

        fields = ['clientname']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ('',)




class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        exclude = ('',)


class User_TimesheetForm(forms.ModelForm):
    class Meta:
        model = User_Timesheet
        exclude = ('',)






