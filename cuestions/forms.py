__author__ = 'mrk2'
from django import forms


class UserResponseForm(forms.Form):
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()