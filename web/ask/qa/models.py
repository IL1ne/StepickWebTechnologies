from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):

    def new(self):
        return self.all().order_by('-added_at')

    def popular(self):
        return self.all().order_by('-rating')


class Question(models.Model):

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    objects = QuestionManager()


class Answer(models.Model):

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answer"

    def __str__(self):
        return '%s answer#%d' % (self.question.title, self.pk)
    """docstring for Answer"""

    text = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)
