from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'created_date': forms.DateTimeInput(attrs={'class': 'form-control mb-2'}),
            'updated_date': forms.DateTimeInput(attrs={'class': 'form-control mb-2'}),
        }