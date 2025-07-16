from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد نمایید.'}),
        label="نام کاربری"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور خود را وارد نمایید.'}),
        label="رمز عبور"
    )


User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری خود را وارد نمایید.'}),
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='نام کاربری نباید بیش از 20 کارکتر باشد')
        ],
        label="نام کاربری"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد نمایید.'}),
        validators=[
            validators.EmailValidator('ایمیل نامعتبر است')
        ],
        label="ایمیل"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور خود را وارد نمایید.'}),
        label="رمز عبور"
    )
    password2 = forms.CharField(
        label="تایید رمز عبور",
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور خود را مجدد وارد نمایید.'})
    )
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('رمز عبور ها یکسان نمی باشند!')
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)
        if query.exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است!')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username)
        if query.exists():
            raise forms.ValidationError('نام کاربری وجود دارد!')
        return  username