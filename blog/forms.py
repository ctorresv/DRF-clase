from django import forms
from .models import Post

""" class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ["titulo", "contenido"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class:" "input"}),
            "contenido": forms.Textarea(attrs={"rows":5})
        }
 """