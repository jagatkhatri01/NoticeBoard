from django import forms
from .models import CRNotice


class CRNoticeForm(forms.ModelForm):
    class Meta:
        model = CRNotice
        fields = ['title', 'content', 'tags']