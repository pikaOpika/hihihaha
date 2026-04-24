from django import forms

from catalog.models import LiteraryFormat


class FormatForm(forms.ModelForm):
    class Meta:
        model = LiteraryFormat
        fields = "__all__"
