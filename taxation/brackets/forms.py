from django import forms
from .models import UserInfo

class New(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('zip_code', 'salary', 'marital_status',)
