from django.contrib import admin
from questions.models import *

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass