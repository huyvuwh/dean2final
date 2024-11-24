from django import forms

class GoogleSheetURLForm(forms.Form):
    sheet_url = forms.URLField(
        label="Google Sheet URL", 
        required=True,
        widget=forms.URLInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nhập URL của Google Sheet'
        })
    )
