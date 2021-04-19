from django.contrib import admin

# Register your models here.
from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'bio')


admin.site.register(Owner, OwnerAdmin)
