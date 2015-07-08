from django.db import models
from random import choice
import json

class Advert(models.Model):
    ad_date = models.DateField()
    content = models.CharField(max_length=1000)
    im_content = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)
    
    
class Human(models.Model):
    vk_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    sex_choise = ( ( 'man', 0), 
                   ( 'woman', 1)
                 )
    sex = models.IntegerField(choices=sex_choise)
    ad_favor = models.ManyToManyField(Advert, related_name = 'ad_favor')
    ad_owner = models.ManyToManyField(Advert, related_name = 'ad_owner')
    
    
