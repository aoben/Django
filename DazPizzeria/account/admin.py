# from django.contrib import admin
# from .models import Profile
# from django.contrib.auth.admin import UserAdmin
#
# admin.site.register(Profile)
#




from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Profile


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(max_length=30)
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()
    fields = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_staff', 'is_superuser', 'is_active')

    def cleaned_password(self):
        return self.initial["password2"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'first_name', 'last_name', 'email', 'password', 'is_admin', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_admin','is_staff', 'is_superuser', 'is_active')
    fieldsets = (
                ('profile', {'fields':('username', 'email', 'password')}),
                ('Personal info', {'fields':('first_name', 'last_name', )}),
                ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')}),
    )

    add_fieldsets = (
                    ('profile', {
                        'classes': ('wide',),
                        'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
                        ),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(Profile, UserAdmin)
