from django.contrib import admin
from .models import NewUser
from django.forms import Textarea
from .form import UserAdminForms


@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):

    model = NewUser
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-start_date',)
    list_filter = ('email', 'username', 'first_name', 'last_name',
                   'is_active', 'is_staff')
    list_display = ['email', 'username', 'first_name', 'last_name']

    fieldsets = (
        ('User Details', {'fields': ('email', 'username', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )

    formfield_overrides = {
        NewUser.about: {
            'widget': Textarea(attrs={
                'rows': 10,
                'cols': 40
            })
        }
    }

    add_fieldset = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
         }),
    )

    form = UserAdminForms
