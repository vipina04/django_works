from django import forms
from django.contrib.auth.forms import UserCreationForm

from classroom_app.models import Login, Student, Complaint, Notifications


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'roll_no', 'college_name', 'phone_number')


class ComplaintRegister(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Complaint
        fields = ('subject', 'complaint', 'date')

class Notification_add(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Notifications
        fields = ('date','subject','notification')
