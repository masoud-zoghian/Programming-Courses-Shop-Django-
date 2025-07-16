from django import forms

class ContactUsForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','maxlength':'20',}),
        label='نام و نام خانوادگی:',
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        label='ایمیل:',
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}),
        label = 'پیام:',
    )