from django.db import models

class Cafe(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=250, unique=True, null=False)
    map_url = models.CharField(max_length=250, null=False)
    img_url = models.CharField(max_length=250,null=False)
    location = models.CharField(max_length=250,null=False)
    seats = models.CharField(max_length=250,null=False)
    has_toilet = models.BooleanField(null=False)
    has_wifi = models.BooleanField(null=False)
    has_sockets = models.BooleanField(null=False)
    can_take_calls = models.BooleanField(null=False)
    coffee_price = models.CharField(max_length=250,null=False)

    def __str__(self):
        return self.name 


