from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)})
    )
    
    add_fieldsets =(
        (None, {
            'classes':('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
    )
    search_fields = ('username',)
    ordering = ('id',)
    filter_horizontal = ()     


admin.site.register(User, UserAdmin)


testuser = User.objects.get(username="Abdumutal")
print(testuser.password)