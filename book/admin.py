from django.contrib import admin

# Register your models here.

from book import models

admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Activate)
admin.site.register(models.Comment)
admin.site.register(models.Commetupdown)
admin.site.register(models.Inactivate)
admin.site.register(models.Score)
admin.site.register(models.Collect)
# admin.site.register(models.Bookup)