from django.forms import ModelForm
from qa.models import Question, Answer
from django import forms

# class AskForm(ModelForm):

#     class Meta:

#         model = Question
#         fields = ['title', 'text', ]

class AnswerForm(ModelForm):

    class Meta:

        model = Answer
        fields = ['text', ]


class AskForm(forms.Form):

    title = forms.CharField(max_length=600, required=True)
    text = forms.CharField(max_length=3000, required=True)

    class Meta:
        model = Question
        fields = ['title', 'text', ]


class SignUpForm(forms.Form):

    """docstring for registrationForm"""

    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

