from django.contrib import admin
from . import models

admin.site.register(models.Orphans)
admin.site.register(models.Gender)
admin.site.register(models.Groups)
admin.site.register(models.Relatives)