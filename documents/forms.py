from django import forms
from documents.models import DocFile


class DocFileForm(forms.ModelForm):
    class Meta:
        model = DocFile
        fields = ['docfile']
        exclude = ['name', 'version', 'author']