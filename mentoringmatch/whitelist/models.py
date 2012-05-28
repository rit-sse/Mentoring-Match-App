from django.db import models

# Create your models here.
class Mentor(models.Model):
  dce = models.CharField(max_length=7)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
