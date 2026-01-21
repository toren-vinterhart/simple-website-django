from django import forms
from website.models import Contact, Newsletter


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterModelForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class TestContactModelForm(forms.ModelForm):
    last_name = forms.CharField(max_length=255)
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email', 'subject']
        # exclude = ['name'] # all fields except name