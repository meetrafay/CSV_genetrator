# yourapp/forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class HomeForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    option = forms.ChoiceField(
        label='Choose Option',
        choices=[('option1', 'Option 1'), ('option2', 'Option 2')],
        widget=forms.RadioSelect()
    )
