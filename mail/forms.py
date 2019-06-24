from django import forms
from django.forms import ModelForm
from . import models


class CreateMailList(ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)


    class Meta:
        model = models.MailList
        fields = (
            'name', 
            'email',
        )


    def save(self, commit=True):
        mail_list = super(CreateMailList, self).save(commit=False)
        mail_list.name = (self.cleaned_data['name']).casefold()
        mail_list.email = self.cleaned_data['email'].casefold()
        if commit:
            mail_list.save()

        return mail_list
