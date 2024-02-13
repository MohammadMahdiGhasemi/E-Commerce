from django import forms
from django.core.exceptions import ValidationError
from .models import Person

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'username', 'email', 'password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError("Passwords don't match")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'username', 'email', 'password', 'role', 'date_time']
        exclude = ['date_time']