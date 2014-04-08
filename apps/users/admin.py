from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'gender', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 
                                      'amount_payed')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 
                                    'active_member')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 
                       'last_name', 'gender',
                       'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)
