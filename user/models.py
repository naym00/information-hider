from helps.choice.common.choices import GENDER, DISTRICTS
from helps.common.generic import Generichelps as ghelp
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from helps.abstract.models import Basic
from django.db import models

def uploadsocialicon(instance, filename):
    return "socialicon/{title}/{filename}".format(title=instance.title, filename=filename)

def generateuniquecode(): return ghelp().getUniqueCodePattern()

class Usertype(models.Model):
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return f'{self.title}'
    
class User(AbstractUser, Basic):
    nickname = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER, default=GENDER[0][0])
    homedistrict = models.CharField(max_length=20, choices=DISTRICTS, blank=True, null=True)
    permanentaddress = models.TextField(blank=True, null=True)
    currentdistrict = models.CharField(max_length=20, choices=DISTRICTS, blank=True, null=True)
    presentaddress = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    type = models.ForeignKey(Usertype, on_delete=models.SET_NULL, blank=True, null=True)
    # phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    draft = models.BooleanField(default=False)

    def getfullname(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else f'{self.first_name}' if self.first_name else f'{self.last_name}'
    
    def get_surname(self):
        return getattr(self, 'nickname', 'No name')
    
    def __str__(self):
        return f'{self.code} {self.username}'
    
    def save(self, *args, **kwargs):
        if self.password: self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
class Socialmediaicon(Basic):
    title = models.CharField(max_length=20, unique=True)
    icon = models.ImageField(upload_to=uploadsocialicon, blank=True, null=True)
    
    def __str__(self):
        return f'{self.code} {self.active} {self.title}'
    
class Socialmedia(Basic):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    socialmediaicon = models.ForeignKey(Socialmediaicon, on_delete=models.SET_NULL, blank=True, null=True)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.code} {self.user.username} {self.socialmediaicon.title}'