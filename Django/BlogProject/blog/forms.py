from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "content"]
        widgets= {
            "author": forms.Select(attrs={
                "class" : "form-control",
                "id" : "comment_author",
                "name": "comment_author",
                "required": True,
            }),
            "content": forms.Textarea(attrs={
                "class" : "form-control",
                "id" : "comment_content",
                "name": "comment_content",
                "rows":4,
                "required":True

            })


        }