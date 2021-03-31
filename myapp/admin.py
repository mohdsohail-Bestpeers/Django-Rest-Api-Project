from django.contrib import admin
from .models import React

class ReactAdmin(admin.ModelAdmin):
  list_display = ['id','Name','Detail']

admin.site.register(React,ReactAdmin)