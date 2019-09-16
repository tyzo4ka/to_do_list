from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class TaskForm(forms.Form):
    description = forms.CharField(max_length=500, required=True, label="Description")
    detailed = forms.CharField(max_length=3000, required=False, label="Details", widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Status")
    complete_before = forms.DateField(required=False, label="Complete before")
