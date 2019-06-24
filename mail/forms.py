from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm
from mail import models


class CreateMailList(ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)


    class Meta:
        model = MailList
        fields = (  
            'name', 
            'email',
        )


    def save(self, commit=True):
        mail_list = super(CreateMailList, self).save(commit=False)
        mail_list.name = (self.cleaned_data['name']).casefold()
        mail_list.email = self.cleaned_data['email'].casefold()
        if commit:
            user.save()

        return mail_list
