from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(required=True,widget=forms.Textarea)