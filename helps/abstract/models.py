
from django.db import models
from helps.common.generic import Generichelps as ghelp

def generateuniquecode(): return ghelp().getUniqueCodePattern()

class Basic(models.Model):
    code = models.CharField(max_length=20, unique=True, default=generateuniquecode, editable=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta: 
        abstract = True