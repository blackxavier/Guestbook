from django import forms
from guestbook.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Your Comment"}
            ),
        }
