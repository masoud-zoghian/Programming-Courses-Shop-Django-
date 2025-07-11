from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your password'})
    )


User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your username'}),
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='نام کاربری نباید بیش از 20 کارکتر باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email'}),
        validators=[
            validators.EmailValidator('ایمیل نامعتبر است')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'re-enter your password'})
    )
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('passwords do not match!')
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)
        if query.exists():
            raise forms.ValidationError('this email is already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username)
        if query.exists():
            raise forms.ValidationError('this username is not available')
        return  username