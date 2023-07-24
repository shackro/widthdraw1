from django.db import models

# Create your models here.
class student(models.Model):
    name =models.CharField(max_length=30,blank=False, null=False)
    school =models.CharField(max_length=20,blank=False, null=False)
    theclass =models.CharField(max_length=12,blank=False, null=False)
    email =models.EmailField()
    number =models.IntegerField()

    def __str__(self):
        return self.name
