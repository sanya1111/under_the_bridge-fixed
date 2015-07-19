from django.db import models
from random import choice
import json
import hashlib
from django.utils import timezone

class Advert(models.Model):        
    date = models.DateField()
    adress = models.CharField(max_length = 300)
#     coords = models.CharField(max_length = 300)
    coords_x = models.DecimalField(max_digits=30, decimal_places=5)
    coords_y = models.DecimalField(max_digits=30, decimal_places=5)
    content = models.CharField(max_length=1000)
    im_content = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)
    
class Human(models.Model):
    ADVERTS_LIMIT = 10     
    def get(id):
        result = Human.objects.filter(vk_id=id)
        if len(result) == 0:
            raise Exception("not found")
        return result[0]
    
    vk_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    ad_favor = models.ManyToManyField(Advert)
    ad_owner = models.ManyToManyField(Advert, related_name="owner")
        
    
    
