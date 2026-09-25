from django import forms

class LoginForm(forms.Form):
    
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'id_login_username',
            'class': 'form-control', 
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'id_login_password',
            'class': 'form-control',
        })
    )
    