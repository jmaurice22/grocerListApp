from django.db import models

# Create your models here.

class Fruits(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
   
    def __str__(self):
        return self.name
        return self.quantity

  


