from django_unicorn.components import UnicornView
from django import forms
from django.contrib.auth.models import Group


class CreateUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    phone_number = forms.CharField()
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)


class CreateUserView(UnicornView):
    form_class = CreateUserForm

    first_name = ""
    last_name = ""
    email = ""
    username = ""
    password = ""
    phone_number = ""
