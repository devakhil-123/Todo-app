from django import forms
from .models import todoModel

class todoForm(forms.ModelForm):
    class Meta:
        model=todoModel
        fields="__all__"
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"enter title"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"enter description"}),
            "date":forms.DateInput(attrs={"class":"form-control","placeholder":"enter date"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }