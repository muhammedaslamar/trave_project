from django.db import models
class place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class pakages(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='picture')
    time_day= models.IntegerField()
    time_night= models.IntegerField()
    star= models.IntegerField()
    reviews= models.IntegerField()
    price = models.IntegerField()