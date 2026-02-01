from django import forms
from blog.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['name', 'email', 'subject', 'message']
        exclude = ['approved', 'post']

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.post_id = self.post
        if commit:
            comment.save()
        return comment
