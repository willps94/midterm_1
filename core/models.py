from django.db import models

# Create your models here.
class Question(models.Model):
   name = models.CharField(max_length=300)
   email = models.CharField(max_length=300)
   message = models.TextField(null=True, blank=True)

   def __unicode__(self):
     return self.name