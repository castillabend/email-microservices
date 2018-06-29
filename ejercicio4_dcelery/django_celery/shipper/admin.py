from django.contrib import admin

# Register your models here.
from shipper.models import FileUploat


# class AdminUploat(admin.ModelAdmin):

admin.site.register(FileUploat)