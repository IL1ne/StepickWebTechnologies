from django.forms import ModelForm, widgets
from qa.models import Question, Answer


class AskForm(ModelForm):

    class Meta:

        model = Question
        fields = ['title', 'text', ]


class AnswerForm(ModelForm):

    class Meta:

        model = Answer
        fields = ['text', 'question', ]