from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('id', 'username', 'email')


admin.site.register(User, UserAdmin)
