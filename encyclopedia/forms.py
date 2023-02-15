from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'first name'}))
