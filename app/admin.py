from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Answer
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'username', 'platform', 'insta_handle', 'profile_image', 'is_staff', 'is_active',)
    list_filter = ('email', 'username', 'platform', 'insta_handle', 'profile_image', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'platform', 'insta_handle', 'profile_image', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'platform', 'insta_handle', 'profile_image', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Question)
admin.site.register(Answer)