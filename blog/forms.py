from django import  forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','summary', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_ttl(self):
        title=self.cleaned_data['title']
        if 'spam' in title.lower():
            raise forms.ValidationError("This title is spam")
        return title