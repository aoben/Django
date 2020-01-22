from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

#build forms here


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


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LogInForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'password']
