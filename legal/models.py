from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Questions(models.Model):
    user = models.ForeignKey(User, default=1)
    question_id=models.CharField(max_length=250)
    question=models.CharField(max_length=10000)
    category=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('legal:index')

    def __str__(self):
        return self.question +' - ' + self.question_id

    
class Answers(models.Model):  
    question= models.ForeignKey(Questions, on_delete=models.CASCADE) 
    answer=models.CharField(max_length=10000)

    def __str__(self):
        return self.answer