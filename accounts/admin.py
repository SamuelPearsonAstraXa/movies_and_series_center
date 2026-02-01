from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .managers import CustomUserManager
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    ordering = ('email', 'phone_number')
    search_fields = ('email', 'phone_number')

    list_display = [
        'email', 'first_name', 'last_name', 'username', 'date_of_birth', 'phone_number'
    ]

    fieldsets = (
        (None, {'fields': ('email', 'profile_img', 'username', 'first_name', 'last_name', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'password1', 'password2',
                'profile_img', 'is_staff', 'is_active', 'groups', 'user_permissions', 'date_of_birth',
            ),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)