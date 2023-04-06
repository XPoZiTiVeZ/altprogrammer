from django.contrib import admin
from .models import Profile, CustomUser
from .forms import CustomCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_email_verified', 'last_login', 'date_joined',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_email_verified',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_email_verified',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2', 'is_staff', 'is_active', 'is_email_verified',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
