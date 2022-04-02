from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Information)
admin.site.register(models.History)
admin.site.register(models.Security)
admin.site.register(models.Bitcoin)