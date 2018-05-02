from django import forms

class UserForm(forms.Form):
    user_zip = forms.CharField(label='zip code: ', max_length=5)
