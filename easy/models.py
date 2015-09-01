from django.db import models
from random import choice
import json
import hashlib
from django.utils import timezone


class Advert(models.Model):        
    date = models.DateField()
    adress = models.CharField(max_length = 300)
    OWNER_TYPE_INFO = ( ('OWNER', False), ('RENTER', True))
    owner_type = models.BooleanField(choices = OWNER_TYPE_INFO, default='OWNER')
    coords_x = models.DecimalField(max_digits=30, decimal_places=5)
    coords_y = models.DecimalField(max_digits=30, decimal_places=5)
    content = models.CharField(max_length=1000)
    im_content = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)
    
class Human(models.Model):     
    def get(id):
        result = Human.objects.filter(vk_id=id)
        if len(result) == 0:
            raise Exception("not found")
        return result[0]
    
    def get_human_or_create(request, id=None):
        if id == None:
            id = request.session.get("id")
        try:
            return Human.get(id)
        except:
            ret = Human(vk_id=id, name="")
            ret.save()
            return ret
    
    def get_human_adverts(request, id=None):
        return Human.get_human_or_create(request, id).ad_owner.all()
        
    def get_coords_list(self):
        return json.loads(self.bum_coords)
    
    def set_coords_list(self, obj):
        self.bum_coords = json.dumps(obj)
    
        
    vk_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    ad_favor = models.ManyToManyField(Advert)
    ad_owner = models.ManyToManyField(Advert, related_name="owner")
    ad_rent = models.ManyToManyField(Advert, related_name="rent")
    bum_coords = models.CharField(max_length=300)
        
    
    
