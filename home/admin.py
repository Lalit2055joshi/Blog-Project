from django.contrib import admin
from .models import *
from home.models import Contact
# Register your models here.


class Contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class Informationadmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'phone', 'time', 'email')


class feedbackadmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'image', 'comment')


admin.site.register(Contact, Contactadmin)
admin.site.register(Feedback, feedbackadmin)
admin.site.register(Information, Informationadmin)
