import re
from django.db import models
from django.core.exceptions import ValidationError

#Symbolizes a mentor in the whitelist
class Mentor(models.Model):
  dce = models.CharField(max_length=7)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  
  #validates Mentor object
  def clean(self):
    #make sure DCE is valid
    if (self.dce is None):
      raise ValidationError('The DCE of the mentor cannot be null.')  
    elif (not re.match('^[a-zA-Z]{3}\d{4}$', self.dce)):
      raise ValidationError('The DCE of the mentor is not valid.')
      
    #make sure first name is valid
    if (self.first_name is None):
      raise ValidationError('The first name of the mentor cannot be null.')
    elif (not re.match('^[a-zA-Z][a-zA-Z -]*[^-|^ ]$', self.first_name)):
      raise ValidationError('The first name of the mentor is not valid.') 
    #if it gets here, the first name is all valid except it may have more
    #or dashes than it should... check that
    if (self.first_name.count(" ") > 1 or self.first_name.count("-") > 1):
      raise ValidationError('The first name can only have one space and/or one dash.') 
      
    #make sure last name is valid
    if (self.last_name is None):
      raise ValidationError('The last name of the mentor cannot be null.')
    elif (not re.match('^[a-zA-Z][a-zA-Z-]*[^-|^ ]( [a-zA-Z].\.)?$', self.last_name)):
      raise ValidationError('The last name of the mentor is not valid.') 
