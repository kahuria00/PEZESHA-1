from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display=("username","email","password")
	search_fields=("your_name","email")


admin.site.register(User,UserAdmin)


# Register your models here.
