from django import forms

SINGLE_OR_MARRIED = (
    ('S', 'single'),
    ('M', 'married'),
)

class New(forms.Form):
    zip_code = forms.IntegerField()
    salary = forms.DecimalField(max_digits=15, decimal_places=2)
    marital_status = forms.ChoiceField(widget=forms.RadioSelect, choices=SINGLE_OR_MARRIED)
