from django import forms




class LoginForm(forms.Form):

    email = forms.CharField(
        required=True,
        label='email',
    )
    password = forms.CharField(
        required=True,
        label='password',
        widget=forms.PasswordInput(),
    )

