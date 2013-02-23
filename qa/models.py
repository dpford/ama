from django import forms
from django.db import models

class Ama(models.Model):
    title = models.CharField(max_length=300)
    ama_id = models.CharField(max_length=15)
    orig_poster = models.CharField(max_length=50)
    created = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.title

class Qa(models.Model):
    ama = models.ForeignKey(Ama)
    ups = models.IntegerField(max_length=7)
    question = models.TextField()
    answer = models.TextField()
    asker = models.CharField(max_length=50)
    answered = models.CharField(max_length=20)
    questid = models.CharField(max_length=20)
    answerid = models.CharField(max_length=20)
    def __unicode__(self):
        return self.asker

class SearchForm(forms.Form):
    amaurl = forms.CharField(max_length=300)