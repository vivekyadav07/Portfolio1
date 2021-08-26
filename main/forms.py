from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,default='',blank=True,null=True)
    email = models.CharField(max_length=70, null=True, blank=True,)
    subject = models.CharField(max_length=12,default='',blank=True,null=True)
    message = models.TextField(max_length=12,default='',blank=True,null=True)
    date = models.DateField(max_length=12,default='',blank=True,null=True)

    def __str__(self):
        return self.name
    