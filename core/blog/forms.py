from django import forms
from .models import Category

class PostForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    body = forms.CharField(widget=forms.Textarea)
    background_image = forms.ImageField()
    