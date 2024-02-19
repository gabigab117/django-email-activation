from django.contrib import admin

from email_activation.models import CustomUser

admin.site.register(CustomUser)
