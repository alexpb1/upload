from django import forms
from django.db.models import fields
from UpWithS3.models import upload

class upload_form(forms.ModelForm):
    class Meta:
        model= upload
        fields='__all__'
    
    def clean(self):
        return self.cleaned_data