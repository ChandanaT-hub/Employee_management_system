from django.db import models

# Create your models here.
class book(models.Model):
    b_name=models.CharField(max_length=200)
    a_name=models.CharField(max_length=200)
    cost=models.IntegerField()

    def __str__(self):
        return self.b_name

