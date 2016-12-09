from django.db import models

class summary(models.Model):
    summary_list = models.CharField(max_length=200)
    article = models.DateTimeField('date published')

class searchTwitter(models.Model):
    tweets = models.ForeignKey(summary, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


