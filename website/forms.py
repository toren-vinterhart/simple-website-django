from django import forms
from website.models import Contact

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactModelForm(forms.ModelForm):
    last_name = forms.CharField(max_length=255)
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email', 'subject']
        # exclude = ['name'] # all fields except name