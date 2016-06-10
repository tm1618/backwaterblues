from django import forms
from django.forms.fields import TimeField
from models import Volunteer, Task, Day, Type


class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = ('name', 'email', 'phone')


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'volunteers', 'day', 'time', 'hours')


class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ("day",)


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ("name",)