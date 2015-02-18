from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from import_export.admin import ImportExportModelAdmin

from .models import User, Payment, Tshirt
from .forms import UserChangeForm, UserCreationForm
from .resources import UserResource


class MyUserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name',
                    'gender', 'student_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'student_number', 'gender',
                                      'phone_number')}),
        ('Profile info', {'fields': ('programming_languages', 'courses', )}),
        ('Social', {'fields': ('facebook', 'twitter', 'github', 'linkedin',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name',
                       'last_name', 'student_number', 'gender',
                       'password1', 'password2')}),
    )
    search_fields = ('student_number', 'email', 'first_name', 'last_name')
    ordering = ('student_number', 'email')
    filter_horizontal = ()


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payed_by', 'amount_payed', 'year_payed', 'created_at')
    raw_id_fields = ('payed_by',)
    search_fields = ('student_number', 'email', 'first_name', 'last_name')


class TshirtAdmin(admin.ModelAdmin):
    list_display = ('payed_by', 'amount_payed', 'created_at',
                    'size', 'back_name')
    raw_id_fields = ('payed_by',)
    search_fields = ('student_number', 'email', 'first_name', 'last_name')

admin.site.register(User, MyUserAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Tshirt, TshirtAdmin)
