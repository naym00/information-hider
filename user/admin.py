from django.contrib import admin
from user import models

admin.site.register([
    models.Usertype,
    models.User,
    models.Socialmediaicon,
    models.Socialmedia
    ])
