from django.db import models


# Create your models here.
class show(models.Model):
    name = models.CharField(max_length=56)
    age = models.IntegerField()
    add = models.TextField()

    def __str__(self):
        return self.add


class kim(models.Model):
    name = models.CharField(max_length=89)
    age = models.IntegerField()
    addr = models.TextField()


class bob(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='img')
    des = models.TextField()

class one(models.Model):
    image=models.ImageField(upload_to='img')
    des=models.TextField()
    date=models.DateField()
