from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    def wtf(self):
        return "OK BROU"
    wtf.admin_order_field = 'pub_date'
    wtf.str="okok"
    wtf.short_description = 'WTF?'
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
